from PySide6.QtCore import QTimer, Signal, Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QStackedWidget, QWidget


class Stack(QStackedWidget):
    time_stopped = Signal(bool)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.remaining_seconds = 0

        self.input_page = QWidget()
        self.input_layout = QHBoxLayout(self.input_page)

        self.input_line = QLineEdit(self.input_page)
        self.input_line.setPlaceholderText("Enter seconds...")

        validator = QIntValidator(0, 86400, self)
        self.input_line.setValidator(validator)

        self.input_layout.addWidget(self.input_line)

        self.timer_label = QLabel("00:00", self)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 32px; font-weight: bold;")

        self.addWidget(self.input_page)
        self.addWidget(self.timer_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._decrement)

    def start_counter(self) -> None:
        if self.currentIndex() == 0:
            text = self.input_line.text()
            if not text:
                return
            self.remaining_seconds = int(text)
            if self.remaining_seconds <= 0:
                return
            self.setCurrentIndex(1)

        self._update_label()
        self.timer.start(1000)

    def pause(self) -> None:
        self.timer.stop()

    def _decrement(self) -> None:
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self._update_label()

        if self.remaining_seconds <= 0:
            self.timer.stop()
            self.reset()
            self.time_stopped.emit(True)
            
    def _update_label(self) -> None:
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")

    def reset(self) -> None:
        self.timer.stop()
        self.remaining_seconds = 0
        self.input_line.clear()
        self.setCurrentIndex(0)
        self.timer_label.setText("00:00")