import requests
import json

class QuizForm():
    q_id = -1
    question = ""
    correct_option = -1
    option1 = ""
    option2 = ""

    def __init__(self, q_id, question, correct_option, option1, option2):
        self.q_id=q_id
        self.question=question
        self.correct_option=correct_option
        self.option1=option1
        self.option2=option2

    def get_correct_option(self):
        if self.correct_option == 1:
            return option1
        else:
            return option2 


req = requests.get('https://opentdb.com/api.php?amount=10&category=11&type=boolean')
data = json.loads(req.content)
q1 = QuizForm(1, data["results"][0]["question"].replace("&#039;", "\'").replace("&quot;","\""), 1, data["results"][0]["correct_answer"] , data["results"][0]["incorrect_answers"][0])

print(q1.question)
print(q1.correct_option)
print(q1.option1)
print(q1.option2)