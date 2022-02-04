from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from user.models import User
from .forms import QuestionAnswerForm


class Index(generic.TemplateView):
    template_name = 'questionnaire/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_users'] = User.objects.count()
        context['top_ten'] = User.objects.order_by('-score')[:10]

        return context


@login_required
def new_game(request, ):
    """
    View function for renewing a specific BookInstance by librarian
    """
    current_user = request.user

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = QuestionAnswerForm(current_user, request.POST)

        # Check if the form is valid:
        if form.is_valid():
            correct = []
            wrong = []
            question_answers_set = current_user.questions.all()
            for index, question_answers in enumerate(question_answers_set):
                user_answer = form.cleaned_data[question_answers.question.title]
                if user_answer == question_answers.default_answer.title:
                    current_user.score = int(current_user.score) + int(question_answers.point)
                    current_user.save()
                    correct.append(question_answers.question)
                else:
                    wrong.append(question_answers.question)

            return render(request, 'questionnaire/result.html',
                          {'correct': correct, 'wrong': wrong, 'score': current_user.score})

    # If this is a GET (or any other method) create the default form.
    else:
        current_user.new_game()
        form = QuestionAnswerForm(current_user)

    return render(request, 'questionnaire/new_game.html', {'form': form, })
