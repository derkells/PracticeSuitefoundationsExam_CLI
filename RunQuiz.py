import json
import random
import os


# Load user data
def load_user_data():
    if os.path.exists("User.json"):
        with open("User.json", "r") as f:
            return json.load(f)
    return {"Name": "", "BestScore": "", "MissedQuestions": []}


# Save user data
def save_user_data(user_data):
    with open("User.json", "w") as f:
        json.dump(user_data, f, indent=4)


# get test questions
def load_test_data():
    with open("Test.json", "r") as f:
        return json.load(f)


def get_user_name(user_data):
    if not user_data["Name"]:
        user_data["Name"] = input("Please enter your name: ")
        save_user_data(user_data)
    print(f"Welcome, {user_data['Name']}!")


# Get Question pool
def get_question_pool(test_data, user_data):
    while True:
        choice = input("Do you want to be tested on all questions (A) or only missed questions (M)? ").strip().upper()
        if choice == "A":
            question_pool = list(test_data.keys())
            break
        elif choice == "M":
            question_pool = user_data["MissedQuestions"]
            if not question_pool:
                print("No missed questions to review. Switching to all questions.")
                question_pool = list(test_data.keys())
            break
        else:
            print("Invalid choice. Please enter 'A' for all questions or 'M' for missed questions.")

    shuffle_choice = input("Do you want the questions randomized? (Y/N): ").strip().upper()
    if shuffle_choice == "Y":
        random.shuffle(question_pool)

    return question_pool


# Run the quiz
def run_quiz(test_data, question_pool):
    missed_questions = []
    score = 0

    for question_id in question_pool:
        question_data = test_data[question_id]
        print(f"\nQuestion {question_id}: {question_data['question']}")
        for option in question_data['options']:
            print(option)


        # ignore casing
        user_answer = [ans.upper() for ans in input("Your answer(s) (e.g., 'A C'): ").strip().split()]

        correct_answers = [ans[0] for ans in question_data['answers']]

        if set(user_answer) == set(correct_answers):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            missed_questions.append(question_id)
            print(f"Correct answer(s): {', '.join(correct_answers)}")

    return score, missed_questions


# Main loop
def main():
    user_data = load_user_data()
    test_data = load_test_data()

    get_user_name(user_data)

    while True:
        question_pool = get_question_pool(test_data, user_data)
        score, missed_questions = run_quiz(test_data, question_pool)
        total_questions = len(question_pool)


        print(f"\nYour Score: {score}/{total_questions}")

        if not user_data["BestScore"] or score > int(user_data["BestScore"]):
            user_data["BestScore"] = str(score)
            print("Congratulations! This is your best score!")

        user_data["MissedQuestions"] = missed_questions
        save_user_data(user_data)

        # Once finished with the Quiz
        retry = input("Would you like to take the entire test again? (Y/N): ").strip().upper()
        if retry != "Y":
            review_missed = input("Would you like to retry only missed questions? (Y/N): ").strip().upper()
            if review_missed != "Y":
                clear_missed = input("Would you like to clear your missed questions? (Y/N): ").strip().upper()
                if clear_missed == "Y":
                    user_data["MissedQuestions"] = []
                    save_user_data(user_data)
                break


if __name__ == "__main__":
    main()
