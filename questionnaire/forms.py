from django import forms


class QuestionAnswerForm(forms.Form):
    def __init__(self, current_user, *args, **kwargs):
        super(QuestionAnswerForm, self).__init__(*args, **kwargs)
        question_answers_set = current_user.questions.all()
        for index, question_answers in enumerate(question_answers_set):
            self.fields[question_answers.question.title] = forms.ChoiceField(
                choices=[(answer.title, answer.title) for answer in question_answers.answers.all()],
                widget=forms.RadioSelect(), )
