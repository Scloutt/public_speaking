from django import forms
from .models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["team", "judge_name", "score", "comments"]
        widgets = {
            "comments": forms.Textarea(attrs={"rows": 3}),
        }
