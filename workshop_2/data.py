from PySide6.QtCore import QObject, Property, Signal, QTimer
import datetime

class MyData(QObject):
    hours_changed = Signal()
    mins_changed = Signal()
    secs_changed = Signal()

    def __init__(self, parent: QObject | None = None):
        super().__init__(parent)
        now = datetime.datetime.now()
        self._hours = now.hour % 12
        self._mins = now.minute
        self._secs = now.second
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._increment)
        self._timer.start(1000)

    @Property(int, notify=hours_changed)
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, new: int):
        new_h = new % 12
        if self._hours != new_h:
            self._hours = new_h
            self.hours_changed.emit()

    @Property(int, notify=mins_changed)
    def mins(self):
        return self._mins

    @mins.setter
    def mins(self, new: int):
        new_m = new % 60
        if self._mins != new_m:
            self._mins = new_m
            self.mins_changed.emit()

    @Property(int, notify=secs_changed)
    def secs(self):
        return self._secs

    @secs.setter
    def secs(self, new: int):
        new_s = new % 60
        if self._secs != new_s:
            self._secs = new_s
            self.secs_changed.emit()

    def _increment(self):
        self._secs+=1
        if self._secs >= 60 :
            self._secs=0
            self._mins+=1
            if self._mins >= 60:
                self._mins=0
                self._hours=(self.hours + 1)%12
                self.hours_changed.emit()
            self.mins_changed.emit()
        self.secs_changed.emit()
        