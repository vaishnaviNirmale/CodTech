import random

# Define questions and answers
questions = {
    "Science": {
        "What is the chemical symbol for water?": {"options": ["H2O", "CO2", "O2", "N2"], "correct": "H2O"},
        "Who developed the theory of relativity?": {"options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"], "correct": "Albert Einstein"},
        "What is the largest planet in our solar system?": {"options": ["Jupiter", "Saturn", "Neptune", "Earth"], "correct": "Jupiter"}
    },
    "History": {
        "In which year did World War II end?": {"options": ["1945", "1939", "1950", "1942"], "correct": "1945"},
        "Who was the first President of the United States?": {"options": ["George Washington", "Thomas Jefferson", "John Adams", "Abraham Lincoln"], "correct": "George Washington"},
        "What ancient civilization built the pyramids of Giza?": {"options": ["Egyptians", "Romans", "Greeks", "Mayans"], "correct": "Egyptians"}
    },
    "General Knowledge": {
        "What is the capital of France?": {"options": ["Paris", "Berlin", "Madrid", "Rome"], "correct": "Paris"},
        "Which planet is known as the Red Planet?": {"options": ["Mars", "Venus", "Jupiter", "Saturn"], "correct": "Mars"},
        "What is the currency of Japan?": {"options": ["Yen", "Won", "Ringgit", "Baht"], "correct": "Yen"}
    },
    "Maths": {
        "What is the value of π (pi) to two decimal places?": {"options": ["3.14", "2.71", "1.62", "4.20"],
                                                               "correct": "3.14"},
        "Solve the equation: 2x + 5 = 15": {"options": ["5", "7", "10", "6"], "correct": "5"},
        "What is the square root of 64?": {"options": ["8", "6", "10", "12"], "correct": "8"},
        "What is the sum of angles in a triangle?": {"options": ["90 degrees", "180 degrees", "270 degrees", "360 degrees"], "correct": "180 degrees"},
        "If a rectangle has a length of 8 units and a width of 5 units, what is its perimeter?": {"options": ["13 units", "18 units", "26 units", "16 units"], "correct": "26 units"}

    }
}

def run_quiz():
    total_score = 0
    category_scores = {}

    categories = list(questions.keys())
    random.shuffle(categories)  # Shuffle the order of categories

    for category in categories:
        category_questions = questions[category]
        category_score = 0
        print(f"\n{category} Questions:")
        print("---------------------")

        question_keys = list(category_questions.keys())
        random.shuffle(question_keys)  # Shuffle the order of questions within the category

        for question_key in question_keys:
            data = category_questions[question_key]
            options = data["options"]
            correct_answer = data["correct"]

            random.shuffle(options)  # Shuffle options to make it more challenging

            print(question_key)

            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")

            user_answer = input("Your answer (enter the option number): ")

            if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
                if options[int(user_answer) - 1] == correct_answer:
                    print("Correct!\n")
                    total_score += 1
                    category_score += 1
                else:
                    print(f"Wrong! The correct answer is: {correct_answer}\n")
            else:
                print("Invalid input. Skipped the question.\n")

        category_scores[category] = category_score

    print("\nQuiz completed! Your scores:")
    for category, score in category_scores.items():
        print(f"{category}: {score}/{len(questions[category])}")

    print(f"\nTotal Score: {total_score}/{sum(len(q) for q in questions.values())}")

if __name__ == "__main__":
    run_quiz()
