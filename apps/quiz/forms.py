from .models import QuesModel, QuizCategoryModel
from django import forms

class PQuizForm(forms.Form):
    listQuestions = [ 
        {"question": "Why is it required for all American citizens to obey the law?", 
        "op1":"to ensure citizen\'s life, liberty and property are protected",
        "op2": "to ensure all Americans are treated equally",
        "op3": "to ensure an executive order is approved by Congress",
        "op4": "to ensure enough funds are collected in speeding tickets to fund the police", 
        "ans":"to ensure citizen\'s life, liberty and property are protected"},
        {"question":"Voting in the US is legally a:",
        "op1":"right", 
        "op2":"obligation",
        "op3":"duty", 
        "op4":"burden", 
        "ans":"right"},
        {"question":"When was the last time the draft was enacted in the United States?", 
        "op1":"The Vietnam War",
        "op2":"The Persian Gulf War", 
        "op3":"Korean War", 
        "op4":"World War II", 
        "ans":"The Vietnam War"},
        {"question":"Which of the following is legally permitted?",  
        "op1":"men not registering for the Selective Service at age 18", 
        "op2":"dropping out of high school in Missouri when you are 15 years old", 
        "op3":"not voting", 
        "op4":"tax evasion", 
        "ans":"not voting"},
        {
        "question":"The right to vote best relates to which Constitutional principle?",
        "op1":"judicidal review",
        "op2":"checks and balances",
        "op3":"separation of powers",
        "op4":"popular sovereignty",
        "ans":"popular sovereignty"
        },
        {
        "question":"What does the Constitution do?",
        "op1":"sets up the government",
        "op2":"defines the government",
        "op3":"protects the basic rights of Americans",
        "op4":"all of the above",
        "ans":"all of the above"
        },
        {
        "question":"Which group actually picks the Presidential winner based on the popular vote?",
        "op1":"the governors of each state",
        "op2":"the US senate",
        "op3":"the US house of representatives",
        "op4":"the Electoral College",
        "ans":"the Electoral College"
        },
        {
        "question":"Which of the following is not one of the ways in which the media affects politics?",
        "op1":"by providing information on both parties",
        "op2":"by contributing to election campaign funds",
        "op3":"by focusing public attention on particular issues",
        "op4":"by providing in-depth coverage of national news",
        "ans":"by contributing to election campaign funds"
        },
        {
        "question":"Which best describes the main objective of a lobbyist?",
        "op1":"to raise campaign funds for political parties",
        "op2":"to influence public decision-making for the common good",
        "op3":"to influence state legislators or members of Congress on issues",
        "op4":"to advise political candidates on how to manage their election campaigns",
        "ans":"to influence state legislators or members of Congress on issues"
        },
        {
        "question":"The validity of public opinion polls may be affected by several factors including:",
        "op1":"excessing polling",
        "op2":"poll overrepresentation of political culture factors such as liberty and civic duty",
        "op3":"overrepresentation of the views of the elite",
        "op4":"the wording of the questions of the poll",
        "ans":"the wording of the questions of the poll"
        }]
    
    CHOICES_1 = (
            (listQuestions[0]["op1"],listQuestions[0]["op1"]),
        (listQuestions[0]["op2"],listQuestions[0]["op2"]),
        (listQuestions[0]["op3"],listQuestions[0]["op3"]),
        (listQuestions[0]["op4"],listQuestions[0]["op4"]),
    )
    answers1 = forms.CharField(label=listQuestions[0]["question"], widget=forms.Select(choices = CHOICES_1), required=True)
    
    try:
        CHOICES_2 = (
            (listQuestions[1].op1,listQuestions[1].op1),
            (listQuestions[1].op2,listQuestions[1].op2),
            (listQuestions[1].op3,listQuestions[1].op3),
            (listQuestions[1].op4,listQuestions[1].op4),
        )
        answers2 = forms.CharField(label=listQuestions[1].question,widget=forms.Select(choices = CHOICES_2), required=True)
    except:
        CHOICES_2 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers2 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_2), required=True)

    try:
        CHOICES_3 = (
            (listQuestions[2].op1,listQuestions[2].op1),
            (listQuestions[2].op2,listQuestions[2].op2),
            (listQuestions[2].op3,listQuestions[2].op3),
            (listQuestions[2].op4,listQuestions[2].op4),
        )
        answers3 = forms.CharField(label=listQuestions[2].question, widget=forms.Select(choices = CHOICES_3), required=True)
    except:
        CHOICES_3 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers3 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_3), required=True)
    

    try:
        CHOICES_4 = (
            (listQuestions[3].op1,listQuestions[3].op1),
            (listQuestions[3].op2,listQuestions[3].op2),
            (listQuestions[3].op3,listQuestions[3].op3),
            (listQuestions[3].op4,listQuestions[3].op4),
        )
        answers4 = forms.CharField(label=listQuestions[3].question, widget=forms.Select(choices = CHOICES_4), required=True)
    except:
        CHOICES_4 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers4 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_4), required=True)
    

    try:
        CHOICES_5 = (
            (listQuestions[4].op1,listQuestions[4].op1),
            (listQuestions[4].op2,listQuestions[4].op2),
            (listQuestions[4].op3,listQuestions[4].op3),
            (listQuestions[4].op4,listQuestions[4].op4),
        )
        answers5 = forms.CharField(label=listQuestions[4].question, widget=forms.Select(choices = CHOICES_5), required=True)
    except:
        CHOICES_5 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers5 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_5), required=True)
    

    try:
        CHOICES_6 = (
            (listQuestions[5].op1,listQuestions[5].op1),
            (listQuestions[5].op2,listQuestions[5].op2),
            (listQuestions[5].op3,listQuestions[5].op3),
            (listQuestions[5].op4,listQuestions[5].op4),
        )
        answers6 = forms.CharField(label=listQuestions[5].question, widget=forms.Select(choices = CHOICES_6), required=True)
    except:
        CHOICES_6 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers6 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_6), required=True)

    try:
        CHOICES_7 = (
            (listQuestions[6].op1,listQuestions[6].op1),
            (listQuestions[6].op2,listQuestions[6].op2),
            (listQuestions[6].op3,listQuestions[6].op3),
            (listQuestions[6].op4,listQuestions[6].op4),
        )
        answers7 = forms.CharField(label=listQuestions[6].question, widget=forms.Select(choices = CHOICES_7), required=True)
    except:
        CHOICES_7 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers7 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_7), required=True)

    try:
        CHOICES_8 = (
            (listQuestions[7].op1,listQuestions[7].op1),
            (listQuestions[7].op2,listQuestions[7].op2),
            (listQuestions[7].op3,listQuestions[7].op3),
            (listQuestions[7].op4,listQuestions[7].op4),
        )
        answers8 = forms.CharField(label=listQuestions[7].question, widget=forms.Select(choices = CHOICES_8), required=True)
    except:
        CHOICES_8 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers8 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_8), required=True)

    try:
        CHOICES_9 = (
            (listQuestions[8].op1,listQuestions[8].op1),
            (listQuestions[8].op2,listQuestions[8].op2),
            (listQuestions[8].op3,listQuestions[8].op3),
            (listQuestions[8].op4,listQuestions[8].op4),
        )
        answers9 = forms.CharField(label=listQuestions[8].question, widget=forms.Select(choices = CHOICES_9), required=True)
    except:
        CHOICES_9 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers9 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_9), required=True)

    try:
        CHOICES_10 = (
            (listQuestions[9].op1,listQuestions[9].op1),
            (listQuestions[9].op2,listQuestions[9].op2),
            (listQuestions[9].op3,listQuestions[9].op3),
            (listQuestions[9].op4,listQuestions[9].op4),
        )
        answers10 = forms.CharField(label=listQuestions[9].question, widget=forms.Select(choices = CHOICES_10), required=True)
    except:
        CHOICES_10 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers10 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_10), required=True)
    
    class Meta:
        model = QuesModel
        fields = "__all__"

class SQuizForm(forms.Form):
    try:
        listQuestions = list(QuesModel.objects.filter(category='S'))  
    except:
        listQuestions = []  
    try:
        CHOICES_1 = (
            (listQuestions[0].op1,listQuestions[0].op1),
            (listQuestions[0].op2,listQuestions[0].op2),
            (listQuestions[0].op3,listQuestions[0].op3),
            (listQuestions[0].op4,listQuestions[0].op4),
        )
        answers1 = forms.CharField(label=listQuestions[0].question, widget=forms.Select(choices = CHOICES_1), required=True)
    except:
        CHOICES_1 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers1 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_1), required=True)

    try:
        CHOICES_2 = (
            (listQuestions[1].op1,listQuestions[1].op1),
            (listQuestions[1].op2,listQuestions[1].op2),
            (listQuestions[1].op3,listQuestions[1].op3),
            (listQuestions[1].op4,listQuestions[1].op4),
        )
        answers2 = forms.CharField(label=listQuestions[1].question,widget=forms.Select(choices = CHOICES_2), required=True)
    except:
        CHOICES_2 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers2 = forms.CharField(label="test question",widget=forms.Select(choices = CHOICES_2), required=True)

    try:
        CHOICES_3 = (
            (listQuestions[2].op1,listQuestions[2].op1),
            (listQuestions[2].op2,listQuestions[2].op2),
            (listQuestions[2].op3,listQuestions[2].op3),
            (listQuestions[2].op4,listQuestions[2].op4),
        )
        answers3 = forms.CharField(label=listQuestions[2].question, widget=forms.Select(choices = CHOICES_3), required=True)
    except:
        CHOICES_3 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers3 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_3), required=True)

    try:
        CHOICES_4 = (
            (listQuestions[3].op1,listQuestions[3].op1),
            (listQuestions[3].op2,listQuestions[3].op2),
            (listQuestions[3].op3,listQuestions[3].op3),
            (listQuestions[3].op4,listQuestions[3].op4),
        )
        answers4 = forms.CharField(label=listQuestions[3].question, widget=forms.Select(choices = CHOICES_4), required=True)
    except:
        CHOICES_4 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers4 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_4), required=True)

    try:
        CHOICES_5 = (
            (listQuestions[4].op1,listQuestions[4].op1),
            (listQuestions[4].op2,listQuestions[4].op2),
            (listQuestions[4].op3,listQuestions[4].op3),
            (listQuestions[4].op4,listQuestions[4].op4),
        )
        answers5 = forms.CharField(label=listQuestions[4].question, widget=forms.Select(choices = CHOICES_5), required=True)
    except:
        CHOICES_5 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers5 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_5), required=True)

    try:
        CHOICES_6 = (
            (listQuestions[5].op1,listQuestions[5].op1),
            (listQuestions[5].op2,listQuestions[5].op2),
            (listQuestions[5].op3,listQuestions[5].op3),
            (listQuestions[5].op4,listQuestions[5].op4),
        )
        answers6 = forms.CharField(label=listQuestions[5].question, widget=forms.Select(choices = CHOICES_6), required=True)
    except:
        CHOICES_6 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers6 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_6), required=True)

    try:
        CHOICES_7 = (
            (listQuestions[6].op1,listQuestions[6].op1),
            (listQuestions[6].op2,listQuestions[6].op2),
            (listQuestions[6].op3,listQuestions[6].op3),
            (listQuestions[6].op4,listQuestions[6].op4),
        )
        answers7 = forms.CharField(label=listQuestions[6].question, widget=forms.Select(choices = CHOICES_7), required=True)
    except:
        CHOICES_7 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers7 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_7), required=True)

    try:
        CHOICES_8 = (
            (listQuestions[7].op1,listQuestions[7].op1),
            (listQuestions[7].op2,listQuestions[7].op2),
            (listQuestions[7].op3,listQuestions[7].op3),
            (listQuestions[7].op4,listQuestions[7].op4),
        )
        answers8 = forms.CharField(label=listQuestions[7].question, widget=forms.Select(choices = CHOICES_8), required=True)
    except:
        CHOICES_8 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers8 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_8), required=True)

    try:
        CHOICES_9 = (
            (listQuestions[8].op1,listQuestions[8].op1),
            (listQuestions[8].op2,listQuestions[8].op2),
            (listQuestions[8].op3,listQuestions[8].op3),
            (listQuestions[8].op4,listQuestions[8].op4),
        )
        answers9 = forms.CharField(label=listQuestions[8].question, widget=forms.Select(choices = CHOICES_9), required=True)
    except:
        CHOICES_9 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers9 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_9), required=True)

    try:
        CHOICES_10 = (
            (listQuestions[9].op1,listQuestions[9].op1),
            (listQuestions[9].op2,listQuestions[9].op2),
            (listQuestions[9].op3,listQuestions[9].op3),
            (listQuestions[9].op4,listQuestions[9].op4),
        )
        answers10 = forms.CharField(label=listQuestions[9].question, widget=forms.Select(choices = CHOICES_10), required=True)
    except:
        CHOICES_10 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers10 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_10), required=True)

    class Meta:
        model = QuesModel
        fields = "__all__"

class CQuizForm(forms.Form):
    try:
        listQuestions = list(QuesModel.objects.filter(category='C'))  
    except:
        listQuestions = [] 
    
    
    try:
        CHOICES_1 = (
            (listQuestions[0].op1,listQuestions[0].op1),
            (listQuestions[0].op2,listQuestions[0].op2),
            (listQuestions[0].op3,listQuestions[0].op3),
            (listQuestions[0].op4,listQuestions[0].op4),
        )
        answers1 = forms.CharField(label=listQuestions[0].question, widget=forms.Select(choices = CHOICES_1), required=True)
    except:
        CHOICES_1 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers1 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_1), required=True)

    try:
        CHOICES_2 = (
            (listQuestions[1].op1,listQuestions[1].op1),
            (listQuestions[1].op2,listQuestions[1].op2),
            (listQuestions[1].op3,listQuestions[1].op3),
            (listQuestions[1].op4,listQuestions[1].op4),
        )
        answers2 = forms.CharField(label=listQuestions[1].question,widget=forms.Select(choices = CHOICES_2), required=True)
    except:
        CHOICES_2 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers2 = forms.CharField(label="test question",widget=forms.Select(choices = CHOICES_2), required=True)

    try:
        CHOICES_3 = (
            (listQuestions[2].op1,listQuestions[2].op1),
            (listQuestions[2].op2,listQuestions[2].op2),
            (listQuestions[2].op3,listQuestions[2].op3),
            (listQuestions[2].op4,listQuestions[2].op4),
        )
        answers3 = forms.CharField(label=listQuestions[2].question, widget=forms.Select(choices = CHOICES_3), required=True)
    except:
        CHOICES_3 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers3 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_3), required=True)

    try:
        CHOICES_4 = (
            (listQuestions[3].op1,listQuestions[3].op1),
            (listQuestions[3].op2,listQuestions[3].op2),
            (listQuestions[3].op3,listQuestions[3].op3),
            (listQuestions[3].op4,listQuestions[3].op4),
        )
        answers4 = forms.CharField(label=listQuestions[3].question, widget=forms.Select(choices = CHOICES_4), required=True)
    except:
        CHOICES_4 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers4 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_4), required=True)

    try:
        CHOICES_5 = (
            (listQuestions[4].op1,listQuestions[4].op1),
            (listQuestions[4].op2,listQuestions[4].op2),
            (listQuestions[4].op3,listQuestions[4].op3),
            (listQuestions[4].op4,listQuestions[4].op4),
        )
        answers5 = forms.CharField(label=listQuestions[4].question, widget=forms.Select(choices = CHOICES_5), required=True)
    except:
        CHOICES_5 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers5 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_5), required=True)

    try:
        CHOICES_6 = (
            (listQuestions[5].op1,listQuestions[5].op1),
            (listQuestions[5].op2,listQuestions[5].op2),
            (listQuestions[5].op3,listQuestions[5].op3),
            (listQuestions[5].op4,listQuestions[5].op4),
        )
        answers6 = forms.CharField(label=listQuestions[5].question, widget=forms.Select(choices = CHOICES_6), required=True)
    except:
        CHOICES_6 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers6 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_6), required=True)

    try:
        CHOICES_7 = (
            (listQuestions[6].op1,listQuestions[6].op1),
            (listQuestions[6].op2,listQuestions[6].op2),
            (listQuestions[6].op3,listQuestions[6].op3),
            (listQuestions[6].op4,listQuestions[6].op4),
        )
        answers7 = forms.CharField(label=listQuestions[6].question, widget=forms.Select(choices = CHOICES_7), required=True)
    except:
        CHOICES_7 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers7 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_7), required=True)

    try:
        CHOICES_8 = (
            (listQuestions[7].op1,listQuestions[7].op1),
            (listQuestions[7].op2,listQuestions[7].op2),
            (listQuestions[7].op3,listQuestions[7].op3),
            (listQuestions[7].op4,listQuestions[7].op4),
        )
        answers8 = forms.CharField(label=listQuestions[7].question, widget=forms.Select(choices = CHOICES_8), required=True)
    except:
        CHOICES_8 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers8 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_8), required=True)

    try:
        CHOICES_9 = (
            (listQuestions[8].op1,listQuestions[8].op1),
            (listQuestions[8].op2,listQuestions[8].op2),
            (listQuestions[8].op3,listQuestions[8].op3),
            (listQuestions[8].op4,listQuestions[8].op4),
        )
        answers9 = forms.CharField(label=listQuestions[8].question, widget=forms.Select(choices = CHOICES_9), required=True)
    except:
        CHOICES_9 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers9 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_9), required=True)

    try:
        CHOICES_10 = (
            (listQuestions[9].op1,listQuestions[9].op1),
            (listQuestions[9].op2,listQuestions[9].op2),
            (listQuestions[9].op3,listQuestions[9].op3),
            (listQuestions[9].op4,listQuestions[9].op4),
        )
        answers10 = forms.CharField(label=listQuestions[9].question, widget=forms.Select(choices = CHOICES_10), required=True)
    except:
        CHOICES_10 = (
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        )
        answers10 = forms.CharField(label="test question", widget=forms.Select(choices = CHOICES_10), required=True)

    class Meta:
        model = QuesModel
        fields = "__all__"