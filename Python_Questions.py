from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QIcon

class PythonMain(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('JavaScript Questions')
        self.setWindowIcon(QIcon('python.png'))
        self.setFixedSize(420, 500)
        self.current_index = 0

        # Step 2: Define flashcards (can come before or after current_index)
        self.flashcards = [
            {"question": "What keyword is used to define a function in Python?", "answer": "def"},
            {"question": "How do you start a comment in Python?", "answer": "#"},
            {"question": "What data type is used to store text?", "answer": "str"},
            {"question": "Which keyword is used to create a loop that runs while a condition is true?",
             "answer": "while"},
            {"question": "How do you import a module named 'math'?", "answer": "import math"},
            {"question": "What symbol is used for exponentiation (power) in Python?", "answer": "**"},
            {"question": "What function is used to print output to the console?", "answer": "print"},
            {"question": "How do you create a list in Python?", "answer": "Using square brackets []"},
            {"question": "What keyword is used to handle exceptions?", "answer": "try"},
            {"question": "Which method adds an item to the end of a list?", "answer": "append"},
            {"question": "What keyword is used to define a function in Python?", "answer": "def"},
            {"question": "How do you start a comment in Python?", "answer": "#"},
            {"question": "What data type is used to store text?", "answer": "str"},
            {"question": "Which keyword is used to create a loop that runs while a condition is true?",
             "answer": "while"},
            {"question": "How do you import a module named 'math'?", "answer": "import math"},
            {"question": "What symbol is used for exponentiation (power) in Python?", "answer": "**"},
            {"question": "What function is used to print output to the console?", "answer": "print"},
            {"question": "How do you create a list in Python?", "answer": "Using square brackets []"},
            {"question": "What keyword is used to handle exceptions?", "answer": "try"},
            {"question": "Which method adds an item to the end of a list?", "answer": "append"},
            {"question": "How do you define a class in Python?", "answer": "Using the 'class' keyword"},
            {"question": "What does 'len()' function return?", "answer": "The length of a sequence"},
            {"question": "How do you convert a string to an integer?", "answer": "int()"},
            {"question": "Which operator is used for floor division?", "answer": "//"},
            {"question": "What is a Python dictionary?", "answer": "A collection of key-value pairs"},
            {"question": "How do you check equality between two variables?", "answer": "Using '==' operator"},
            {"question": "What symbol is used for single-line comments?", "answer": "#"},
            {"question": "How do you write a multi-line string?", "answer": "Using triple quotes ''' or \"\"\""},
            {"question": "Which keyword is used to create a conditional statement?", "answer": "if"},
            {"question": "What is the difference between a list and a tuple?",
             "answer": "Lists are mutable; tuples are immutable"},
            {"question": "What does the 'range()' function do?", "answer": "Generates a sequence of numbers"},
            {"question": "How do you open a file for reading?", "answer": "open('filename', 'r')"},
            {"question": "What is a lambda function?", "answer": "An anonymous inline function"},
            {"question": "Which method removes the last item from a list?", "answer": "pop()"},
            {"question": "How do you create an empty set?", "answer": "Using set()"},
            {"question": "What is the output of 'bool(0)'?", "answer": "False"},
            {"question": "How do you check the type of a variable?", "answer": "Using type()"},
            {"question": "What is list comprehension?", "answer": "A concise way to create lists"},
            {"question": "How do you import only the 'sqrt' function from math module?",
             "answer": "from math import sqrt"},
            {"question": "What is the purpose of 'pass' statement?", "answer": "It’s a placeholder that does nothing"},
            {"question": "How do you raise an exception?", "answer": "Using 'raise' keyword"},
            {"question": "What does 'is' operator check?", "answer": "Whether two variables point to the same object"},
            {"question": "How do you concatenate strings?", "answer": "Using the '+' operator"},
            {"question": "Which method converts a string to uppercase?", "answer": "upper()"},
            {"question": "How do you create a virtual environment in Python?",
             "answer": "Using 'python -m venv env_name'"},
            {"question": "What is the default encoding for Python source files?", "answer": "UTF-8"},
            {"question": "Which method returns a list of all keys in a dictionary?", "answer": "keys()"},
            {"question": "What is the difference between '==' and 'is'?",
             "answer": "'==' checks value equality; 'is' checks identity"},
            {"question": "How do you install external packages in Python?", "answer": "Using pip"},
            {"question": "What does 'None' represent?", "answer": "The absence of a value"},
            {"question": "What does the 'with' statement do when working with files?",
             "answer": "Automatically handles opening and closing files"},
            {"question": "How do you reverse a list?", "answer": "Using reverse() method or [::-1] slice"},
            {"question": "What is a generator?", "answer": "A function that yields values lazily"},
            {"question": "How do you handle multiple exceptions?", "answer": "Using multiple except blocks or a tuple"},
            {"question": "What is duck typing in Python?",
             "answer": "Type compatibility based on methods/behavior, not inheritance"},
            {"question": "How do you check if a key exists in a dictionary?", "answer": "Using 'in' keyword"},
            {"question": "What does the 'global' keyword do?",
             "answer": "Allows modifying a global variable inside a function"},
            {"question": "How do you create a list of numbers from 0 to 9?", "answer": "list(range(10))"},
            {"question": "What is the use of 'yield' keyword?",
             "answer": "To produce a generator and yield values one at a time"},
            {"question": "How do you sort a list in-place?", "answer": "Using sort() method"},
            {"question": "What is the difference between 'del' and 'remove' for lists?",
             "answer": "'del' removes by index; 'remove' removes by value"}
        ]

        # Widgets
        self.question_label = QLabel(self.flashcards[self.current_index]["question"])
        self.question_label.setFont(QFont('Arial', 16, QFont.Bold))
        self.question_label.setWordWrap(True)
        self.question_label.setAlignment(Qt.AlignCenter)

        self.answer_input = QLineEdit()
        self.answer_input.setFont(QFont('Arial', 14))
        self.answer_input.setFixedSize(320, 40)
        self.answer_input.setPlaceholderText("Type your answer here...")

        self.check_button = QPushButton("Check Answer")
        self.check_button.setFont(QFont('Arial', 14))
        self.check_button.setFixedSize(220, 45)
        self.check_button.setStyleSheet("""
                        QPushButton {
                            background-color: #3498db;
                            color: white;
                            border-radius: 10px;
                            transition: background-color 0.3s;
                        }
                        QPushButton:hover {
                            background-color: #2980b9;
                        }
                        QPushButton:disabled {
                            background-color: #95a5a6;
                        }
                    """)

        self.feedback_label = QLabel("")
        self.feedback_label.setFont(QFont('Arial', 14))
        self.feedback_label.setAlignment(Qt.AlignCenter)

        self.exit_button = QPushButton("← Back")
        self.exit_button.setFont(QFont('Arial', 13))
        self.exit_button.setFixedSize(110, 40)
        self.exit_button.setStyleSheet("""
                        QPushButton {
                            background-color: #e74c3c;
                            color: white;
                            border-radius: 10px;
                            transition: background-color 0.3s;
                        }
                        QPushButton:hover {
                            background-color: #c0392b;
                        }
                    """)

        # Layout setup
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 100)
        layout.setSpacing(25)

        layout.addWidget(self.question_label)
        layout.addWidget(self.answer_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.check_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.feedback_label)
        layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self.exit_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

        # Connections
        self.check_button.clicked.connect(self.check_answer)
        self.exit_button.clicked.connect(self.back)

        self.show()

    def back(self):
        from Main_Project_Window import Main
        self.close()
        self.main_window = Main()
        self.main_window.show()

    def check_answer(self):
        user_answer = self.answer_input.text().strip().lower()
        correct_answer = self.flashcards[self.current_index]["answer"].lower()

        if user_answer == correct_answer:
            self.feedback_label.setText('✅ Correct!')
            self.feedback_label.setStyleSheet("color: green;")
            self.current_index += 1
            if self.current_index < len(self.flashcards):
                self.question_label.setText(self.flashcards[self.current_index]["question"])
                self.answer_input.clear()
            else:
                self.feedback_label.setText("🎉 You finished all questions!")
                self.check_button.setEnabled(False)
                self.answer_input.setEnabled(False)
        else:
            self.feedback_label.setText("❌ Try again!")
            self.feedback_label.setStyleSheet("color: red;")

if __name__ == '__main__':
    app = QApplication([])
    win = PythonMain()
    app.exec_()
