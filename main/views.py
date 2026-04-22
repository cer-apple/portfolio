from django.shortcuts import render


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


