    # Lists the questions, options and answer
    def __init__(self):
        self.score = 0
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
                "answer": "C"
            },
            {
                "question": "Which programming language is known for its snake logo?",
                "options": ["A. Java", "B. Python", "C. C++", "D. Ruby"],
                "answer": "B"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
                "answer": "B"
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": ["A. H2O", "B. O2", "C. CO2", "D. N2"],
                "answer": "A"
            },
            {
              "question": "Who is the current President of the United States?",
              "options": ["A. Trump", "B. Hilary", "C. Biden", "D. Obama"],
              "answer": "C"
            }
        ]
    # Displays a question, takes user input, and checks if the answer is right
    def ask_question(self, question_data):
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)
        user_answer = input("Your answer: ").upper()
        if user_answer == question_data["answer"]:
            print("Correct!\n")
            return 1
        else:
            print(f"Incorrect! The right answer is {question_data['correct']}.\n")
            return 0
    #   Begins the quiz, loops through the questions, and calculates the score.
    def start_quiz(self):
        print("Welcome to the Quiz App!\n")
        for question in self.questions:
            self.score += self.ask_question(question)

        print(f"Your final score is: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Excellent! You got all the answers correct!")
        elif self.score >= len(self.questions) // 2:
            print("Good job! Keep practicing.")
        else:
            print("Better luck next time!")


def main():
    quiz = QuizApp()
    quiz.start_quiz()


if __name__ == "__main__":
    main()
