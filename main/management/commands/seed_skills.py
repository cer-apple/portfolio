import json
from pathlib import Path

from django.core.management.base import BaseCommand

from main.models import Skill


class Command(BaseCommand):
    help = (
        "Idempotently upsert Skill records from main/fixtures/skills.json. "
        "Matches existing rows by (category, name); creates new ones if missing. "
        "Never deletes records, so admin-only additions are preserved."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--fixture',
            default=str(Path('main') / 'fixtures' / 'skills.json'),
            help='Path to the skills fixture JSON file.',
        )

    def handle(self, *args, **options):
        fixture_path = Path(options['fixture'])
        with fixture_path.open(encoding='utf-8') as fp:
            entries = json.load(fp)

        created = updated = 0
        for entry in entries:
            category = entry['category']
            name = entry['name']
            defaults = {
                k: v for k, v in entry.items()
                if k not in {'category', 'name'}
            }
            _, was_created = Skill.objects.update_or_create(
                category=category, name=name, defaults=defaults,
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(
            f'seed_skills: {created} created, {updated} updated '
            f'(from {fixture_path}).'
        ))
