from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('technology/<int:tech_id>/', views.technology_detail, name='technology_detail'),
    path('roadmap/<int:roadmap_id>/', views.roadmap_detail, name='roadmap_detail'),
    path('toggle-progress/<int:topic_id>/', views.toggle_progress, name='toggle_progress'),
    path('api/progress/', views.get_progress_data, name='progress_data'),
]
