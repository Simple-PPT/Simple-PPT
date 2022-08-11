"""
Don't ask me why you can't find release_GUI.py.
Because this is.

Build with PyQt6.3.1.
Powered by YangZhenxun.
version: v0.0.1 --PyQt
name : Simple PPT(Auto make PPT)

Why name is "Simple PPT"?
Because It can make PPT.
"""

import json
import os
import sys
import time
import relese_system
import requests

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTranslator
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

ah = ''


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setup_Ui(self)
        self.retranslateUi(self)
        self.trans = QTranslator()

    def setup_Ui(self, MainWindow: QMainWindow) -> None:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 50, 151, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 60, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 100, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 251, 20))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(270, 200, 221, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 150, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,800,22))
        self.menubar.setObjectName("menubar")
        self.menuLanguage = QtWidgets.QMenu(self.menubar)
        self.menuLanguage.setObjectName("menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEnglish = QtGui.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionEnglish.setText("English")
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.setText("中文（简体）")
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.action_2)
        self.menubar.addAction(self.menuLanguage.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.show2)  # type: ignore
        self.pushButton_2.clicked.connect(lambda: self.show1(MainWindow))  # type: ignore
        self.actionEnglish.triggered.connect(self.show3)  # type: ignore
        self.action_2.triggered.connect(self.show4)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "Auto-make-PPT' s GUI"))
        self.label.setText(QtCore.QCoreApplication.translate("MainWindow", "version:v0.0.1--PyQt"))
        self.pushButton.setText(QtCore.QCoreApplication.translate("MainWindow", "check new"))
        self.lineEdit.setText(QtCore.QCoreApplication.translate("MainWindow", ""))
        self.label_2.setText(QtCore.QCoreApplication.translate("MainWindow", "Please input your write info.xlsx file's time:"))
        self.pushButton_2.setText(QtCore.QCoreApplication.translate("MainWindow", "OK"))
        self.menuLanguage.setTitle(QtCore.QCoreApplication.translate("MainWindow", "Language"))
        self.new = QtCore.QCoreApplication.translate("MainWindow", "New")
        self.H_N_V = QtCore.QCoreApplication.translate("MainWindow", "Have new version!")
        self.T_D = QtCore.QCoreApplication.translate("MainWindow", "To download")
        self.D_3 = QtCore.QCoreApplication.translate("MainWindow", "Do you want to download the new version?")
        self.OK = QtCore.QCoreApplication.translate("MainWindow", "OK")
        self.Y_4 = QtCore.QCoreApplication.translate("MainWindow", "Your version is new!")
        self.github_E_Title = QtCore.QCoreApplication.translate("MainWindow", "Error")
        self.github_E_Text = QtCore.QCoreApplication.translate("MainWindow", "'github.com 'has no response.")
        self.T_U = QtCore.QCoreApplication.translate("MainWindow", "Timed up")
        self.H_3 = QtCore.QCoreApplication.translate("MainWindow", "Have you finished writing the info.xlsx file?")
        self.Done = QtCore.QCoreApplication.translate("MainWindow", "Done")
        self.Y_3 = QtCore.QCoreApplication.translate("MainWindow", "Your PPT is done!")
        self.E = QtCore.QCoreApplication.translate("MainWindow", "Error")
        self.D_I = QtCore.QCoreApplication.translate("MainWindow", "Don't input string!")

    def show2(self):
        self.retranslateUi(self)
        try:
            api_url = "https://api.github.com/repos/YangZhenxun/Auto-make-PPT"
            download_url = "https://github.com/YangZhenxun/Auto-make-PPT/archive/master.zip"

            def get_FileModifyTime(path):
                d = {}
                files = os.listdir(path)
                for file in files:
                    t = os.path.getmtime(path+file)
                    d[file] = t
                return d

            def is_old(old_time: time) -> bool:
                all_info = requests.get(api_url, timeout=5).json()
                new_time = time.mktime(time.strptime(all_info["updated_at"], "%Y-%m-%dT%H:%M:%SZ"))
                if not old_time:
                    old_time = all_info["updated_at"]
                if new_time > old_time:
                    old_time = new_time
                    return True
                else:
                    return False

            def download_newfile(name):
                r = requests.get(download_url, timeout=5)
                name = name.replace('/', '_') + '.zip'
                with open("./" + name, 'wb') as f:
                    f.write(r.content)

            files = get_FileModifyTime('./')
            for i in files:
                print(i, files[i])
                old = is_old(files[i])
            if old:
                QMessageBox.information(self, self.new, self.H_N_V,
                                        QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.Yes)
                rres = QMessageBox.question(self, self.T_D, self.D_3,
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
                if rres == QMessageBox.StandardButton.Yes:
                    download_newfile('Auto-make-PPT')
            else:
                QMessageBox.information(self, self.OK, self.Y_4,
                                        QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.Yes)
        except:
            QMessageBox.critical(self, self.github_E_Title, self.github_E_Text,
                                 QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.Yes)

    def show1(self, MainWindow):
        self.ProgressBar(MainWindow)
        ss = QMessageBox.information(self,self.T_U,self.H_3,QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No,QMessageBox.StandardButton.Yes)
        if ss == QMessageBox.StandardButton.Yes:
            relese_system.system().read_and_make()
            QMessageBox.information(self,self.Done,self.Y_3,QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)

    def ProgressBar(self, MainWindow):
        try:
            integer = int(self.lineEdit.text())
        except:
            QMessageBox.critical(MainWindow, self.E, self.D_I, QMessageBox.StandardButton.Yes,QMessageBox.StandardButton.Yes)
        else:
            self.progressBar.setMaximum(integer)
            for i in range(1,integer + 1):
                self.progressBar.setValue(i)
                time.sleep(1)

    def show3(self):
        self.to_en_US()
        relese_system.system().write_en_US()

    def show4(self):
        self.to_zh_Hans_CN()
        relese_system.system().write_zh_Hans_CN()

    def to_en_US(self):
        self.trans.load("./en-US")
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)

    def to_zh_Hans_CN(self):
        self.trans.load("./zh-Hans-CN")
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)


    def to_find(self):
        global ah
        for find_dirs,dirs,files in os.walk("D:\\"):
            print(dirs)
            if "info.xlsx" in files:
                ah = find_dirs
                return ah
            else:
                self.again()

    def again(self):
        global ah
        for find_dirs, dirs, files in os.walk("C:\\"):
            print(dirs)
            if "info.xlsx" in files:
                ah = find_dirs
                print(dirs)
                return ah
            else:
                return False

    def load_language(self):
        if not os.path.isfile("./info_server.json"):
            with open("./info_server.json","w") as f:
                json.dump({"APP":"Simple PPT","version":"v0.0.1","language":False},f)
        else:
            with open("info_server.json") as f:
                l = json.load(f)
                jl = json.dumps(l)
                lj = json.loads(jl)

                if lj["language"] == "en-US":
                    self.to_en_US()
                elif lj["language"] == "zh-Hans-CN":
                    self.to_zh_Hans_CN()
                else:
                    self.to_en_US()


def __main__():
    app = QApplication(sys.argv)
    main = Ui_MainWindow()
    relese_system.system().make_excel()
    main.to_find()
    main.load_language()
    main.show()
    QMessageBox.information(main, "info.xlsx", QtCore.QCoreApplication.translate("context(Why?)","The info.xlsx file is in %s and info.xlsx is done.")% ah)
    sys.exit(app.exec())

if __name__ == '__main__':
    __main__()
