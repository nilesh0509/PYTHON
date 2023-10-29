import random

def load_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 6):
            question = lines[i].strip()
            options = [lines[i + j].strip() for j in range(1, 5)]
            answer = lines[i + 5].strip()
            questions.append({
                "question": question,
                "options": options,
                "answer": answer
            })
    return questions

def generate_upsc_question(questions):
    return random.choice(questions)

def upsc_quiz(questions):
    print("स्वागत है! यहां UPSC परीक्षा से संबंधित MCQ क्विज़ खेलें.")
    score = 0

    while True:
        upsc_question_data = generate_upsc_question(questions)
        question = upsc_question_data["question"]
        options = upsc_question_data["options"]
        answer = upsc_question_data["answer"]

        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_choice = input("तुम्हारा उत्तर क्या है? (1/2/3/4): ").strip()

        try:
            user_choice = int(user_choice)
        except ValueError:
            print("अमान्य उत्तर. कृपया संख्या दर्ज करें.")
            continue

        if 1 <= user_choice <= len(options):
            user_answer = options[user_choice - 1]
            if user_answer == answer:
                print("सही जवाब!")
                score += 1
            else:
                print(f"क्षमा करें, सही उत्तर {answer} है.")
        else:
            print("अमान्य उत्तर. कृपया वैध विकल्प का चयन करें.")

        play_again = input("क्या आप फिर से खेलना चाहते हैं? (हाँ/नहीं): ").lower()
        if play_again != "हाँ":
            break

    print(f"तुम्हारा स्कोर है: {score}. UPSC परीक्षा के लिए खेलने के लिए धन्यवाद!")

if __name__ == "__main__":
    question_file = "upsc_questions.txt"  # Provide the path to your question file
    upsc_questions = load_questions_from_file(question_file)
    upsc_quiz(upsc_questions)
