from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = [
        "question",
        "overall_strongly_agree_answers",
        "overall_agree_answers",
        "overall_neutral_answers",
        "overall_disagree_answers",
        "overall_strongly_disagree_answers",
    ]


admin.site.register(Question, QuestionAdmin)
