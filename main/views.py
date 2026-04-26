from django.shortcuts import get_object_or_404, render

from .models import Project


def top(request):
    """Home page view"""
    return render(request, 'top.html')


def profile(request):
    """Profile page view"""
    return render(request, 'profile.html')


def education(request):
    """Education page view"""
    return render(request, 'education.html')


def work(request):
    """Work history page view"""
    return render(request, 'work.html')


def contact(request):
    """Contact page view"""
    return render(request, 'contact.html')


def hobby(request):
    """Hobby page view"""
    return render(request, 'hobby.html')


def advisory(request):
    """Advisory & Consulting summary page"""
    return render(request, 'advisory.html')


def advisory_detail(request):
    """Advisory & Consulting detail page with services and contact CTA"""
    context = {
        'contact_form_url': 'https://docs.google.com/forms/d/e/1FAIpQLScK6VOUFJetWAJvklLkR-zUz-n0vXXYUObrRRAg3q9nHahjUw/viewform',
    }
    return render(request, 'advisory_detail.html', context)


def projects(request):
    """Projects list page — shows all Project records."""
    return render(request, 'projects.html', {'projects': Project.objects.all()})


def project_detail(request, slug):
    """Individual project detail page."""
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})


