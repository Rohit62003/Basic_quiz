
class Question:
    def __init__(self, question, options, correct_answer, descriptions):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.descriptions = descriptions

    def ask_question(self):
        print(f"\nQuestion: {self.question}")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        if user_answer == self.correct_answer:
            print("Correct answer!")
            print(f"Description: {self.descriptions[user_answer-1]}")
            return 1
        else:
            print(f"Incorrect answer. The correct answer is {self.correct_answer}.")
            print(f"Description: {self.descriptions[self.correct_answer-1]}")
            return 0


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, options, correct_answer, descriptions):
        self.questions.append(Question(question, options, correct_answer, descriptions))

    def start_quiz(self):
        for question in self.questions:
            question.ask_question()
            while True:
                try:
                    user_answer = int(input("Enter the number of your answer: "))
                    if 1 <= user_answer <= len(question.options):
                        self.score += question.check_answer(user_answer)
                        break
                    else:
                        print("Invalid answer number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        print(f"\nQuiz finished! Your final score is {self.score} out of {len(self.questions)}")


# Create a quiz and add questions
quiz = Quiz()
quiz.add_question("What is the capital of Bihar", ["Patna", "Delhi", "Kolkata", "jaipur"], 1, ["Patna is the capital city of the Indian state of Bihar,Historically known as Pataliputra.", "The national capital of India", "Kolkata is the capital of West Bengal..", "jaipur is the capital of Rajasthan."])
quiz.add_question("What is the largest planet in our solar system?", ["Earth", "Saturn", "Jupiter", "Uranus"], 3, ["Earth is the third planet from the Sun and the only known planet to support life.", "Saturn is a gas giant planet known for its ring system.", "Jupiter is the largest planet in our solar system, with a diameter of approximately 142,984 kilometers.", "Uranus is an ice giant planet with a tilted axis that causes extreme seasons."])
quiz.add_question("Who Invented Python?", ["Guido van Rossum", "Dennis Ritchie", "Sir Tim Berners-Lee", "James Gosling."], 1, ["Python was invented by Guido van Rossum in the late 1980s.", "C was created in the 1970s by Dennis Ritchie","HTML was created by Sir Tim Berners-Lee in 1991 .","Java was developed by James Gosling."])
# Start the quiz
quiz.start_quiz()
