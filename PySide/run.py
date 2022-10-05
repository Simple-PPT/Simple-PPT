import os
import sys
from ui_NoDone import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from requests import session
import webbrowser
import requests
import lxml
from bs4 import BeautifulSoup
import fake_useragent

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.msgabout = QCoreApplication.translate("about", u"<h2>Simple PPT</h2>version:0.0.2<br/>It can make a PPT for you.<br/>More see:<a href=https://github.com/Simple-PPT/Simple-PPT>Github</a>", None)
        self.version = 0.001
        self.session = session()
        self.ua = fake_useragent.UserAgent()

    def ShowAbout(self):
        QMessageBox.about(self, "About Simple PPT 0.0.2", self.msgabout)

    def OpenFeedback(self):
        webbrowser.open_new("https://github.com/Simple-PPT/Simple-PPT/issues/new")

    def checkupdate(self):
        newversion = self.session.get('https://api.github.com/repos/Simple-PPT/Simple-PPT/releases/latest').json()["tag_name"]
        try:
            name = float(newversion)
        except Exception as e:
            QMessageBox.critical(self, QCoreApplication.translate("MessageBox", u"Error", None), QCoreApplication.translate("MessageBox", u"Error:<br/>%s<br/><br/><a href=https://github.com/Simple-PPT/Simple-PPT/issues/new>Feedback Error</a>", None)%e, QMessageBox.Yes)
        else:
            if name > self.version:
                to_update = QMessageBox.question(self, QCoreApplication.translate("MessageBox", u"New version", None), QCoreApplication.translate("MessageBox", u"Find a new version:%d.\nWould you like to update?", None)% name, buttons=QMessageBox.Yes|QMessageBox.No, defaultButton=QMessageBox.Yes)
                if to_update == QMessageBox.Yes:
                    req = self.session.get("https://github.com/Simple-PPT/Simple-PPT/releases/tag/%s"%newversion, headers={"User-Agent":self.ua.random})
                    bs = BeautifulSoup(req)
                    so = bs.find()

            else:
                QMessageBox.information(self, QCoreApplication.translate("MessageBox", u"No new version", None), QCoreApplication.translate("MessageBox", u"Your version is latest."), QMessageBox.Yes)
    def chagefile(self):
        filePath, filetype = QFileDialog.getOpenFileName(self, QCoreApplication.translate("QFileDialog", u"Open a file", None), r"c:\\", QCoreApplication.translate("QFileDialog", u"Documentation(*.docx *.md)", None))
        if filePath == None or filePath == "":
            pass
        else:
            if os.path.isfile(filePath):
                pass
            else:
                QMessageBox.warning(self, QCoreApplication.translate("MessageBox", u"wrong file path", None), QCoreApplication.translate("MessageBox",u"The file's path is wrong!", None), QMessageBox.Yes)

    def titlestyle(self):
        pass

    def textstyle(self):
        pass

    def CreatPPT(self,titlesyle, textstyle):
        pass

def main():
    app = QApplication()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

main()
