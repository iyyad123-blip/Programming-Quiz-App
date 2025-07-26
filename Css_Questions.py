from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QIcon

class CssMain(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Css Questions')
        self.setWindowIcon(QIcon('css-3.png'))
        self.setFixedSize(420, 500)
        self.current_index = 0
        # Step 2: Define flashcards (can come before or after current_index)
        self.flashcards = [
            {"question": "What does CSS stand for?", "answer": "Cascading Style Sheets"},
            {"question": "How do you link an external CSS file to an HTML document?",
             "answer": "<link rel='stylesheet' href='style.css'>"},
            {"question": "Which property is used to change the text color?", "answer": "color"},
            {"question": "How do you change the background color of an element?", "answer": "background-color"},
            {"question": "What is the CSS syntax to select an element by its id?", "answer": "#id"},
            {"question": "What is the CSS syntax to select elements by their class?", "answer": ".class"},
            {"question": "How do you select all <p> elements in CSS?", "answer": "p"},
            {"question": "What property controls the font size?", "answer": "font-size"},
            {"question": "How do you make text bold using CSS?", "answer": "font-weight: bold;"},
            {"question": "Which property controls the space between letters?", "answer": "letter-spacing"},
            {"question": "How do you center-align text?", "answer": "text-align: center;"},
            {"question": "What property is used to control the width of an element?", "answer": "width"},
            {"question": "How do you add space inside an element between its content and border?", "answer": "padding"},
            {"question": "How do you add space outside an element?", "answer": "margin"},
            {"question": "Which CSS property changes the font family?", "answer": "font-family"},
            {"question": "How do you apply CSS styles inline within an HTML element?",
             "answer": "Using the style attribute"},
            {"question": "What does 'Cascading' mean in CSS?",
             "answer": "Styles are applied based on specificity and order"},
            {"question": "Which property controls the element's border color?", "answer": "border-color"},
            {"question": "How do you remove the underline from links?", "answer": "text-decoration: none;"},
            {"question": "What property controls the opacity of an element?", "answer": "opacity"},
            {"question": "How do you make an element float to the right?", "answer": "float: right;"},
            {"question": "What is the default position value for elements?", "answer": "static"},
            {"question": "Which property allows you to position an element absolutely?",
             "answer": "position: absolute;"},
            {"question": "What property controls the stacking order of overlapping elements?", "answer": "z-index"},
            {"question": "How do you add a shadow to text?", "answer": "text-shadow"},
            {"question": "Which property controls the height of an element?", "answer": "height"},
            {"question": "How do you make an element's background image cover the entire area?",
             "answer": "background-size: cover;"},
            {"question": "What does the box model consist of?", "answer": "content, padding, border, and margin"},
            {"question": "How do you select all elements inside a div?", "answer": "div *"},
            {"question": "What selector targets direct children only?", "answer": ">"},
            {"question": "How do you make text italic?", "answer": "font-style: italic;"},
            {"question": "Which property controls the space between lines of text?", "answer": "line-height"},
            {"question": "How do you create a rounded corner?", "answer": "border-radius"},
            {"question": "What is the syntax for a CSS comment?", "answer": "/* comment */"},
            {"question": "How do you hide an element without removing it from the layout?",
             "answer": "visibility: hidden;"},
            {"question": "How do you completely hide an element?", "answer": "display: none;"},
            {"question": "Which property controls whether content overflows its container?", "answer": "overflow"},
            {"question": "How do you change the cursor to a pointer on hover?", "answer": "cursor: pointer;"},
            {"question": "What pseudo-class applies styles when the mouse is over an element?", "answer": ":hover"},
            {"question": "How do you apply styles to the first child element?", "answer": ":first-child"},
            {"question": "Which property controls the space between words?", "answer": "word-spacing"},
            {"question": "What is a media query used for?",
             "answer": "To apply styles based on device characteristics like screen size"},
            {"question": "How do you make a website responsive?",
             "answer": "Using flexible layouts, media queries, and relative units"},
            {"question": "Which unit is relative to the font size of the root element?", "answer": "rem"},
            {"question": "What does flexbox help with?",
             "answer": "Creating flexible and responsive layout structures"},
            {"question": "What property defines the main axis direction in flexbox?", "answer": "flex-direction"},
            {"question": "How do you center content horizontally and vertically using flexbox?",
             "answer": "justify-content: center; align-items: center;"},
            {"question": "What does the float property do?",
             "answer": "Allows elements to be taken out of the normal flow and aligned left or right"},
            {"question": "What property is used to control transparency in rgba colors?",
             "answer": "The alpha channel (the fourth value in rgba)"},
            {"question": "What is the difference between class selector and id selector in CSS?",
             "answer": "Class selects multiple elements; id selects a single unique element"},
            {"question": "How do you make a fixed navigation bar?", "answer": "position: fixed; top: 0;"},
            {"question": "What does the display property do?",
             "answer": "Controls how an element is displayed (block, inline, flex, none, etc.)"},
            {"question": "How do you create a grid layout?", "answer": "Using display: grid;"},
            {"question": "What is the difference between padding and margin?",
             "answer": "Padding is inside the element border; margin is outside"},
            {"question": "What does the !important declaration do?", "answer": "Overrides other conflicting CSS rules"},
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
    win = CssMain()
    win.show()
    app.exec_()
