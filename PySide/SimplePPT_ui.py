# coding : utf-8

from PySide6 import (QtCore, QtGui, QtWidgets)
from PySide6.QtCore import (QSize)
from PySide6.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton, QLabel)
from PySide6.QtGui import (QIcon)
import sys
from icon import Uisetup


class mainUi(QMainWindow):
    def __init__(self):
        super(mainUi, self).__init__()
        self.initUI()
        self.retranslateUi()

    def initUI(self):
        icon = QIcon()
        icon.addFile(":/icon/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.setFixedSize(960, 700)
        self.widget = QWidget()
        self.layout = QGridLayout()
        self.widget.setLayout(self.layout)

        self.left_widget = QWidget()
        self.left_widget.setObjectName("left_widget")
        self.left_layout = QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        self.left_button_MP = QPushButton()
        self.left_button_MP.setObjectName("left_button_MP")

        self.left_layout.addWidget(self.left_button_MP, 0, 0, 1, 3)

        self.right_widget = QWidget()
        self.right_widget.setObjectName("right_widget")
        self.right_layout = QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.right_label_MP = QLabel()
        self.right_label_MP.setObjectName("right_label_MP")

        self.right_layout.addWidget(self.right_label_MP, 0, 0, 1, 10)

        self.layout.addWidget(self.left_widget, 0, 0, 1, 2)
        self.layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.widget)

    def retranslateUi(self):
        self.setWindowTitle("Simple PPT")
        self.left_button_MP.setText(QtCore.QCoreApplication.translate("mainUi", "Make PPT"))
        self.right_label_MP.setText(QtCore.QCoreApplication.translate("mainUi", "<h2>Make PPT</h2>"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_Ui = mainUi()
    main_Ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
