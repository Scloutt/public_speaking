from django.contrib import admin
from .models import Team, Rubric, Submission, AuditLog

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "school", "active")
    search_fields = ("name", "school")

@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("team", "judge_name", "score", "created_at")
    list_filter = ("judge_name", "created_at")
    search_fields = ("team__name", "judge_name")

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("action", "user", "created_at")
    list_filter = ("action", "created_at")
    search_fields = ("details",)
