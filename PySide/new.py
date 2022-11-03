import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl

if __name__ == "__main__":
    app = QApplication([])
    view = QQuickView()
    view.setSource(QUrl('./SimplePPT_ui.qml'))
    view.show()
    sys.exit(app.exec())
