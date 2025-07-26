from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QIcon
from Python_Questions import PythonMain
from JavaScript_Questions import JavaMain
from Html_Questions import HtmlMain
from Css_Questions import CssMain
from Django_Questions import DjangoMain
from Java_Questions import JavaMain as JavaQuestionsMain

class Main(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle('Programming Language Quiz')
        self.setWindowIcon(QIcon('point-dinterrogation.png'))
        self.setFixedSize(420, 500)

        # Main layout
        self.layout = QVBoxLayout()
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(30, 20, 30, 20)

        # Title
        title = QLabel("Choose a Language")
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title)

        # Top space
        self.add_spacer()

        # Buttons (Same height/width)
        self.add_button('Python Questions', self.Python)
        self.add_button('JavaScript Questions', self.JavaScript)
        self.add_button('HTML Questions', self.Html)
        self.add_button('CSS Questions', self.Css)
        self.add_button('Django Questions', self.Django)
        self.add_button('Java Questions', self.Java)

        # Bottom space
        self.add_spacer()

        self.setLayout(self.layout)
        self.show()

    def add_button(self, text, handler):
        button = QPushButton(text)
        button.setFont(QFont('Arial', 14))
        button.setFixedSize(260, 45)
        button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        button.clicked.connect(handler)
        self.layout.addWidget(button, alignment=Qt.AlignCenter)

    def add_spacer(self):
        spacer = QSpacerItem(200, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addSpacerItem(spacer)

    def JavaScript(self):
        self.hide()
        self.main1 = JavaMain()
        self.main1.show()

    def Python(self):
        self.hide()
        self.main2 = PythonMain()
        self.main2.show()

    def Html(self):
        self.hide()
        self.main3 = HtmlMain()
        self.main3.show()

    def Css(self):
        self.hide()
        self.main4 = CssMain()
        self.main4.show()

    def Django(self):
        self.hide()
        self.main5 = DjangoMain()
        self.main5.show()

    def Java(self):
        self.hide()
        self.main6 = JavaQuestionsMain()
        self.main6.show()


if __name__ == '__main__':
    app = QApplication([])
    win = Main()
    app.exec_()
