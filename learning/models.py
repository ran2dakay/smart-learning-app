from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='code')
    color = models.CharField(max_length=20, default='primary')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.name


class Roadmap(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='roadmaps')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.technology.name} - {self.get_level_display()}: {self.title}"

    def get_topic_count(self):
        return self.topics.count()

    def get_completed_count(self, user):
        return Progress.objects.filter(user=user, topic__roadmap=self, completed=True).count()

    def get_progress_percent(self, user):
        total = self.get_topic_count()
        if total == 0:
            return 0
        completed = self.get_completed_count(user)
        return int((completed / total) * 100)


class Topic(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=200)
    explanation = models.TextField()
    example = models.TextField()
    learning_objective = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.roadmap.technology.name} > {self.roadmap.get_level_display()} > {self.name}"


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='progress')
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'topic')

    def __str__(self):
        status = 'Completed' if self.completed else 'In Progress'
        return f"{self.user.username} - {self.topic.name} ({status})"
