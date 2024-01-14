from core.models import Question
from django.shortcuts import get_object_or_404


def get_first_question_id():
    return Question.objects.first().pk


def next_question_id(current_question_id):
    current_question = get_object_or_404(Question, pk=current_question_id)

    next_question = (
        Question.objects.filter(pk__gt=current_question_id).order_by("pk").first()
    )

    if not next_question:
        return get_first_question_id()

    return next_question.pk


def prev_question_id(current_question_id):
    current_question = get_object_or_404(Question, pk=current_question_id)
    prev_question = (
        Question.objects.filter(pk__lt=current_question_id).order_by("-pk").first()
    )

    if not prev_question:
        return get_first_question_id()

    return prev_question.pk
