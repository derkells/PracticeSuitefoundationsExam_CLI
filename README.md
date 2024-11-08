# PracticeSuitefoundationsExam_CLI
CLI practice test for the SuiteFoundations Exam!  
While I made this for the SuiteFoundations exam, it could be used with any material you are interested in learning.

## Requirements
- **Python Interpreter**: This script requires Python to run. (I use Python 3.12.2).
- **Python Standard Library**: All necessary libraries are included in Python's standard library, so no external packages are required.

---

## Formatting Questions in `RawTestQuestions.csv`
- Each question should start with a number, followed by a close parenthesis, the question text, and a question mark.
- Options should follow below, each beginning with a letter (A, B, C, etc.), followed by a period (`A.`).
  
### Example:
```plaintext
1) What is the primary classification in NetSuite?
A. Departments
B. Classes
C. Subsidiaries
D. Locations

2) Which feature supports multi-location inventory?
A. Locations
B. Inventory
C. Multi-Location Inventory
D. Advanced Inventory Management


## Formatting Questions in `RawTestAnswers.csv`
The `RawTestAnswers.csv` file should contain the correct answers for each question in `RawTestQuestions.csv`, using the following format.

### Format
Each row in `RawTestAnswers.csv` should contain:
1. **Question Number**: The question number, followed by a space.
2. **Answer(s)**: The correct answer(s) for the question. If there are multiple correct answers, separate them with "`::`".

### Example Rows
```plaintext
1 C (Subsidiaries)
2 C (Multi-Location Inventory)
3 A (The navigational path to the record updates with the renaming.)
4 A (Reverse or delete all transactions related to customers and their secondary subsidiaries.) :: C (Remove all secondary subsidiaries from Customer records.)
