from django.db import models
from django.urls import reverse
from django.utils.translation import get_language, gettext_lazy as _


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('chatbot', 'Chatbot'),
        ('n8n', 'n8n Agent Workflow'),
        ('langchain', 'LangChain Agent'),
        ('media', 'Google AI Studio Media'),
        ('ml', 'Machine Learning (scikit-learn)'),
        ('django', 'Django'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    summary = models.CharField(
        max_length=300,
        help_text='One-sentence summary shown on the list page.',
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other',
    )
    business_problem = models.TextField(
        help_text='The real-world problem this project addresses.',
    )
    tools_used = models.CharField(
        max_length=300,
        help_text='Comma-separated, e.g. "Python, Django, OpenAI API".',
    )
    key_features = models.TextField(
        help_text='One feature per line.',
    )
    role = models.TextField(
        help_text='Your role and contribution.',
    )
    biggest_challenge = models.TextField()
    lessons_learned = models.TextField()

    # Japanese translations — optional, fall back to English when blank.
    summary_ja = models.CharField(max_length=300, blank=True, default='')
    business_problem_ja = models.TextField(blank=True, default='')
    tools_used_ja = models.CharField(max_length=300, blank=True, default='')
    key_features_ja = models.TextField(blank=True, default='')
    role_ja = models.TextField(blank=True, default='')
    biggest_challenge_ja = models.TextField(blank=True, default='')
    lessons_learned_ja = models.TextField(blank=True, default='')

    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(
        default=0,
        help_text='Lower numbers show first.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def _localized(self, base):
        if get_language() == 'ja':
            ja = (getattr(self, f'{base}_ja', '') or '').strip()
            if ja:
                return ja
        return getattr(self, base)

    @property
    def localized_summary(self):
        return self._localized('summary')

    @property
    def localized_business_problem(self):
        return self._localized('business_problem')

    @property
    def localized_role(self):
        return self._localized('role')

    @property
    def localized_biggest_challenge(self):
        return self._localized('biggest_challenge')

    @property
    def localized_lessons_learned(self):
        return self._localized('lessons_learned')

    def tools_list(self):
        source = self._localized('tools_used')
        return [t.strip() for t in source.split(',') if t.strip()]

    def features_list(self):
        source = self._localized('key_features')
        return [f.strip() for f in source.splitlines() if f.strip()]


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming_languages', _('Programming Languages')),
        ('ai_ml', _('AI / Machine Learning')),
        ('business', _('Business / Sales')),
        ('languages', _('Languages')),
        ('tools', _('Tools / Frameworks')),
    ]

    CATEGORY_ICONS = {
        'programming_languages': '📊',
        'ai_ml': '🤖',
        'business': '💼',
        'languages': '🌐',
        'tools': '🛠',
    }

    CATEGORY_DISPLAY_ORDER = [
        'programming_languages',
        'ai_ml',
        'business',
        'languages',
        'tools',
    ]

    PROFICIENCY_CHOICES = [
        ('beginner', _('Beginner')),
        ('intermediate', _('Intermediate')),
        ('advanced', _('Advanced')),
        ('expert', _('Expert')),
        ('native', _('Native')),
        ('business_professional', _('Business Professional')),
    ]

    name = models.CharField(max_length=100)
    name_ja = models.CharField(max_length=100, blank=True, default='')
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)
    proficiency = models.CharField(max_length=30, choices=PROFICIENCY_CHOICES)
    icon = models.CharField(
        max_length=8,
        blank=True,
        default='',
        help_text='Optional emoji or short symbol shown next to the skill name.',
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text='Lower numbers show first within a category.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order', 'id']

    def __str__(self):
        return f'{self.name} ({self.get_proficiency_display()})'

    @property
    def localized_name(self):
        if get_language() == 'ja' and self.name_ja:
            return self.name_ja
        return self.name

    @property
    def category_icon(self):
        return self.CATEGORY_ICONS.get(self.category, '')
