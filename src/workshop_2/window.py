from .buttons import Buttons
from .stack import Stack
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class Window(QMainWindow):

  def __init__(self) -> None:
    super().__init__()
    self.setWindowTitle("Countdown Timer App")
    self.resize(300, 200)

    central_widget = QWidget(self)
    self.setCentralWidget(central_widget)
    main_layout = QVBoxLayout(central_widget)

    self.stack_widget = Stack(self)
    self.buttons_widget = Buttons(self)

    main_layout.addWidget(self.stack_widget)
    main_layout.addWidget(self.buttons_widget)

    self.buttons_widget.start.connect(self.stack_widget.start_counter)
    self.buttons_widget.start.connect(lambda: self._switch_buttons(False))

    self.buttons_widget.pause.connect(self.stack_widget.pause)
    self.buttons_widget.pause.connect(lambda: self._switch_buttons(True))

    self.buttons_widget.reset.connect(self.stack_widget.reset)
    self.buttons_widget.reset.connect(lambda: self.buttons_widget.reset_buttons())
    
    self.stack_widget.time_stopped.connect(lambda: self.buttons_widget.reset_buttons())

  def _switch_buttons(self, state: bool) -> None:
    self.buttons_widget.timer_paused = state