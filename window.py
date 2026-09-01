from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QLabel, QRadioButton, QHBoxLayout
from config import MW_TITLE, MW_HEIGHT, MW_WIDTH, FOCUSED_QUESTION, KNOW_NEXT_STEP_QUESTION, DOING_QUESTION

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
        self.doing.setPlaceholderText("Apply to jobs / Write an email")
        self.doing.setFixedHeight(100)

        layout.addWidget(self.doing)

        # know next step?
        self.know_next_step_label = QLabel(KNOW_NEXT_STEP_QUESTION)
        layout.addWidget(self.know_next_step_label)

        inner_container = QWidget()
        inner_layout = QHBoxLayout(inner_container)

        self.know_button = QRadioButton("Yes")
        self.not_know_button = QRadioButton("No")
        inner_layout.addWidget(self.know_button)
        inner_layout.addWidget(self.not_know_button)
        layout.addWidget(inner_container)

        content = QWidget()
        content.setLayout(layout)
        self.setLayout(layout)