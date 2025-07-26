from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QIcon


class HtmlMain(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('HTML Questions')
        self.setWindowIcon(QIcon('html-5.png'))
        self.setFixedSize(420, 500)
        self.current_index = 0


        self.flashcards = [
            {"question": "What does HTML stand for?", "answer": "HyperText Markup Language"},
            {"question": "Which tag is used to create a hyperlink?", "answer": "<a>"},
            {"question": "How do you insert an image in HTML?", "answer": "<img>"},
            {"question": "What is the purpose of the <title> tag?",
             "answer": "Defines the title of the webpage shown in the browser tab"},
            {"question": "How do you create an unordered list?", "answer": "<ul>"},
            {"question": "How do you create an ordered list?", "answer": "<ol>"},
            {"question": "Which tag defines a list item?", "answer": "<li>"},
            {"question": "What tag is used for paragraph text?", "answer": "<p>"},
            {"question": "How do you create a line break?", "answer": "<br>"},
            {"question": "Which tag is used to define a table?", "answer": "<table>"},
            {"question": "What tag defines a table row?", "answer": "<tr>"},
            {"question": "Which tag defines a table header cell?", "answer": "<th>"},
            {"question": "Which tag defines a table data cell?", "answer": "<td>"},
            {"question": "How do you add a comment in HTML?", "answer": "<!-- comment -->"},
            {"question": "What attribute specifies the URL of a link?", "answer": "href"},
            {"question": "What attribute specifies the source of an image?", "answer": "src"},
            {"question": "What attribute provides alternative text for an image?", "answer": "alt"},
            {"question": "How do you create a checkbox input?", "answer": "<input type='checkbox'>"},
            {"question": "How do you create a radio button?", "answer": "<input type='radio'>"},
            {"question": "Which tag is used to create a dropdown list?", "answer": "<select>"},
            {"question": "Which tag defines options inside a dropdown?", "answer": "<option>"},
            {"question": "What tag defines a form?", "answer": "<form>"},
            {"question": "What attribute specifies the method for submitting a form?", "answer": "method"},
            {"question": "What is the default method of a form?", "answer": "GET"},
            {"question": "How do you specify that a form data should be sent securely?", "answer": "Use method='POST'"},
            {"question": "Which tag is used to embed a video?", "answer": "<video>"},
            {"question": "Which tag is used to embed audio?", "answer": "<audio>"},
            {"question": "Which attribute controls the size of the text in HTML?",
             "answer": "style (e.g., style='font-size:20px;')"},
            {"question": "What does the <head> tag contain?", "answer": "Metadata, scripts, styles, and title"},
            {"question": "What tag is used for the main heading of a page?", "answer": "<h1>"},
            {"question": "What are <h1> to <h6> tags used for?", "answer": "Headings of different levels"},
            {"question": "Which tag is used to create a block-level section?", "answer": "<div>"},
            {"question": "Which tag is used to create an inline container?", "answer": "<span>"},
            {"question": "What tag is used to define emphasized text?", "answer": "<em>"},
            {"question": "What tag is used to define strong importance text?", "answer": "<strong>"},
            {"question": "What is semantic HTML?", "answer": "Using HTML tags that describe their meaning and purpose"},
            {"question": "What does the <nav> tag represent?", "answer": "Navigation links"},
            {"question": "What does the <section> tag represent?", "answer": "A generic section of content"},
            {"question": "What does the <article> tag represent?",
             "answer": "An independent, self-contained piece of content"},
            {"question": "What does the <aside> tag represent?",
             "answer": "Content tangentially related to the main content"},
            {"question": "What is the purpose of the <footer> tag?",
             "answer": "Defines the footer for a section or page"},
            {"question": "What is the purpose of the <header> tag?",
             "answer": "Defines the header for a section or page"},
            {"question": "What attribute is used to specify inline CSS styles?", "answer": "style"},
            {"question": "How do you link an external CSS file?", "answer": "<link rel='stylesheet' href='style.css'>"},
            {"question": "How do you add a favicon to a webpage?", "answer": "<link rel='icon' href='favicon.ico'>"},
            {"question": "What is the difference between the <b> and <strong> tags?",
             "answer": "<b> is for styling bold text; <strong> indicates importance"},
            {"question": "How do you make a section of text italic?", "answer": "<i> or <em>"},
            {"question": "Which attribute controls the behavior of links?", "answer": "target"},
            {"question": "What value of target opens a link in a new tab?", "answer": "_blank"},
            {"question": "How do you specify the language of an HTML document?",
             "answer": "Using the lang attribute on the <html> tag"},
            {"question": "What tag is used to embed JavaScript?", "answer": "<script>"},
            {"question": "Where is the best place to put the <script> tag for loading JS?",
             "answer": "At the end of the <body>"},
            {"question": "What tag is used to define metadata such as character set?", "answer": "<meta>"},
            {"question": "How do you specify UTF-8 character encoding?", "answer": "<meta charset='UTF-8'>"},
            {"question": "What does the DOCTYPE declaration do?", "answer": "Specifies the HTML version and type"},
            {"question": "What is the purpose of the <iframe> tag?",
             "answer": "Embed another HTML page inside the current page"},
            {"question": "How do you create a button in HTML?", "answer": "<button>"},
            {"question": "Which input type allows users to select a date?", "answer": "<input type='date'>"},
            {"question": "What attribute specifies a placeholder text in input?", "answer": "placeholder"},
            {"question": "What attribute is used to disable a form input?", "answer": "disabled"},
            {"question": "How do you create a hidden input field?", "answer": "<input type='hidden'>"},
            {"question": "How do you make an input field required?", "answer": "required attribute"},
            {"question": "What attribute specifies multiple files in file input?", "answer": "multiple"},
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
    win = HtmlMain()
    app.exec_()
