from .models import QuesModel, QuizCategoryModel
from django import forms

class PQuizForm(forms.Form):
    listQuestions = list(QuesModel.objects.filter(category='P'))  
    CHOICES_1 = (
        (listQuestions[0].op1,listQuestions[0].op1),
        (listQuestions[0].op2,listQuestions[0].op2),
        (listQuestions[0].op3,listQuestions[0].op3),
        (listQuestions[0].op4,listQuestions[0].op4),
    )
    answers1 = forms.CharField(label=listQuestions[0].question, widget=forms.Select(choices = CHOICES_1), required=True)

    CHOICES_2 = (
        (listQuestions[1].op1,listQuestions[1].op1),
        (listQuestions[1].op2,listQuestions[1].op2),
        (listQuestions[1].op3,listQuestions[1].op3),
        (listQuestions[1].op4,listQuestions[1].op4),
    )
    answers2 = forms.CharField(label=listQuestions[1].question,widget=forms.Select(choices = CHOICES_2), required=True)

    CHOICES_3 = (
        (listQuestions[2].op1,listQuestions[2].op1),
        (listQuestions[2].op2,listQuestions[2].op2),
        (listQuestions[2].op3,listQuestions[2].op3),
        (listQuestions[2].op4,listQuestions[2].op4),
    )
    answers3 = forms.CharField(label=listQuestions[2].question, widget=forms.Select(choices = CHOICES_3), required=True)

    CHOICES_4 = (
        (listQuestions[3].op1,listQuestions[3].op1),
        (listQuestions[3].op2,listQuestions[3].op2),
        (listQuestions[3].op3,listQuestions[3].op3),
        (listQuestions[3].op4,listQuestions[3].op4),
    )
    answers4 = forms.CharField(label=listQuestions[3].question, widget=forms.Select(choices = CHOICES_4), required=True)


    CHOICES_5 = (
        (listQuestions[4].op1,listQuestions[4].op1),
        (listQuestions[4].op2,listQuestions[4].op2),
        (listQuestions[4].op3,listQuestions[4].op3),
        (listQuestions[4].op4,listQuestions[4].op4),
    )
    answers5 = forms.CharField(label=listQuestions[4].question, widget=forms.Select(choices = CHOICES_5), required=True)


    CHOICES_6 = (
        (listQuestions[5].op1,listQuestions[5].op1),
        (listQuestions[5].op2,listQuestions[5].op2),
        (listQuestions[5].op3,listQuestions[5].op3),
        (listQuestions[5].op4,listQuestions[5].op4),
    )
    answers6 = forms.CharField(label=listQuestions[5].question, widget=forms.Select(choices = CHOICES_6), required=True)


    CHOICES_7 = (
        (listQuestions[6].op1,listQuestions[6].op1),
        (listQuestions[6].op2,listQuestions[6].op2),
        (listQuestions[6].op3,listQuestions[6].op3),
        (listQuestions[6].op4,listQuestions[6].op4),
    )
    answers7 = forms.CharField(label=listQuestions[6].question, widget=forms.Select(choices = CHOICES_7), required=True)


    CHOICES_8 = (
        (listQuestions[7].op1,listQuestions[7].op1),
        (listQuestions[7].op2,listQuestions[7].op2),
        (listQuestions[7].op3,listQuestions[7].op3),
        (listQuestions[7].op4,listQuestions[7].op4),
    )
    answers8 = forms.CharField(label=listQuestions[7].question, widget=forms.Select(choices = CHOICES_8), required=True)


    CHOICES_9 = (
        (listQuestions[8].op1,listQuestions[8].op1),
        (listQuestions[8].op2,listQuestions[8].op2),
        (listQuestions[8].op3,listQuestions[8].op3),
        (listQuestions[8].op4,listQuestions[8].op4),
    )
    answers9 = forms.CharField(label=listQuestions[8].question, widget=forms.Select(choices = CHOICES_9), required=True)


    CHOICES_10 = (
        (listQuestions[9].op1,listQuestions[9].op1),
        (listQuestions[9].op2,listQuestions[9].op2),
        (listQuestions[9].op3,listQuestions[9].op3),
        (listQuestions[9].op4,listQuestions[9].op4),
    )
    answers10 = forms.CharField(label=listQuestions[9].question, widget=forms.Select(choices = CHOICES_10), required=True)

class SQuizForm(forms.Form):
    listQuestions = list(QuesModel.objects.filter(category='S'))  
    CHOICES_1 = (
        (listQuestions[0].op1,listQuestions[0].op1),
        (listQuestions[0].op2,listQuestions[0].op2),
        (listQuestions[0].op3,listQuestions[0].op3),
        (listQuestions[0].op4,listQuestions[0].op4),
    )
    answers1 = forms.CharField(label=listQuestions[0].question, widget=forms.Select(choices = CHOICES_1), required=True)

    CHOICES_2 = (
        (listQuestions[1].op1,listQuestions[1].op1),
        (listQuestions[1].op2,listQuestions[1].op2),
        (listQuestions[1].op3,listQuestions[1].op3),
        (listQuestions[1].op4,listQuestions[1].op4),
    )
    answers2 = forms.CharField(label=listQuestions[1].question,widget=forms.Select(choices = CHOICES_2), required=True)

    CHOICES_3 = (
        (listQuestions[2].op1,listQuestions[2].op1),
        (listQuestions[2].op2,listQuestions[2].op2),
        (listQuestions[2].op3,listQuestions[2].op3),
        (listQuestions[2].op4,listQuestions[2].op4),
    )
    answers3 = forms.CharField(label=listQuestions[2].question, widget=forms.Select(choices = CHOICES_3), required=True)

    CHOICES_4 = (
        (listQuestions[3].op1,listQuestions[3].op1),
        (listQuestions[3].op2,listQuestions[3].op2),
        (listQuestions[3].op3,listQuestions[3].op3),
        (listQuestions[3].op4,listQuestions[3].op4),
    )
    answers4 = forms.CharField(label=listQuestions[3].question, widget=forms.Select(choices = CHOICES_4), required=True)


    CHOICES_5 = (
        (listQuestions[4].op1,listQuestions[4].op1),
        (listQuestions[4].op2,listQuestions[4].op2),
        (listQuestions[4].op3,listQuestions[4].op3),
        (listQuestions[4].op4,listQuestions[4].op4),
    )
    answers5 = forms.CharField(label=listQuestions[4].question, widget=forms.Select(choices = CHOICES_5), required=True)


    CHOICES_6 = (
        (listQuestions[5].op1,listQuestions[5].op1),
        (listQuestions[5].op2,listQuestions[5].op2),
        (listQuestions[5].op3,listQuestions[5].op3),
        (listQuestions[5].op4,listQuestions[5].op4),
    )
    answers6 = forms.CharField(label=listQuestions[5].question, widget=forms.Select(choices = CHOICES_6), required=True)


    CHOICES_7 = (
        (listQuestions[6].op1,listQuestions[6].op1),
        (listQuestions[6].op2,listQuestions[6].op2),
        (listQuestions[6].op3,listQuestions[6].op3),
        (listQuestions[6].op4,listQuestions[6].op4),
    )
    answers7 = forms.CharField(label=listQuestions[6].question, widget=forms.Select(choices = CHOICES_7), required=True)


    CHOICES_8 = (
        (listQuestions[7].op1,listQuestions[7].op1),
        (listQuestions[7].op2,listQuestions[7].op2),
        (listQuestions[7].op3,listQuestions[7].op3),
        (listQuestions[7].op4,listQuestions[7].op4),
    )
    answers8 = forms.CharField(label=listQuestions[7].question, widget=forms.Select(choices = CHOICES_8), required=True)


    CHOICES_9 = (
        (listQuestions[8].op1,listQuestions[8].op1),
        (listQuestions[8].op2,listQuestions[8].op2),
        (listQuestions[8].op3,listQuestions[8].op3),
        (listQuestions[8].op4,listQuestions[8].op4),
    )
    answers9 = forms.CharField(label=listQuestions[8].question, widget=forms.Select(choices = CHOICES_9), required=True)


    CHOICES_10 = (
        (listQuestions[9].op1,listQuestions[9].op1),
        (listQuestions[9].op2,listQuestions[9].op2),
        (listQuestions[9].op3,listQuestions[9].op3),
        (listQuestions[9].op4,listQuestions[9].op4),
   )
    answers10 = forms.CharField(label=listQuestions[9].question, widget=forms.Select(choices = CHOICES_10), required=True)

class CQuizForm(forms.Form):
    listQuestions = list(QuesModel.objects.filter(category='C'))  
    CHOICES_1 = (
        (listQuestions[0].op1,listQuestions[0].op1),
        (listQuestions[0].op2,listQuestions[0].op2),
        (listQuestions[0].op3,listQuestions[0].op3),
        (listQuestions[0].op4,listQuestions[0].op4),
    )
    answers1 = forms.CharField(label=listQuestions[0].question, widget=forms.Select(choices = CHOICES_1), required=True)

    CHOICES_2 = (
        (listQuestions[1].op1,listQuestions[1].op1),
        (listQuestions[1].op2,listQuestions[1].op2),
        (listQuestions[1].op3,listQuestions[1].op3),
        (listQuestions[1].op4,listQuestions[1].op4),
    )
    answers2 = forms.CharField(label=listQuestions[1].question,widget=forms.Select(choices = CHOICES_2), required=True)

    CHOICES_3 = (
        (listQuestions[2].op1,listQuestions[2].op1),
        (listQuestions[2].op2,listQuestions[2].op2),
        (listQuestions[2].op3,listQuestions[2].op3),
        (listQuestions[2].op4,listQuestions[2].op4),
    )
    answers3 = forms.CharField(label=listQuestions[2].question, widget=forms.Select(choices = CHOICES_3), required=True)

    CHOICES_4 = (
        (listQuestions[3].op1,listQuestions[3].op1),
        (listQuestions[3].op2,listQuestions[3].op2),
        (listQuestions[3].op3,listQuestions[3].op3),
        (listQuestions[3].op4,listQuestions[3].op4),
    )
    answers4 = forms.CharField(label=listQuestions[3].question, widget=forms.Select(choices = CHOICES_4), required=True)

    CHOICES_5 = (
        (listQuestions[4].op1,listQuestions[4].op1),
        (listQuestions[4].op2,listQuestions[4].op2),
        (listQuestions[4].op3,listQuestions[4].op3),
        (listQuestions[4].op4,listQuestions[4].op4),
    )
    answers5 = forms.CharField(label=listQuestions[4].question, widget=forms.Select(choices = CHOICES_5), required=True)

    CHOICES_6 = (
        (listQuestions[5].op1,listQuestions[5].op1),
        (listQuestions[5].op2,listQuestions[5].op2),
        (listQuestions[5].op3,listQuestions[5].op3),
        (listQuestions[5].op4,listQuestions[5].op4),
    )
    answers6 = forms.CharField(label=listQuestions[5].question, widget=forms.Select(choices = CHOICES_6), required=True)


    CHOICES_7 = (
        (listQuestions[6].op1,listQuestions[6].op1),
        (listQuestions[6].op2,listQuestions[6].op2),
        (listQuestions[6].op3,listQuestions[6].op3),
        (listQuestions[6].op4,listQuestions[6].op4),
    )
    answers7 = forms.CharField(label=listQuestions[6].question, widget=forms.Select(choices = CHOICES_7), required=True)


    CHOICES_8 = (
        (listQuestions[7].op1,listQuestions[7].op1),
        (listQuestions[7].op2,listQuestions[7].op2),
        (listQuestions[7].op3,listQuestions[7].op3),
        (listQuestions[7].op4,listQuestions[7].op4),
    )
    answers8 = forms.CharField(label=listQuestions[7].question, widget=forms.Select(choices = CHOICES_8), required=True)


    CHOICES_9 = (
        (listQuestions[8].op1,listQuestions[8].op1),
        (listQuestions[8].op2,listQuestions[8].op2),
        (listQuestions[8].op3,listQuestions[8].op3),
        (listQuestions[8].op4,listQuestions[8].op4),
    )
    answers9 = forms.CharField(label=listQuestions[8].question, widget=forms.Select(choices = CHOICES_9), required=True)


    CHOICES_10 = (
        (listQuestions[9].op1,listQuestions[9].op1),
        (listQuestions[9].op2,listQuestions[9].op2),
        (listQuestions[9].op3,listQuestions[9].op3),
        (listQuestions[9].op4,listQuestions[9].op4),
    )
    answers10 = forms.CharField(label=listQuestions[9].question, widget=forms.Select(choices = CHOICES_10), required=True)