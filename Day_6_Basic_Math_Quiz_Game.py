import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer

def math_quiz():
    score = 0
    print("\n=== Welcome to the Math Quiz Game! ---")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    for i in range(5):
        question, answer = generate_question()
        print(f"Question {i+1}: {question}")
        user_answer = input("Your answer: ")
        if user_answer == str(answer):
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
    print("\n--- Game Over! ---")
    print(f"Your final score is: {score}/5")
math_quiz()