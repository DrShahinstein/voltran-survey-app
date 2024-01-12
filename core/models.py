from django.db import models


class Question(models.Model):
    question = models.CharField("Soru", max_length=80, default="your question")

    overall_strongly_agree_answers = models.IntegerField(
        "Bu soruya kesinlikle katılanların sayısı", default=0
    )
    overall_agree_answers = models.IntegerField(
        "Bu soruya katılanların sayısı", default=0
    )
    overall_neutral_answers = models.IntegerField(
        "Bu soru için nötr olanların sayısı", default=0
    )
    overall_disagree_answers = models.IntegerField(
        "Bu soruya katılmayanların sayısı", default=0
    )
    overall_strongly_disagree_answers = models.IntegerField(
        "Bu soruya kesinlikle katılmayanların sayısı", default=0
    )

    def __str__(self):
        return self.question
