from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Signal
from PySide6.QtGui import QIntValidator

class Input(QWidget):
    time_entered = Signal(int, int, int)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        inputs_layout = QHBoxLayout()
        
        self.hour_input = QLineEdit()
        self.hour_input.setPlaceholderText("Hour")
        self.hour_input.setValidator(QIntValidator(0, 23, self))

        self.min_input = QLineEdit()
        self.min_input.setPlaceholderText("Minute")
        self.min_input.setValidator(QIntValidator(0, 59, self))

        self.sec_input = QLineEdit()
        self.sec_input.setPlaceholderText("Second")
        self.sec_input.setValidator(QIntValidator(0, 59, self))

        inputs_layout.addWidget(self.hour_input)
        inputs_layout.addWidget(self.min_input)
        inputs_layout.addWidget(self.sec_input)

        self.confirm_btn = QPushButton("Confirm")
        self.confirm_btn.clicked.connect(self._confirm_input)

        layout.addLayout(inputs_layout)
        layout.addWidget(self.confirm_btn)

    def _confirm_input(self):
        h = int(self.hour_input.text()) if self.hour_input.text() else 0
        m = int(self.min_input.text()) if self.min_input.text() else 0
        s = int(self.sec_input.text()) if self.sec_input.text() else 0
        self.time_entered.emit(h, m, s)