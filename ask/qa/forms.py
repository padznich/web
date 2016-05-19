from django import forms

from models import Question, Answer, User


class LoginForm(forms.Form):

    login = forms.CharField(max_length=50)
    password = forms.PasswordInput()
    email = forms.CharField(max_length=50)


class AskForm(forms.Form):

    def __init__(self, *args, **kwargs):

        super(AskForm, self).__init__(*args, **kwargs)

    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        title = self.cleaned_data.get('title')
        text = self.cleaned_data.get('text')
        if title is None or len(title) < 5:
            raise forms.ValidationError(u'Title must contains more than 5 characters')
        if text is None or len(text) < 5:
            raise forms.ValidationError(u'Text must contains more than 5 characters')
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        if question.author_id:
            question.author_id += 1
        else:
            question.author_id = 1
        question.save()
        return question


class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    _user = User()

    def clean(self):
        text = self.cleaned_data.get('text')
        question = self.cleaned_data.get('question')
        if question is not int:
            raise forms.ValidationError(u'question must be an integer')
        if text is None or len(text) < 5:
            raise forms.ValidationError(u'Text must contains more than 5 characters')
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
