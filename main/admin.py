from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'category', 'updated_at')
    list_display_links = ('title',)
    list_editable = ('order',)
    list_filter = ('category',)
    search_fields = ('title', 'summary', 'tools_used')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Overview', {
            'fields': ('title', 'slug', 'category', 'summary', 'order'),
        }),
        ('Detail page content (English)', {
            'fields': (
                'business_problem',
                'tools_used',
                'key_features',
                'role',
                'biggest_challenge',
                'lessons_learned',
            ),
        }),
        ('Detail page content (日本語) — leave blank to fall back to English', {
            'classes': ('collapse',),
            'fields': (
                'summary_ja',
                'business_problem_ja',
                'tools_used_ja',
                'key_features_ja',
                'role_ja',
                'biggest_challenge_ja',
                'lessons_learned_ja',
            ),
        }),
        ('Visuals & links', {
            'fields': ('image', 'github_url', 'demo_url'),
        }),
    )
