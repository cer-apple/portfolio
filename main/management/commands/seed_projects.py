import json
from pathlib import Path

from django.core.management.base import BaseCommand

from main.models import Project


class Command(BaseCommand):
    help = (
        "Idempotently upsert Project records from main/fixtures/projects.json. "
        "Matches existing rows by slug; creates new ones if missing. "
        "Never deletes records, so admin-only additions are preserved."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--fixture',
            default=str(Path('main') / 'fixtures' / 'projects.json'),
            help='Path to the projects fixture JSON file.',
        )

    def handle(self, *args, **options):
        fixture_path = Path(options['fixture'])
        with fixture_path.open(encoding='utf-8') as fp:
            entries = json.load(fp)

        created = updated = 0
        for entry in entries:
            slug = entry['slug']
            defaults = {k: v for k, v in entry.items() if k != 'slug'}
            _, was_created = Project.objects.update_or_create(
                slug=slug, defaults=defaults,
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(
            f'seed_projects: {created} created, {updated} updated '
            f'(from {fixture_path}).'
        ))
