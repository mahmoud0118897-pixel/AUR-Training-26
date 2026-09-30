from PySide6.QtWidgets import QWidget
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtCore import QObject, QUrl
from workshop2.assets import get_asset


class StatusWidget(QQuickWidget):
    def __init__(self, widget_filepath: str, data_bridge: QObject | None = None, parent: QWidget | None = None):
        super().__init__(parent)
        self.setSource(QUrl.fromLocalFile(get_asset(widget_filepath)))
        if data_bridge is not None:
            self.rootContext().setContextProperty("dataBridge", data_bridge)