from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QIcon


class JavaMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JavaScript Questions')
        self.setWindowIcon(QIcon('script-java.png'))
        self.setFixedSize(420, 500)
        self.current_index = 0

        # Step 2: Define flashcards (can come before or after current_index)
        self.flashcards = [
            {"question": "What keyword is used to declare a variable in JavaScript?", "answer": "var"},
            {"question": "Which keyword declares a block-scoped variable?", "answer": "let"},
            {"question": "How do you declare a constant in JavaScript?", "answer": "const"},
            {"question": "Which symbol is used for single-line comments?", "answer": "//"},
            {"question": "Which symbol is used for multi-line comments?", "answer": "/* */"},
            {"question": "How do you write a string in JavaScript?", "answer": "Using quotes ('' or \"\")"},
            {"question": "What is the type of NaN?", "answer": "number"},
            {"question": "How do you write a function in JavaScript?", "answer": "function myFunc() {}"},
            {"question": "What is the output of typeof null?", "answer": "object"},
            {"question": "Which keyword refers to the current object?", "answer": "this"},
            {"question": "What is the correct way to write an array?", "answer": "[1, 2, 3]"},
            {"question": "How do you access the first item in an array?", "answer": "array[0]"},
            {"question": "Which method adds an element to the end of an array?", "answer": "push()"},
            {"question": "Which method removes the last item in an array?", "answer": "pop()"},
            {"question": "Which method adds an element to the beginning of an array?", "answer": "unshift()"},
            {"question": "Which method removes the first item of an array?", "answer": "shift()"},
            {"question": "How do you find the length of an array?", "answer": "array.length"},
            {"question": "What is the operator for strict equality?", "answer": "==="},
            {"question": "What does '===' check for?", "answer": "Value and type equality"},
            {"question": "What is the output of 2 + '2'?", "answer": "22"},
            {"question": "What is the output of 2 - '2'?", "answer": "0"},
            {"question": "Which function parses a string into an integer?", "answer": "parseInt()"},
            {"question": "Which function parses a string into a float?", "answer": "parseFloat()"},
            {"question": "What keyword is used to create a class in JavaScript?", "answer": "class"},
            {"question": "How do you create a new object from a class?", "answer": "new ClassName()"},
            {"question": "How do you write an arrow function?", "answer": "() => {}"},
            {"question": "What is the output of typeof undefined?", "answer": "undefined"},
            {"question": "What is the default value of a declared but unassigned variable?", "answer": "undefined"},
            {"question": "Which loop runs at least once?", "answer": "do...while"},
            {"question": "How do you write a conditional in JavaScript?", "answer": "if (condition) {}"},
            {"question": "How do you check if a value is not equal in JavaScript?", "answer": "!="},
            {"question": "What does the '+' operator do with strings?", "answer": "Concatenates them"},
            {"question": "What is the difference between '==' and '==='?",
             "answer": "'==' compares values; '===' compares values and types"},
            {"question": "How do you define an object?", "answer": "Using curly braces {}"},
            {"question": "How do you access an object property?", "answer": "obj.key or obj['key']"},
            {"question": "What is a callback function?",
             "answer": "A function passed to another function as an argument"},
            {"question": "How do you get the current date in JavaScript?", "answer": "new Date()"},
            {"question": "What is JSON?", "answer": "JavaScript Object Notation"},
            {"question": "How do you convert an object to JSON?", "answer": "JSON.stringify()"},
            {"question": "How do you convert JSON to an object?", "answer": "JSON.parse()"},
            {"question": "What is the purpose of setTimeout?", "answer": "To delay code execution"},
            {"question": "What is the purpose of setInterval?", "answer": "To run code repeatedly"},
            {"question": "How do you select an element by ID?", "answer": "document.getElementById()"},
            {"question": "How do you select elements by class name?", "answer": "document.getElementsByClassName()"},
            {"question": "How do you select elements using CSS selectors?", "answer": "document.querySelector()"},
            {"question": "How do you change the text of an HTML element?",
             "answer": "element.textContent or element.innerText"},
            {"question": "How do you change the HTML of an element?", "answer": "element.innerHTML"},
            {"question": "How do you add an event listener?", "answer": "element.addEventListener()"},
            {"question": "What is the event object in JavaScript?", "answer": "An object that describes an event"},
            {"question": "What is a promise?", "answer": "An object representing a future result"},
            {"question": "Which method is used to handle fulfilled promises?", "answer": ".then()"},
            {"question": "Which method is used to handle promise errors?", "answer": ".catch()"},
            {"question": "What does async mean in JavaScript?", "answer": "Declares a function that returns a promise"},
            {"question": "What does await do?", "answer": "Pauses execution until the promise resolves"},
            {"question": "What is hoisting?", "answer": "Variable and function declarations are moved to the top"},
            {"question": "What is the DOM?", "answer": "Document Object Model"},
            {"question": "What does isNaN() check?", "answer": "If a value is Not-a-Number"},
            {"question": "What is a closure in JavaScript?",
             "answer": "A function that remembers variables from its outer scope"},
            {"question": "What is the use of the spread operator (...)?", "answer": "To expand iterable elements"},
            {"question": "How do you combine two arrays?", "answer": "Using concat() or spread operator"},
            {"question": "How do you find an element in an array?", "answer": "Using find() or indexOf()"}
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
    win = JavaMain()
    app.exec_()
