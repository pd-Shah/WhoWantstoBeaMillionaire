import os

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WhoWantstoBeaMillionaire.settings')
django.setup()

from questionnaire.models import QuestionAnswer
from user.models import User

fake = Faker()


def create_question_answer():
    for i in range(1, 100):
        qa = QuestionAnswer.objects.get(pk=i)
        qa.default_answer = qa.answers.all()[0]
        qa.save()


def create_user_answer():
    user = User.objects.get(pk=1)
    for i in range(5):
        qa = QuestionAnswer.objects.get(pk=fake.random_int(min=0, max=QuestionAnswer.objects.count()))
        user.questions.add(qa)


if __name__ == "__main__":
    create_question_answer()
    create_user_answer()
