from django.contrib import admin

from .models import Project, Skill


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


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('category', 'order', 'name', 'proficiency', 'icon', 'updated_at')
    list_display_links = ('name',)
    list_editable = ('order',)
    list_filter = ('category', 'proficiency')
    search_fields = ('name', 'name_ja')
    fieldsets = (
        (None, {
            'fields': ('category', 'name', 'name_ja', 'proficiency', 'icon', 'order'),
        }),
    )
