from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('profile/', views.profile, name='profile'),
    path('education/', views.education, name='education'),
    path('work/', views.work, name='work'),
    path('contact/', views.contact, name='contact'),
]
