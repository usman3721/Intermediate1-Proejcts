from data import question_data

class Question:
    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer=q_answer

  
class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.question_list=q_list
    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            
            print("You have completed the quiz")
            print(f"Your final score is{quiz.score}/{quiz.question_number}")
            return False

      

            
       
    def next_question(self):
        
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q. {self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("You got it right")
        else:
            print("it is wrong")
        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    # def qurstion_complete(self):
    #     if self.question_number==len(self.question_list):
    #         print("You have completed the quiz")
    #         print(f"Your final score is{quiz.score}/{quiz.question_number}")
    #     else:
    #         self.next_question()
            
   


question_bank=[]
for items in question_data:
    question_text=items["text"]
    question_answer=items["answer"]
    new_quetsion=Question(q_answer=question_answer,q_text=question_text)
    question_bank.append(new_quetsion)

        

quiz=QuizBrain(question_bank)
while quiz.still_has_question:
    quiz.next_question()






