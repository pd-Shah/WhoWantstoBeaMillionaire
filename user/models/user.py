import random

from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db import models

from questionnaire.models import QuestionAnswer
from .common import CommonModel
from ..managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, CommonModel):
    title = models.CharField(max_length=256, blank=True, null=True, )
    phone = models.CharField('Phone Number', max_length=11, unique=True, )
    profile = models.OneToOneField("Profile", null=True, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    score = models.IntegerField(default=0, )
    questions = models.ManyToManyField('questionnaire.QuestionAnswer')
    objects = UserManager()
    USERNAME_FIELD = 'phone'

    # REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.phone

    def new_game(self, ):
        self.questions.clear()
        items = list(QuestionAnswer.objects.all())
        random_questions = random.sample(items, 5)
        [self.questions.add(q) for q in random_questions]
