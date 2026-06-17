from django.urls import path
from . import views

app_name = "debate"

urlpatterns = [
    path("", views.home, name="home"),
    path("rubrics/", views.rubric_list, name="rubric_list"),
    path("submit/", views.submission_create, name="submission_create"),
    path("export/submissions/", views.export_submissions_csv, name="export_submissions_csv"),
    path("api/queue-sync/", views.queue_sync, name="queue_sync"),
]
