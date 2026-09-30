from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget


class Buttons(QWidget):
    start = Signal()
    pause = Signal()
    reset = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._is_paused = False

        self.btn_start = QPushButton("Start")
        self.btn_reset = QPushButton("Reset")

        self.btn_start.clicked.connect(self._b1_clicked)
        self.btn_reset.clicked.connect(self._b2_clicked)

        layout = QHBoxLayout(self)
        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_reset)

    @property
    def timer_paused(self) -> bool:
        return self._is_paused

    @timer_paused.setter
    def timer_paused(self, state: bool) -> None:
        self._is_paused = state
        if self._is_paused:
            self.btn_start.setText("Resume")
        else:
                self.btn_start.setText("Pause")
        
    def reset_buttons(self) -> None:
        self._is_paused = False
        self.btn_start.setText("Start")


    def _b1_clicked(self) -> None:
        if self._is_paused:
            self.pause.emit()
            self._is_paused = False
        else:
            self.start.emit()
            self._is_paused = True
            self.btn_start.setText("Pause")

            
    def _b2_clicked(self) -> None:
        self.reset.emit()
        self._is_paused = False
        self.btn_start.setText("Start")
