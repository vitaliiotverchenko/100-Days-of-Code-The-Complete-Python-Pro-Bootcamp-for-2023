from question_model import Question


class Quiz():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.game_is_on = True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
        print("----------------------------\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.prompt} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def play(self):
        while self.game_is_on:
            if self.question_number < len(self.question_list):
                self.next_question()
            else:
                print("You've completed the quiz!")
                print(
                    f"Your final score was: {self.score}/{self.question_number}")
                self.game_is_on = False
