from django.contrib import admin
from .models import UserProfile, Technology, Roadmap, Topic, Progress


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']


@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    list_display = ['technology', 'level', 'title', 'order']
    list_filter = ['technology', 'level']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'roadmap', 'order']
    list_filter = ['roadmap__technology', 'roadmap__level']


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'topic', 'completed', 'completed_at']
    list_filter = ['completed', 'user']
