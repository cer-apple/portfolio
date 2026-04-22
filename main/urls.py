from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('profile/', views.profile, name='profile'),
    path('education/', views.education, name='education'),
    path('work/', views.work, name='work'),
    path('advisory/', views.advisory, name='advisory'),
    path('advisory/detail/', views.advisory_detail, name='advisory_detail'),
    path('hobby/', views.hobby, name='hobby'),
    path('contact/', views.contact, name='contact'),
]
