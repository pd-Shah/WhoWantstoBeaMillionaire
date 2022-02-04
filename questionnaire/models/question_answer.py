from django.db import models

from .common import CommonBaseModel


class QuestionAnswer(CommonBaseModel):
    POINT = (
        ('5', '5'),
        ('10', '10'),
        ('15', '15'),
        ('20', '20'),
    )

    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True, blank=True)
    answers = models.ManyToManyField('Answer', )
    default_answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name="default_answer_set", null=True,
                                       blank=True)
    point = models.CharField(max_length=2, choices=POINT, default=5)
