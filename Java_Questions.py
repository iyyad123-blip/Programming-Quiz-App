from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QIcon


class JavaMain(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Java Questions')
        self.setWindowIcon(QIcon('java.png'))
        self.setFixedSize(420, 500)

        self.current_index = 0

        # Step 2: Define flashcards (can come before or after current_index)
        self.flashcards = [
            {"question": "What is the size of int in Java?", "answer": "4 bytes"},
            {"question": "Which keyword is used to create a class?", "answer": "class"},
            {"question": "What is the entry point of a Java program?",
             "answer": "public static void main(String[] args)"},
            {"question": "Which keyword is used to inherit a class?", "answer": "extends"},
            {"question": "Which keyword is used to implement an interface?", "answer": "implements"},
            {"question": "What is method overloading?",
             "answer": "Defining multiple methods with the same name but different parameters"},
            {"question": "What is method overriding?", "answer": "Redefining a parent class method in a child class"},
            {"question": "What is a constructor?", "answer": "A special method used to initialize objects"},
            {"question": "What is encapsulation?", "answer": "Wrapping data and methods into a single unit (class)"},
            {"question": "What is inheritance?", "answer": "Acquiring properties and behaviors from another class"},
            {"question": "What is polymorphism?",
             "answer": "Ability to take many forms (method overloading and overriding)"},
            {"question": "What is an interface?",
             "answer": "An abstract type used to specify a behavior that classes must implement"},
            {"question": "What is an abstract class?",
             "answer": "A class that cannot be instantiated and may contain abstract methods"},
            {"question": "Which collection class allows duplicate elements?", "answer": "List"},
            {"question": "Which collection does not allow duplicates?", "answer": "Set"},
            {"question": "What does JVM stand for?", "answer": "Java Virtual Machine"},
            {"question": "What does JRE stand for?", "answer": "Java Runtime Environment"},
            {"question": "What does JDK stand for?", "answer": "Java Development Kit"},
            {"question": "What is the default value of boolean in Java?", "answer": "false"},
            {"question": "What is the use of the 'final' keyword?",
             "answer": "To make a variable constant, a method un-overridable, or a class un-inheritable"},
            {"question": "How do you create an object in Java?", "answer": "Using the new keyword: new ClassName()"},
            {"question": "What is a package in Java?", "answer": "A namespace that organizes classes and interfaces"},
            {"question": "How do you import a package?", "answer": "import packageName.ClassName;"},
            {"question": "What is exception handling?", "answer": "Mechanism to handle runtime errors"},
            {"question": "What keywords are used in exception handling?",
             "answer": "try, catch, finally, throw, throws"},
            {"question": "What is a checked exception?", "answer": "An exception checked at compile time"},
            {"question": "What is an unchecked exception?", "answer": "An exception not checked at compile time"},
            {"question": "What is the base class of all exceptions?", "answer": "Throwable"},
            {"question": "What is garbage collection?", "answer": "Process of automatic memory management"},
            {"question": "How do you run a thread in Java?",
             "answer": "Extend Thread or implement Runnable and call start()"},
            {"question": "What is synchronization?",
             "answer": "Controlling access to shared resources by multiple threads"},
            {"question": "What is the use of static keyword?",
             "answer": "To create methods or variables that belong to the class, not instances"},
            {"question": "What is the difference between == and equals()?",
             "answer": "== compares references, equals() compares values"},
            {"question": "What is the use of super keyword?", "answer": "To refer to the parent class"},
            {"question": "What is the use of this keyword?", "answer": "To refer to the current class instance"},
            {"question": "What is the difference between ArrayList and LinkedList?",
             "answer": "ArrayList is backed by an array, LinkedList by nodes"},
            {"question": "What is the purpose of toString()?",
             "answer": "To return a string representation of an object"},
            {"question": "What is the output of System.out.println(10 + 20 + \"Hello\")?", "answer": "30Hello"},
            {"question": "How do you handle multiple exceptions?",
             "answer": "Using multiple catch blocks or multi-catch (Java 7+)"},
            {"question": "What is a lambda expression?",
             "answer": "A short block of code which takes in parameters and returns a value"},
            {"question": "What is a functional interface?", "answer": "An interface with only one abstract method"},
            {"question": "How do you write a for-each loop?", "answer": "for (Type item : collection)"},
            {"question": "How do you declare an array?", "answer": "int[] arr = new int[5];"},
            {"question": "What is the difference between String, StringBuilder, and StringBuffer?",
             "answer": "Mutability and thread-safety"},
            {"question": "What is the use of instanceof operator?", "answer": "To check object type at runtime"},
            {"question": "What is autoboxing?", "answer": "Automatic conversion from primitive to wrapper"},
            {"question": "What is unboxing?", "answer": "Conversion from wrapper to primitive"},
            {"question": "What is a singleton class?", "answer": "A class that allows only one instance"},
            {"question": "What is the purpose of the transient keyword?",
             "answer": "To prevent serialization of a variable"},
            {"question": "What is the difference between throw and throws?",
             "answer": "throw is used to explicitly throw an exception, throws declares it"},
            {"question": "What is the purpose of finalize() method?",
             "answer": "To perform cleanup before garbage collection"},
            {"question": "What is the difference between public, private, protected?",
             "answer": "Access modifiers for classes, methods, variables"},
            {"question": "Can a class be both abstract and final?", "answer": "No, they are contradictory"},
            {"question": "What is the default value of int?", "answer": "0"},
            {"question": "What is the difference between break and continue?",
             "answer": "break exits loop, continue skips to next iteration"},
            {"question": "What is the result of 5/2 in Java?", "answer": "2 (integer division)"},
            {"question": "How do you generate random numbers?", "answer": "Using Random class or Math.random()"},
            {"question": "What does the 'native' keyword mean?",
             "answer": "Indicates a method is implemented in native (non-Java) code"},
            {"question": "What is the use of annotations in Java?", "answer": "Provide metadata about code"}
        ]

        # Title Label
        self.question_label = QLabel(self.flashcards[self.current_index]["question"])
        self.question_label.setFont(QFont('Arial', 16, QFont.Bold))
        self.question_label.setWordWrap(True)
        self.question_label.setAlignment(Qt.AlignCenter)

        # Answer Input
        self.answer_input = QLineEdit()
        self.answer_input.setFont(QFont('Arial', 14))
        self.answer_input.setFixedSize(300, 40)
        self.answer_input.setPlaceholderText("Type your answer...")

        # Check Button
        self.check_button = QPushButton("Check Answer")
        self.check_button.setFont(QFont('Arial', 14))
        self.check_button.setFixedSize(200, 45)
        self.check_button.setStyleSheet("""
                    QPushButton {
                        background-color: #2ecc71;
                        color: white;
                        border-radius: 10px;
                    }
                    QPushButton:hover {
                        background-color: #27ae60;
                    }
                """)

        # Feedback
        self.feedback_label = QLabel("")
        self.feedback_label.setFont(QFont('Arial', 13))
        self.feedback_label.setAlignment(Qt.AlignCenter)

        # Exit Button
        self.Exit_button = QPushButton("← Back")
        self.Exit_button.setFont(QFont('Arial', 13))
        self.Exit_button.setFixedSize(100, 35)
        self.Exit_button.setStyleSheet("""
                    QPushButton {
                        background-color: #e74c3c;
                        color: white;
                        border-radius: 8px;
                    }
                    QPushButton:hover {
                        background-color: #c0392b;
                    }
                """)

        # Layout
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(30, 30, 30, 100)

        self.layout.addWidget(self.question_label)
        self.layout.addWidget(self.answer_input, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.check_button, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.feedback_label)
        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.Exit_button, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

        # Connections
        self.check_button.clicked.connect(self.check_answer)
        self.Exit_button.clicked.connect(self.back)

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
            self.feedback_label.setText("✅ Correct!")
            self.feedback_label.setFont(QFont('Arial', 20))
            self.current_index += 1
            if self.current_index < len(self.flashcards):
                self.question_label.setText(self.flashcards[self.current_index]["question"])
                self.answer_input.clear()
            else:
                self.feedback_label.setText("🎉 You finished all questions!")
                self.check_button.setEnabled(False)
        else:
            self.feedback_label.setText("❌ Try again!")

if __name__ == '__main__':
    app = QApplication([])
    win = JavaMain()
    app.exec_()
