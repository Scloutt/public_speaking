from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=128)
    school = models.CharField(max_length=128, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Rubric(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Submission(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    judge_name = models.CharField(max_length=128)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team} by {self.judge_name}"


class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=256)
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} @ {self.created_at.isoformat()}"
