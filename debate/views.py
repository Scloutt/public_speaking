from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import SubmissionForm
from .models import Team, Rubric, Submission, AuditLog


def staff_required(view_func):
    return user_passes_test(lambda u: u.is_active and u.is_staff)(view_func)


def home(request):
    teams = Team.objects.filter(active=True)
    return render(request, "debate/home.html", {"teams": teams})


@login_required
def rubric_list(request):
    rubrics = Rubric.objects.all().order_by("-created_at")
    return render(request, "debate/rubric_list.html", {"rubrics": rubrics})


@login_required
def submission_create(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save()
            AuditLog.objects.create(
                user=request.user,
                action="submission_created",
                details=f"Submission {submission.id} created for {submission.team}",
            )
            if request.htmx:
                return render(request, "debate/partials/submission_success.html", {"submission": submission})
            return redirect(reverse("debate:home"))
    else:
        form = SubmissionForm()
    return render(request, "debate/submission_form.html", {"form": form})


@login_required
@staff_required
def export_submissions_csv(request):
    submissions = Submission.objects.select_related("team").order_by("created_at")
    rows = ["id,team,judge_name,score,comments,created_at"]
    for item in submissions:
        rows.append(",".join([
            str(item.id),
            item.team.name,
            item.judge_name,
            str(item.score),
            item.comments.replace(",", " "),
            item.created_at.isoformat(),
        ]))
    return HttpResponse("\n".join(rows), content_type="text/csv")


@login_required
@staff_required
def queue_sync(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed."}, status=405)
    payload = request.body.decode("utf-8")
    return JsonResponse({"status": "ok", "received": payload})
