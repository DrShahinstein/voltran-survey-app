from django.shortcuts import render
from django.views import View
from .models import Question


class IndexView(View):
    def get(self, request):
        questions = Question.objects.all()
        context = {
            "poll_questions": questions,
            "scale_order": [
                (2, "agree"),
                (1, "agree"),
                (0, "neutral"),
                (1, "disagree"),
                (2, "disagree"),
            ],
        }
        return render(request, "index.html", context)
