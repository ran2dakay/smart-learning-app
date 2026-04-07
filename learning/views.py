from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Technology, Roadmap, Topic, Progress
from .forms import RegisterForm
import json


def landing(request):
    technologies = Technology.objects.all()
    context = {
        'technologies': technologies,
        'user': request.user,
    }
    return render(request, 'learning/landing.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Smart Learning Platform, {user.username}!')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    technologies = Technology.objects.all()
    user = request.user

    tech_data = []
    total_topics = 0
    total_completed = 0

    for tech in technologies:
        tech_topics = Topic.objects.filter(roadmap__technology=tech).count()
        tech_completed = Progress.objects.filter(
            user=user,
            topic__roadmap__technology=tech,
            completed=True
        ).count()
        percent = int((tech_completed / tech_topics * 100)) if tech_topics > 0 else 0
        tech_data.append({
            'tech': tech,
            'topics': tech_topics,
            'completed': tech_completed,
            'remaining': tech_topics - tech_completed,
            'percent': percent,
        })
        total_topics += tech_topics
        total_completed += tech_completed

    overall_percent = int((total_completed / total_topics * 100)) if total_topics > 0 else 0

    context = {
        'tech_data': tech_data,
        'total_topics': total_topics,
        'total_completed': total_completed,
        'total_remaining': total_topics - total_completed,
        'overall_percent': overall_percent,
    }
    return render(request, 'learning/dashboard.html', context)


@login_required
def technology_detail(request, tech_id):
    technology = get_object_or_404(Technology, id=tech_id)
    roadmaps = Roadmap.objects.filter(technology=technology).prefetch_related('topics')
    user = request.user

    roadmap_data = []
    for roadmap in roadmaps:
        topics_with_progress = []
        for topic in roadmap.topics.all():
            progress, _ = Progress.objects.get_or_create(user=user, topic=topic)
            topics_with_progress.append({
                'topic': topic,
                'progress': progress,
            })
        total = roadmap.topics.count()
        completed = Progress.objects.filter(user=user, topic__roadmap=roadmap, completed=True).count()
        percent = int((completed / total * 100)) if total > 0 else 0
        roadmap_data.append({
            'roadmap': roadmap,
            'topics_with_progress': topics_with_progress,
            'total': total,
            'completed': completed,
            'remaining': total - completed,
            'percent': percent,
        })

    context = {
        'technology': technology,
        'roadmap_data': roadmap_data,
    }
    return render(request, 'learning/technology_detail.html', context)


@login_required
def roadmap_detail(request, roadmap_id):
    roadmap = get_object_or_404(Roadmap, id=roadmap_id)
    user = request.user
    topics_with_progress = []
    for topic in roadmap.topics.all():
        progress, _ = Progress.objects.get_or_create(user=user, topic=topic)
        topics_with_progress.append({
            'topic': topic,
            'progress': progress,
        })
    total = roadmap.topics.count()
    completed = Progress.objects.filter(user=user, topic__roadmap=roadmap, completed=True).count()
    percent = int((completed / total * 100)) if total > 0 else 0

    context = {
        'roadmap': roadmap,
        'topics_with_progress': topics_with_progress,
        'total': total,
        'completed': completed,
        'remaining': total - completed,
        'percent': percent,
    }
    return render(request, 'learning/roadmap_detail.html', context)


@login_required
@require_POST
def toggle_progress(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    progress, created = Progress.objects.get_or_create(user=request.user, topic=topic)
    progress.completed = not progress.completed
    if progress.completed:
        progress.completed_at = timezone.now()
    else:
        progress.completed_at = None
    progress.save()

    roadmap = topic.roadmap
    total = roadmap.topics.count()
    completed_count = Progress.objects.filter(
        user=request.user, topic__roadmap=roadmap, completed=True
    ).count()
    percent = int((completed_count / total * 100)) if total > 0 else 0

    return JsonResponse({
        'completed': progress.completed,
        'roadmap_percent': percent,
        'completed_count': completed_count,
        'remaining_count': total - completed_count,
    })


@login_required
def get_progress_data(request):
    user = request.user
    tech_progress = []
    for tech in Technology.objects.all():
        total = Topic.objects.filter(roadmap__technology=tech).count()
        completed = Progress.objects.filter(user=user, topic__roadmap__technology=tech, completed=True).count()
        percent = int((completed / total * 100)) if total > 0 else 0
        tech_progress.append({
            'id': tech.id,
            'name': tech.name,
            'total': total,
            'completed': completed,
            'percent': percent,
        })
    return JsonResponse({'technologies': tech_progress})
