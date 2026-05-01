from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # 301 redirects for the old paths so previously shared links keep working.
    path('top/', RedirectView.as_view(pattern_name='home', permanent=True)),
    path('profile/', RedirectView.as_view(pattern_name='about', permanent=True)),
    path('education/', views.education, name='education'),
    path('work/', views.work, name='work'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path('advisory/', views.advisory, name='advisory'),
    path('advisory/detail/', views.advisory_detail, name='advisory_detail'),
    path('hobby/', views.hobby, name='hobby'),
    path('skills/', views.skills, name='skills'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
]
