from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from workshop2.data import MyData
from workshop2.status_widget import StatusWidget
from workshop2.input import Input

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("clock")
        self.resize(400,480)
        self.data=MyData(self)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        self.layout = QVBoxLayout(centralWidget)
        self.status_widget = StatusWidget("clock.qml", data_bridge=self.data)
        self.layout.addWidget(self.status_widget, stretch=1)
        
        self.input_widget = Input()
        self.input_widget.time_entered.connect(self._set_time)
        self.layout.addWidget(self.input_widget)
        
        self.show()
    def _set_time(self, hour: int, min: int, sec: int):
        self.data.hours = hour
        self.data.mins = min
        self.data.secs = sec

