from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QTextEdit,
    QVBoxLayout,
    QLabel,
    QRadioButton,
    QHBoxLayout,
)
from PySide6.QtCore import QTimer

from config import (
    MW_TITLE,
    MW_HEIGHT,
    MW_WIDTH,
    MW_STYLESHEET,
    FOCUSED_QUESTION,
    KNOW_NEXT_STEP_QUESTION,
    DOING_QUESTION,
    DOING_PLACEHOLDER,
    REFLECTION_TIMERS,
)
from json_store import JSONStore
from models import ReflectionEntry


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.is_finishing = False

        self.setWindowTitle(MW_TITLE)
        self.resize(MW_WIDTH, MW_HEIGHT)
        self.setStyleSheet(MW_STYLESHEET)

        self.store = JSONStore()

        # Timer
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.show_again)

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
        know_next_step_label = QLabel(KNOW_NEXT_STEP_QUESTION)
        layout.addWidget(know_next_step_label)

        inner_container = QWidget()
        inner_layout = QHBoxLayout(inner_container)

        self.know_button = QRadioButton("Yes")
        self.not_know_button = QRadioButton("No")

        inner_layout.addWidget(self.know_button)
        inner_layout.addWidget(self.not_know_button)

        layout.addWidget(inner_container)

        # Reflection timer buttons
        timer_container = QWidget()
        timer_layout = QHBoxLayout(timer_container)

        for label, minutes in REFLECTION_TIMERS:
            button = QPushButton(label)
            button.clicked.connect(
                lambda checked=False, minutes=minutes: self.submit_value(minutes)
            )
            timer_layout.addWidget(button)

        layout.addWidget(timer_container)

        # Finish button
        self.finish_button = QPushButton("Finish")
        self.finish_button.clicked.connect(self.finish)
        layout.addWidget(self.finish_button)

        self.setLayout(layout)

    def submit_value(self, minutes):
        """
        Save the current reflection and start a timer.
        """
        self.save_current_reflection()

        # Start/restart the timer.
        self.timer.start(minutes * 60 * 1000)

        self.clear_form()
        self.hide()

    def finish(self):
        """
        Save the current reflection and close the application.
        """
        self.save_current_reflection()

        self.is_finishing = True
        self.timer.stop()
        self.close()

    def closeEvent(self, event):
        """
        Handle the window's X button.

        Save an empty reflection, don't start a timer,
        and allow the application to close.
        """
        if not self.is_finishing:
            entry = ReflectionEntry(
                focused=None,
                doing=None,
                know_next_step=None,
            )

            self.store.insert_entry(entry)

        self.timer.stop()
        event.accept()

    def save_current_reflection(self):
        """
        Save the values currently entered in the form.
        """
        entry = ReflectionEntry(
            focused=self.get_focus_value(),
            doing=self.doing.toPlainText().strip(),
            know_next_step=self.get_know_value(),
        )

        self.store.insert_entry(entry)

    def show_again(self):
        """
        Show the reflection window when the timer expires.
        """
        self.show()
        self.raise_()
        self.activateWindow()

    def clear_form(self):
        """
        Reset the form before the next reflection.
        """
        self.focused_button.setAutoExclusive(False)
        self.unfocused_button.setAutoExclusive(False)
        self.focused_button.setChecked(False)
        self.unfocused_button.setChecked(False)
        self.focused_button.setAutoExclusive(True)
        self.unfocused_button.setAutoExclusive(True)

        self.know_button.setAutoExclusive(False)
        self.not_know_button.setAutoExclusive(False)
        self.know_button.setChecked(False)
        self.not_know_button.setChecked(False)
        self.know_button.setAutoExclusive(True)
        self.not_know_button.setAutoExclusive(True)

        self.doing.clear()

    def get_focus_value(self):
        """
        Return True, False, or None depending on the selection.
        """
        if self.focused_button.isChecked():
            return True

        if self.unfocused_button.isChecked():
            return False

        return None

    def get_know_value(self):
        """
        Return True, False, or None depending on the selection.
        """
        if self.know_button.isChecked():
            return True

        if self.not_know_button.isChecked():
            return False

        return None
