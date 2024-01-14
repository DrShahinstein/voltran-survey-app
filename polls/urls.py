from django.contrib import admin
from django.urls import path
from core.views import IndexView, QuestionView, ResultsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("question/<int:pk>/", QuestionView.as_view(), name="question-view"),
    path("results/", ResultsView.as_view(), name="results"),
]
