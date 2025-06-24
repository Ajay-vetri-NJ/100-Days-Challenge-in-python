questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) Madrid", "B) Rome", "C) Paris", "D) Berlin"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Which language is primarily used for iOS development?",
        "choices": ["A) Java", "B) Swift", "C) Kotlin", "D) Python"],
        "answer": "B"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    }
]
score = 0
for i, question in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {question['question']}")
    for choice in question["choices"]:
        print(choice)
    answer = input("Enter your answer (A, B, C, or D): ").upper()
    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer was {question['answer']}.")
print(f"\nYou got {score} out of {len(questions)} questions correct.")