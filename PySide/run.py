import sys
from ui_NoDone import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from requests import session
import webbrowser

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.msgabout = QCoreApplication.translate("about", u"<h2>Simple PPT</h2>version:0.0.2<br/>It can make a PPT for you.<br/>More see:<a href=https://github.com/Simple-PPT/Simple-PPT>Github</a>", None)
        self.version = 0.02
        self.session = session()

    def ShowAbout(self):
        QMessageBox.about(self, "About Simple PPT 0.0.2", self.msgabout)

    def OpenFeedback(self):
        webbrowser.open_new("https://github.com/Simple-PPT/Simple-PPT/issues/new")

    def checkupdate(self):
        newversion = self.session.get('https://api.github.com/repos/Simple-PPT/Simple-PPT/releases/latest').json()["tag_name"]
        try:
            name = int(newversion)
        except Exception as e:
            QMessageBox.critical(self, QCoreApplication.translate("MessageBox", "Error", None), QCoreApplication.translate("MessageBox", f"Error:<br/>{e}<br/><br/><a href=https://github.com/Simple-PPT/Simple-PPT/issues/new>Feedback Error</a>", None), QMessageBox.Yes)
        else:
            if name > self.version:
                QMessageBox.question(self, QCoreApplication.translate("MessageBox","New version", None), QCoreApplication.translate("MessageBox", "Find a new version:%d.\nWould you like to update?", None)% name, QMessageBox.Yes, QMessageBox.No)
            else:
                QMessageBox.information(self, QCoreApplication.translate("MessageBox","No new version", None), QCoreApplication.translate("MessageBox", "Your version is latest."), QMessageBox.Yes)

    def chagefile(self):
        pass

    def titlestyle(self):
        pass

    def textstyle(self):
        pass

    def CreatPPT(self):
        pass

def main():
    app = QApplication()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

main()
