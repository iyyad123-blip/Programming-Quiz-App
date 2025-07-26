from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QIcon


class DjangoMain(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Django Questions')
        self.setWindowIcon(QIcon('django.png'))
        self.setFixedSize(420, 500)
        self.current_index = 0

        # Step 2: Define flashcards (can come before or after current_index)
        self.flashcards = [
            {"question": "What is Django?", "answer": "A high-level Python web framework"},
            {"question": "Which command creates a new Django project?",
             "answer": "django-admin startproject projectname"},
            {"question": "Which command creates a new app in Django?", "answer": "python manage.py startapp appname"},
            {"question": "What file contains database configurations?", "answer": "settings.py"},
            {"question": "What is a Django model?", "answer": "A Python class that maps to a database table"},
            {"question": "How do you define a model field for a character string?", "answer": "CharField"},
            {"question": "Which method saves a model instance to the database?", "answer": "save()"},
            {"question": "What is a Django view?",
             "answer": "A function or class that handles a web request and returns a response"},
            {"question": "How do you map a URL to a view?", "answer": "Using urlpatterns in urls.py"},
            {"question": "What template engine does Django use by default?",
             "answer": "Django Template Language (DTL)"},
            {"question": "What is a QuerySet?", "answer": "A collection of database queries in Django"},
            {"question": "How do you filter objects in a QuerySet?", "answer": "Using filter() method"},
            {"question": "Which command applies migrations to the database?", "answer": "python manage.py migrate"},
            {"question": "How do you create migration files?", "answer": "python manage.py makemigrations"},
            {"question": "What is the purpose of migrations?",
             "answer": "To propagate model changes to the database schema"},
            {"question": "How do you register a model with the admin site?",
             "answer": "By importing it in admin.py and calling admin.site.register(ModelName)"},
            {"question": "What does the 'urls.py' file do?", "answer": "Defines URL routing for the Django app"},
            {"question": "What is the difference between a project and an app in Django?",
             "answer": "A project is the whole website; an app is a web component inside the project"},
            {"question": "How do you create a superuser?", "answer": "python manage.py createsuperuser"},
            {"question": "How do you serve static files in development?",
             "answer": "Using django.contrib.staticfiles and configuring STATIC_URL"},
            {"question": "Which setting defines the database engine?", "answer": "DATABASES['default']['ENGINE']"},
            {"question": "How do you access POST data in a view?", "answer": "request.POST"},
            {"question": "What is the purpose of CSRF protection?",
             "answer": "To prevent Cross-Site Request Forgery attacks"},
            {"question": "How do you include CSRF token in a Django template form?", "answer": "{% csrf_token %}"},
            {"question": "What is Django’s ORM?",
             "answer": "Object-Relational Mapping to interact with the database using Python"},
            {"question": "How do you perform a foreign key relationship in Django models?",
             "answer": "Using models.ForeignKey"},
            {"question": "What is a ManyToManyField?",
             "answer": "A field representing many-to-many relationships between models"},
            {"question": "What is the use of get_object_or_404()?",
             "answer": "Returns an object or raises a 404 error if not found"},
            {"question": "How do you create a form in Django?",
             "answer": "By subclassing django.forms.Form or ModelForm"},
            {"question": "How do you validate form data in Django?", "answer": "Using form.is_valid() method"},
            {"question": "What is the purpose of the 'context' dictionary in views?",
             "answer": "To pass data to templates"},
            {"question": "How do you reverse a URL by its name in Django?",
             "answer": "Using django.urls.reverse or the {% url %} template tag"},
            {"question": "What is middleware in Django?",
             "answer": "Hooks into request/response processing for custom logic"},
            {"question": "How do you enable Django’s debug mode?", "answer": "Set DEBUG = True in settings.py"},
            {"question": "What is the default database in Django?", "answer": "SQLite"},
            {"question": "How do you use Django’s built-in User model?",
             "answer": "Import from django.contrib.auth.models"},
            {"question": "How do you customize the User model?",
             "answer": "By subclassing AbstractUser or AbstractBaseUser"},
            {"question": "What is the function of the manage.py file?",
             "answer": "A command-line utility to interact with the Django project"},
            {"question": "How do you add pagination in Django?", "answer": "Using django.core.paginator.Paginator"},
            {"question": "What does the 'static' template tag do?", "answer": "Returns the URL of a static file"},
            {"question": "How do you send emails in Django?", "answer": "Using django.core.mail.send_mail"},
            {"question": "What is the purpose of Django’s sessions framework?",
             "answer": "To store user data between requests"},
            {"question": "How do you handle file uploads in Django?",
             "answer": "Using FileField or ImageField in models"},
            {"question": "What is a class-based view?",
             "answer": "A view implemented as a Python class instead of a function"},
            {"question": "How do you redirect a user in a Django view?", "answer": "Using django.shortcuts.redirect"},
            {"question": "What is the use of @login_required decorator?",
             "answer": "Restricts access to authenticated users"},
            {"question": "How do you set up internationalization (i18n) in Django?",
             "answer": "By enabling middleware and using translation functions"},
            {"question": "What is the purpose of Django signals?",
             "answer": "To allow decoupled applications to get notified when actions occur"},
            {"question": "What does the migrate command do?", "answer": "Applies database schema changes"},
            {"question": "How do you create custom management commands?",
             "answer": "By creating a management/commands directory inside an app"},
            {"question": "What is the purpose of fixtures in Django?",
             "answer": "To load initial data into the database"},
            {"question": "How do you cache views in Django?", "answer": "Using cache_page decorator"},
            {"question": "What is Django REST Framework?", "answer": "A toolkit to build Web APIs in Django"},
            {"question": "How do you protect a view from CSRF attacks?",
             "answer": "Using csrf_protect decorator or {% csrf_token %} in templates"},
            {"question": "What is the default port Django development server runs on?", "answer": "8000"},
            {"question": "How do you configure allowed hosts in Django?",
             "answer": "Using ALLOWED_HOSTS in settings.py"},
            {"question": "What are Django fixtures?",
             "answer": "Files that contain serialized data for loading into the database"},
            {"question": "How do you enable admin interface in Django?",
             "answer": "By including django.contrib.admin in INSTALLED_APPS and running migrate"},
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

        # Layout
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
    win = DjangoMain()
    app.exec_()