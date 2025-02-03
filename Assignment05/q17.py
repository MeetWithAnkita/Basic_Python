import random
# Questions and answers
questions = [
    ("What is the capital of France?", "Paris"),
    ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
    ("What is 2+2?", "4"),
    ("What is the largest planet?", "Jupiter"),
    ("Who discovered America?", "Columbus"),
    ("What is the chemical symbol for water?", "H2O"),
    ("What year did World War II end?", "1945"),
    ("What is the smallest prime number?", "2"),
    ("Who painted the Mona Lisa?", "Da Vinci"),
    ("What is the speed of light?", "299792458")
]
random.shuffle(questions)
score = 0

# Ask 4 random questions
for question, answer in questions[:4]:
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        score += 1

print(f"You got {score}/4 correct.")