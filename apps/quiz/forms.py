from .models import QuizCategoryModel
from django import forms

#this is the quiz form for the political quiz with the political questions
class PQuizForm(forms.Form):

    #list of 10 questions with the question, each option, and the answer
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
        {"question":"The right to vote best relates to which Constitutional principle?",
        "op1":"judicidal review",
        "op2":"checks and balances",
        "op3":"separation of powers",
        "op4":"popular sovereignty",
        "ans":"popular sovereignty"},
        {"question":"What does the Constitution do?",
        "op1":"sets up the government",
        "op2":"defines the government",
        "op3":"protects the basic rights of Americans",
        "op4":"all of the above",
        "ans":"all of the above"},
        {"question":"Which group actually picks the Presidential winner based on the popular vote?",
        "op1":"the governors of each state",
        "op2":"the US senate",
        "op3":"the US house of representatives",
        "op4":"the Electoral College",
        "ans":"the Electoral College"},
        {"question":"Which of the following is not one of the ways in which the media affects politics?",
        "op1":"by providing information on both parties",
        "op2":"by contributing to election campaign funds",
        "op3":"by focusing public attention on particular issues",
        "op4":"by providing in-depth coverage of national news",
        "ans":"by contributing to election campaign funds"},
        {"question":"Which best describes the main objective of a lobbyist?",
        "op1":"to raise campaign funds for political parties",
        "op2":"to influence public decision-making for the common good",
        "op3":"to influence state legislators or members of Congress on issues",
        "op4":"to advise political candidates on how to manage their election campaigns",
        "ans":"to influence state legislators or members of Congress on issues"},
        {"question":"The validity of public opinion polls may be affected by several factors including:",
        "op1":"excessing polling",
        "op2":"poll overrepresentation of political culture factors such as liberty and civic duty",
        "op3":"overrepresentation of the views of the elite",
        "op4":"the wording of the questions of the poll",
        "ans":"the wording of the questions of the poll"}]
    
    #pull each option from the list of questions (op1, op2, op3, op4)
    CHOICES_1 = (
        (listQuestions[0]["op1"],listQuestions[0]["op1"]),
        (listQuestions[0]["op2"],listQuestions[0]["op2"]),
        (listQuestions[0]["op3"],listQuestions[0]["op3"]),
        (listQuestions[0]["op4"],listQuestions[0]["op4"]),
    )

    #the answer is chosen from the dropdown form widget with each label being the corresponding question
    answers1 = forms.CharField(label=listQuestions[0]["question"], widget=forms.Select(choices = CHOICES_1), required=True)
    
    #repeat the same for the rest of the questions in the list
    CHOICES_2 = (
        (listQuestions[1]["op1"],listQuestions[1]["op1"]),
        (listQuestions[1]["op2"],listQuestions[1]["op2"]),
        (listQuestions[1]["op3"],listQuestions[1]["op3"]),
        (listQuestions[1]["op4"],listQuestions[1]["op4"]),
    )
    answers2 = forms.CharField(label=listQuestions[1]["question"],widget=forms.Select(choices = CHOICES_2), required=True)

    CHOICES_3 = (
        (listQuestions[2]["op1"],listQuestions[2]["op1"]),
        (listQuestions[2]["op2"],listQuestions[2]["op2"]),
        (listQuestions[2]["op3"],listQuestions[2]["op3"]),
        (listQuestions[2]["op4"],listQuestions[2]["op4"]),
    )
    answers3 = forms.CharField(label=listQuestions[2]["question"], widget=forms.Select(choices = CHOICES_3), required=True)

    CHOICES_4 = (
        (listQuestions[3]["op1"],listQuestions[3]["op1"]),
        (listQuestions[3]["op2"],listQuestions[3]["op2"]),
        (listQuestions[3]["op3"],listQuestions[3]["op3"]),
        (listQuestions[3]["op4"],listQuestions[3]["op4"]),
    )
    answers4 = forms.CharField(label=listQuestions[3]["question"], widget=forms.Select(choices = CHOICES_4), required=True)

    CHOICES_5 = (
        (listQuestions[4]["op1"],listQuestions[4]["op1"]),
        (listQuestions[4]["op2"],listQuestions[4]["op2"]),
        (listQuestions[4]["op3"],listQuestions[4]["op3"]),
        (listQuestions[4]["op4"],listQuestions[4]["op4"]),
    )
    answers5 = forms.CharField(label=listQuestions[4]["question"], widget=forms.Select(choices = CHOICES_5), required=True)   

    CHOICES_6 = (
        (listQuestions[5]["op1"],listQuestions[5]["op1"]),
        (listQuestions[5]["op2"],listQuestions[5]["op2"]),
        (listQuestions[5]["op3"],listQuestions[5]["op3"]),
        (listQuestions[5]["op4"],listQuestions[5]["op4"]),
    )
    answers6 = forms.CharField(label=listQuestions[5]["question"], widget=forms.Select(choices = CHOICES_6), required=True)

    CHOICES_7 = (
        (listQuestions[6]["op1"],listQuestions[6]["op1"]),
        (listQuestions[6]["op2"],listQuestions[6]["op2"]),
        (listQuestions[6]["op3"],listQuestions[6]["op3"]),
        (listQuestions[6]["op4"],listQuestions[6]["op4"]),
    )
    answers7 = forms.CharField(label=listQuestions[6]["question"], widget=forms.Select(choices = CHOICES_7), required=True)

    CHOICES_8 = (
        (listQuestions[7]["op1"],listQuestions[7]["op1"]),
        (listQuestions[7]["op2"],listQuestions[7]["op2"]),
        (listQuestions[7]["op3"],listQuestions[7]["op3"]),
        (listQuestions[7]["op4"],listQuestions[7]["op4"]),
    )
    answers8 = forms.CharField(label=listQuestions[7]["question"], widget=forms.Select(choices = CHOICES_8), required=True)

    CHOICES_9 = (
        (listQuestions[8]["op1"],listQuestions[8]["op1"]),
        (listQuestions[8]["op2"],listQuestions[8]["op2"]),
        (listQuestions[8]["op3"],listQuestions[8]["op3"]),
        (listQuestions[8]["op4"],listQuestions[8]["op4"]),
    )
    answers9 = forms.CharField(label=listQuestions[8]["question"], widget=forms.Select(choices = CHOICES_9), required=True)

    CHOICES_10 = (
        (listQuestions[9]["op1"],listQuestions[9]["op1"]),
        (listQuestions[9]["op2"],listQuestions[9]["op2"]),
        (listQuestions[9]["op3"],listQuestions[9]["op3"]),
        (listQuestions[9]["op4"],listQuestions[9]["op4"]),
    )
    answers10 = forms.CharField(label=listQuestions[9]["question"], widget=forms.Select(choices = CHOICES_10), required=True)

#the social quiz form is in the same format as the political quiz form but with different questions, options, and answers
class SQuizForm(forms.Form):
    listQuestions = [ 
        {"question": "Which of the following is the best example of civic responsibility?", 
        "op1":"attending school",
        "op2":"jury duty",
        "op3":"going to work",
        "op4":"donating blood", 
        "ans":"donating blood"},
        {"question":"All of the following are civic responsibilities except:",
        "op1":"holding elected office", 
        "op2":"registering to vote",
        "op3":"respecting other people\'s opinions", 
        "op4":"paying taxes", 
        "ans":"paying taxes"},
        {"question":"Schools teach civic responsibility to students with the goal to:", 
        "op1":"produce responsible citizens and active participants in community and government",
        "op2":"ensure everyone will run for an elected office", 
        "op3":"ensure everyone pays their taxes on time", 
        "op4":"produce citizens who will serve in the military", 
        "ans":"produce responsible citizens and active participants in community and government"},
        {"question":"Which is an example of a required civic responsibility?",  
        "op1":"serving in the military", 
        "op2":"communicating with government officials", 
        "op3":"going to college", 
        "op4":"attending school until your state\'s compulsory attendance age is reached", 
        "ans":"attending school until your state\'s compulsory attendance age is reached"},
        {"question":"Which of the following is an example of civic responsibility",
        "op1":"registering to vote",
        "op2":"going to work",
        "op3":"paying taxes",
        "op4":"attending school",
        "ans":"registering to vote"},
        {"question":"What is a civic duty that children perform every day?",
        "op1":"listen to and obey their parents",
        "op2":"go to school",
        "op3":"sit on juries",
        "op4":"volunteer in their community",
        "ans":"go to school"},
        {"question":"What is one example of personal responsibility?",
        "op1":"exercising and eating healthy",
        "op2":"voting",
        "op3":"the US house of representatives",
        "op4":"running for political office",
        "ans":"exercising and eating healthy"},
        {"question":"What is citizenship?",
        "op1":"something that is given automatically when a person moves to a different country",
        "op2":"being a member of a nation or country and having full rights and responsibilities under the law",
        "op3":"that other grade on your report card that nobody really looks at",
        "op4":"a large boat that only carries passengers that are members of a certain country",
        "ans":"being a member of a nation or country and having full rights and responsibilities under the law"},
        {"question":"What is the difference between a civic duty and a civic responsibility?",
        "op1":"civic duties are optional but responsibilities are required",
        "op2":"there is no difference and the words are used interchangeably",
        "op3":"civic duties are required but civic responsibilities are optional",
        "op4":"none of the answers are correct",
        "ans":"civic duties are required but civic responsibilities are optional"},
        {"question":"Why is jury duty a civic duty?",
        "op1":"it provides the best opportunity for a fair trial of your peers",
        "op2":"it ensures that 12 people serve on every jury",
        "op3":"it ensures we have a pool of citizens to pick from",
        "op4":"it guarantees a correct verdict every time",
        "ans":"it provides the best opportunity for a fair trial of your peers"}]

    CHOICES_1 = (
        (listQuestions[0]["op1"],listQuestions[0]["op1"]),
        (listQuestions[0]["op2"],listQuestions[0]["op2"]),
        (listQuestions[0]["op3"],listQuestions[0]["op3"]),
        (listQuestions[0]["op4"],listQuestions[0]["op4"]),
    )
    answers1 = forms.CharField(label=listQuestions[0]["question"], widget=forms.Select(choices = CHOICES_1), required=True)

    CHOICES_2 = (
        (listQuestions[1]["op1"],listQuestions[1]["op1"]),
        (listQuestions[1]["op2"],listQuestions[1]["op2"]),
        (listQuestions[1]["op3"],listQuestions[1]["op3"]),
        (listQuestions[1]["op4"],listQuestions[1]["op4"]),
    )
    answers2 = forms.CharField(label=listQuestions[1]["question"],widget=forms.Select(choices = CHOICES_2), required=True)

    CHOICES_3 = (
        (listQuestions[2]["op1"],listQuestions[2]["op1"]),
        (listQuestions[2]["op2"],listQuestions[2]["op2"]),
        (listQuestions[2]["op3"],listQuestions[2]["op3"]),
        (listQuestions[2]["op4"],listQuestions[2]["op4"]),
    )
    answers3 = forms.CharField(label=listQuestions[2]["question"], widget=forms.Select(choices = CHOICES_3), required=True)

    CHOICES_4 = (
        (listQuestions[3]["op1"],listQuestions[3]["op1"]),
        (listQuestions[3]["op2"],listQuestions[3]["op2"]),
        (listQuestions[3]["op3"],listQuestions[3]["op3"]),
        (listQuestions[3]["op4"],listQuestions[3]["op4"]),
    )
    answers4 = forms.CharField(label=listQuestions[3]["question"], widget=forms.Select(choices = CHOICES_4), required=True)

    CHOICES_5 = (
        (listQuestions[4]["op1"],listQuestions[4]["op1"]),
        (listQuestions[4]["op2"],listQuestions[4]["op2"]),
        (listQuestions[4]["op3"],listQuestions[4]["op3"]),
        (listQuestions[4]["op4"],listQuestions[4]["op4"]),
    )
    answers5 = forms.CharField(label=listQuestions[4]["question"], widget=forms.Select(choices = CHOICES_5), required=True)

    CHOICES_6 = (
        (listQuestions[5]["op1"],listQuestions[5]["op1"]),
        (listQuestions[5]["op2"],listQuestions[5]["op2"]),
        (listQuestions[5]["op3"],listQuestions[5]["op3"]),
        (listQuestions[5]["op4"],listQuestions[5]["op4"]),
    )
    answers6 = forms.CharField(label=listQuestions[5]["question"], widget=forms.Select(choices = CHOICES_6), required=True)

    CHOICES_7 = (
        (listQuestions[6]["op1"],listQuestions[6]["op1"]),
        (listQuestions[6]["op2"],listQuestions[6]["op2"]),
        (listQuestions[6]["op3"],listQuestions[6]["op3"]),
        (listQuestions[6]["op4"],listQuestions[6]["op4"]),
    )
    answers7 = forms.CharField(label=listQuestions[6]["question"], widget=forms.Select(choices = CHOICES_7), required=True)

    CHOICES_8 = (
        (listQuestions[7]["op1"],listQuestions[7]["op1"]),
        (listQuestions[7]["op2"],listQuestions[7]["op2"]),
        (listQuestions[7]["op3"],listQuestions[7]["op3"]),
        (listQuestions[7]["op4"],listQuestions[7]["op4"]),
    )
    answers8 = forms.CharField(label=listQuestions[7]["question"], widget=forms.Select(choices = CHOICES_8), required=True)

    CHOICES_9 = (
        (listQuestions[8]["op1"],listQuestions[8]["op1"]),
        (listQuestions[8]["op2"],listQuestions[8]["op2"]),
        (listQuestions[8]["op3"],listQuestions[8]["op3"]),
        (listQuestions[8]["op4"],listQuestions[8]["op4"]),
    )
    answers9 = forms.CharField(label=listQuestions[8]["question"], widget=forms.Select(choices = CHOICES_9), required=True)

    CHOICES_10 = (
        (listQuestions[9]["op1"],listQuestions[9]["op1"]),
        (listQuestions[9]["op2"],listQuestions[9]["op2"]),
        (listQuestions[9]["op3"],listQuestions[9]["op3"]),
        (listQuestions[9]["op4"],listQuestions[9]["op4"]),
    )
    answers10 = forms.CharField(label=listQuestions[9]["question"], widget=forms.Select(choices = CHOICES_10), required=True)

#the social quiz form is in the same format as the political quiz form but with different questions, options, and answers
class CQuizForm(forms.Form):
    listQuestions = [ 
        {"question":"What is community service?", 
        "op1":"getting paid to do a job",
        "op2":"volunteering to do something for your family",
        "op3":"volunteering to do free work to benefit your community",
        "op4":"getting compensated to do work", 
        "ans":"volunteering to do free work to benefit your community"},
        {"question":"Examples of volunteer work would be:", 
        "op1":"serving in a community diner for the poor/in need",
        "op2":"picking up trash along the highway",
        "op3":"organizing a clothing drive for the less fortunate",
        "op4":"all of the above", 
        "ans":"all of the above"},
        {"question":"What could Maria do if she wanted to serve her community?", 
        "op1":"buy a ticket for the fair in her town",
        "op2":"read a book on the history of her community",
        "op3":"volunteer to work with a group that cleans the city park",
        "op4":"sell lemonade in her neighborhood", 
        "ans":"volunteer to work with a group that cleans the city park"},
        {"question":"Benefits of volunteering can be:", 
        "op1":"better community",
        "op2":"better self-worth",
        "op3":"learning new skills",
        "op4":"all of the above", 
        "ans":"all of the above"},
        {"question":"How do citizens contribute to the improvement of a community?", 
        "op1":"by volunteerism and civic responsibility",
        "op2":"by virtue and law",
        "op3":"by following volunteerism laws",
        "op4":"by spending time at the public library", 
        "ans":"by volunteerism and civic responsibility"},
        {"question":"Which term is defined as a theory or system of moral values dealing with what is good and bad with moral duty and obligation?", 
        "op1":"ethics",
        "op2":"service learning",
        "op3":"integrity",
        "op4":"productivity", 
        "ans":"ethics"},
        {"question":"What do we call it when someone works to help others by giving their time and talents without receiving pay?", 
        "op1":"performing a public requirement",
        "op2":"voting",
        "op3":"volunteering",
        "op4":"acting on behalf of the constitution", 
        "ans":"volunteering"},
        {"question":"Which of the following involves designing laws, rules, protocols, and procedures to guide or influence behavior?", 
        "op1":"social change",
        "op2":"economic change",
        "op3":"policy change",
        "op4":"regulation change", 
        "ans":"policy change"},
        {"question":"What is the purpose of community involvement?", 
        "op1":"to increase your awareness of community needs",
        "op2":"to identify with your community",
        "op3":"to learn to make a difference in your community",
        "op4":"all of the above", 
        "ans":"all of the above"},
        {"question":"Which of the following do not describe community service correctly?", 
        "op1":"often done near the area where you live so your own community reaps the benefits of your work",
        "op2":"you do not get paid to perform community service",
        "op3":"something done that does not benefit anyone",
        "op4":"work done by a person or group of people that benefits others", 
        "ans":"something done that does not benefit anyone"}]

    CHOICES_1 = (
        (listQuestions[0]["op1"],listQuestions[0]["op1"]),
        (listQuestions[0]["op2"],listQuestions[0]["op2"]),
        (listQuestions[0]["op3"],listQuestions[0]["op3"]),
        (listQuestions[0]["op4"],listQuestions[0]["op4"]),
    )
    answers1 = forms.CharField(label=listQuestions[0]["question"], widget=forms.Select(choices = CHOICES_1), required=True)

    CHOICES_2 = (
        (listQuestions[1]["op1"],listQuestions[1]["op1"]),
        (listQuestions[1]["op2"],listQuestions[1]["op2"]),
        (listQuestions[1]["op3"],listQuestions[1]["op3"]),
        (listQuestions[1]["op4"],listQuestions[1]["op4"]),
    )
    answers2 = forms.CharField(label=listQuestions[1]["question"],widget=forms.Select(choices = CHOICES_2), required=True)

    CHOICES_3 = (
        (listQuestions[2]["op1"],listQuestions[2]["op1"]),
        (listQuestions[2]["op2"],listQuestions[2]["op2"]),
        (listQuestions[2]["op3"],listQuestions[2]["op3"]),
        (listQuestions[2]["op4"],listQuestions[2]["op4"]),
    )
    answers3 = forms.CharField(label=listQuestions[2]["question"], widget=forms.Select(choices = CHOICES_3), required=True)

    CHOICES_4 = (
        (listQuestions[3]["op1"],listQuestions[3]["op1"]),
        (listQuestions[3]["op2"],listQuestions[3]["op2"]),
        (listQuestions[3]["op3"],listQuestions[3]["op3"]),
        (listQuestions[3]["op4"],listQuestions[3]["op4"]),
    )
    answers4 = forms.CharField(label=listQuestions[3]["question"], widget=forms.Select(choices = CHOICES_4), required=True)

    CHOICES_5 = (
        (listQuestions[4]["op1"],listQuestions[4]["op1"]),
        (listQuestions[4]["op2"],listQuestions[4]["op2"]),
        (listQuestions[4]["op3"],listQuestions[4]["op3"]),
        (listQuestions[4]["op4"],listQuestions[4]["op4"]),
    )
    answers5 = forms.CharField(label=listQuestions[4]["question"], widget=forms.Select(choices = CHOICES_5), required=True)

    CHOICES_6 = (
        (listQuestions[5]["op1"],listQuestions[5]["op1"]),
        (listQuestions[5]["op2"],listQuestions[5]["op2"]),
        (listQuestions[5]["op3"],listQuestions[5]["op3"]),
        (listQuestions[5]["op4"],listQuestions[5]["op4"]),
    )
    answers6 = forms.CharField(label=listQuestions[5]["question"], widget=forms.Select(choices = CHOICES_6), required=True)

    CHOICES_7 = (
        (listQuestions[6]["op1"],listQuestions[6]["op1"]),
        (listQuestions[6]["op2"],listQuestions[6]["op2"]),
        (listQuestions[6]["op3"],listQuestions[6]["op3"]),
        (listQuestions[6]["op4"],listQuestions[6]["op4"]),
    )
    answers7 = forms.CharField(label=listQuestions[6]["question"], widget=forms.Select(choices = CHOICES_7), required=True)

    CHOICES_8 = (
        (listQuestions[7]["op1"],listQuestions[7]["op1"]),
        (listQuestions[7]["op2"],listQuestions[7]["op2"]),
        (listQuestions[7]["op3"],listQuestions[7]["op3"]),
        (listQuestions[7]["op4"],listQuestions[7]["op4"]),
    )
    answers8 = forms.CharField(label=listQuestions[7]["question"], widget=forms.Select(choices = CHOICES_8), required=True)

    CHOICES_9 = (
        (listQuestions[8]["op1"],listQuestions[8]["op1"]),
        (listQuestions[8]["op2"],listQuestions[8]["op2"]),
        (listQuestions[8]["op3"],listQuestions[8]["op3"]),
        (listQuestions[8]["op4"],listQuestions[8]["op4"]),
    )
    answers9 = forms.CharField(label=listQuestions[8]["question"], widget=forms.Select(choices = CHOICES_9), required=True)

    CHOICES_10 = (
        (listQuestions[9]["op1"],listQuestions[9]["op1"]),
        (listQuestions[9]["op2"],listQuestions[9]["op2"]),
        (listQuestions[9]["op3"],listQuestions[9]["op3"]),
        (listQuestions[9]["op4"],listQuestions[9]["op4"]),
    )
    answers10 = forms.CharField(label=listQuestions[9]["question"], widget=forms.Select(choices = CHOICES_10), required=True)