import csv
import json
import re

# File paths
questions_file = 'RawTestQuestions.csv'
answers_file = 'RawTestAnswers.csv'
output_file = 'Test.json'

# regex to find answers
option_pattern = re.compile(r'^[A-Z]\.')

# Read and store questions with options from RawTestQuestions.csv
questions = {}
current_question_number = None
current_question_text = ""
current_options = []

with open(questions_file, mode='r', encoding='utf-8') as q_file:
    csv_reader = csv.reader(q_file)
    for row in csv_reader:
        if row:
            line = row[0].strip()

            # Check if the line is a question (begins with a number followed by ")")
            if re.match(r'^\d+\)', line):
                # If there's a previous question, save it before moving on
                if current_question_number:
                    questions[current_question_number] = {
                        'question': current_question_text,
                        'options': current_options
                    }

                # Extract question number and text
                current_question_number, current_question_text = line.split(')', 1)
                current_question_number = current_question_number.strip()
                current_question_text = current_question_text.strip()
                current_options = []

            # Check if the line is an option
            elif option_pattern.match(line):
                current_options.append(line.strip())

    # Save the last question
    if current_question_number:
        questions[current_question_number] = {
            'question': current_question_text,
            'options': current_options
        }

# Store answers from RawTestAnswers.csv, If there are multiple answers they should be split with ::
answers = {}
with open(answers_file, mode='r', encoding='utf-8') as a_file:
    csv_reader = csv.reader(a_file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        if row:
            # Split row content into question number and all answers
            question_number, all_answers = row[0].split(' ', 1)
            question_number = question_number.strip()

            # Split multiple answers by "::" and strip any extra whitespace
            individual_answers = [answer.strip() for answer in all_answers.split('::')]

            # Add all answers to the answer dictionary for the question
            answers[question_number] = individual_answers

# Combine questions and answers, write to Test.json
quiz_data = {}
for q_num, q_data in questions.items():
    quiz_data[q_num] = {
        'question': q_data['question'],
        'options': q_data['options'],
        'answers': answers.get(q_num, [])
    }

# Write to Test.json
with open(output_file, mode='w', encoding='utf-8') as json_file:
    json.dump(quiz_data, json_file, indent=4)

print(f"Quiz data successfully written to {output_file}")
