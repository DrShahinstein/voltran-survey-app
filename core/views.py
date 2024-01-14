from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from core.models import Question
from .question_handlers import get_first_question_id, next_question_id, prev_question_id


class IndexView(View):
    def get(self, request):
        if Question.objects.exists():
            first_question_id = get_first_question_id()
            return redirect("question-view", pk=first_question_id)
        else:
            return render(request, "404.html")


class QuestionView(View):
    template = "questions.html"

    def get(self, request, pk):
        try:
            self.object = self.get_object(pk)
        except:
            first_question_id = get_first_question_id()
            return redirect("question-view", pk=first_question_id)

        context = self.get_context_data()
        return render(request, self.template, context)

    def post(self, request, pk):
        try:
            self.object = self.get_object(pk)
        except:
            first_question_id = get_first_question_id()
            return redirect("question-view", pk=first_question_id)

        context = self.get_context_data()

        selected_answer = request.POST.get("selected_answer")

        self.update_question_answers(self.object, selected_answer)
        self.object.save()

        next_id = next_question_id(pk)

        return redirect("question-view", pk=next_id)

    def get_context_data(self, **kwargs) -> dict[str, any]:
        question = self.object
        current_question_id = question.pk
        next_id = next_question_id(current_question_id)
        prev_id = prev_question_id(current_question_id)

        context = {
            "current_id": current_question_id,
            "next_id": next_id,
            "prev_id": prev_id,
            "question": question,
            "scale_order": [
                (2, "agree"),
                (1, "agree"),
                (0, "neutral"),
                (1, "disagree"),
                (2, "disagree"),
            ],
            **kwargs,
        }

        return context

    def get_object(self, pk):
        current_question = get_object_or_404(Question, pk=pk)

        next_question = Question.objects.filter(pk=pk).order_by("pk").first()

        if not next_question:
            first_question = Question.objects.order_by("pk").first()
            return first_question

        return next_question

    def update_question_answers(self, question, selected_answer):
        if selected_answer == "strongly agree":
            question.overall_strongly_agree_answers += 1
        elif selected_answer == "agree":
            question.overall_agree_answers += 1
        elif selected_answer == "neutral":
            question.overall_neutral_answers += 1
        elif selected_answer == "disagree":
            question.overall_disagree_answers += 1
        elif selected_answer == "strongly disagree":
            question.overall_strongly_disagree_answers += 1


class ResultsView(View):
    def get(self, request):
        questions = Question.objects.all()
        context = {
            "questions": questions,
        }
        return render(request, "results.html", context)
