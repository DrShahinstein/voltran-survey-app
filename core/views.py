from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from core.models import Question


class IndexView(View):
    def get(self, request):
        if Question.objects.exists():
            return redirect("question-view", pk=1)
        else:
            return render(request, "404.html")


class QuestionView(View):
    def get(self, request, pk):
        try:
            self.object = self.get_object(pk)
        except:
            return redirect("question-view", pk=1)

        context = self.get_context_data()
        return render(request, "questions.html", context)

    def post(self, request, pk):
        try:
            self.object = self.get_object(pk)
        except:
            return redirect("question-view", pk=1)

        context = self.get_context_data()

        response = {
            "success": {"success": "Answer submitted successfully"},
            "error": {"error": "Invalid request data"},
        }

        question_text = request.POST.get("question_text")
        selected_answer = request.POST.get("selected_answer")

        if not question_text or not selected_answer:
            return JsonResponse(response["error"], status=400)

        question = get_object_or_404(Question, question=question_text)

        self.update_question_answers(question, selected_answer)
        question.save()

        return render(request, "questions.html", context)

    def get_context_data(self, **kwargs) -> dict[str, any]:
        question = self.object
        context = {
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
        return get_object_or_404(Question, pk=pk)

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
