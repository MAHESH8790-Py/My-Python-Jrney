quiz = {
    "What is the capital of India? ": "Delhi",
    "Who developed Python? ": "Guido van Rossum",
    "2 + 2 = ? ": "4",
    "What is the keyword to create a function? ": "def"
}

score = 0

for question, answer in quiz.items():
    print("\n" + question)
    user_answer = input("Your answer: ")

    if user_answer.lower() == answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct Answer:", answer)

print("\n===== Quiz Finished =====")
print("Your Score:", score, "/", len(quiz))