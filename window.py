from PySide6.QtWidgets import QPushButton, QWidget, QTextEdit, QVBoxLayout, QLabel, QRadioButton, QHBoxLayout
from config import MW_TITLE, MW_HEIGHT, MW_WIDTH, FOCUSED_QUESTION, KNOW_NEXT_STEP_QUESTION, DOING_QUESTION, DOING_PLACEHOLDER

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(MW_TITLE)
        self.resize(MW_HEIGHT, MW_WIDTH)

        # Layout
        layout = QVBoxLayout()

        # "Focused?" question
        focused_label = QLabel(FOCUSED_QUESTION)
        layout.addWidget(focused_label)

        inner_container = QWidget()
        inner_layout = QHBoxLayout(inner_container)

        self.focused_button = QRadioButton("Yes")
        self.unfocused_button = QRadioButton("No")
        inner_layout.addWidget(self.focused_button)
        inner_layout.addWidget(self.unfocused_button)
        layout.addWidget(inner_container)

        # "What are you doing?" question
        doing_label = QLabel(DOING_QUESTION)
        layout.addWidget(doing_label)

        self.doing = QTextEdit()
        self.doing.setPlaceholderText(DOING_PLACEHOLDER)
        self.doing.setFixedHeight(100)

        layout.addWidget(self.doing)

        # "Do you know the next step?" question
        self.know_next_step_label = QLabel(KNOW_NEXT_STEP_QUESTION)
        layout.addWidget(self.know_next_step_label)

        inner_container = QWidget()
        inner_layout = QHBoxLayout(inner_container)

        self.know_button = QRadioButton("Yes")
        self.not_know_button = QRadioButton("No")
        inner_layout.addWidget(self.know_button)
        inner_layout.addWidget(self.not_know_button)
        layout.addWidget(inner_container)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_value)
        layout.addWidget(self.submit_button)

        content = QWidget()
        content.setLayout(layout)
        self.setLayout(layout)

    def submit_value(self):
        """
        Closes the window.
        """
        self.close()