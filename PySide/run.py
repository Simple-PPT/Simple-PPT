import os
from subprocess import Popen
import sys
from ui_NoDone import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from requests import *
import webbrowser
import platform
from bs4 import BeautifulSoup
import fake_useragent
import docx

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.msgabout = QCoreApplication.translate("about", u"<h2>Simple PPT</h2>version:0.0.2<br/>It can make a PPT for you.<br/>More see:<a href=https://github.com/Simple-PPT/Simple-PPT>Github</a>", None)
        self.version = 0.0
        self.session = session()
        self.ua = fake_useragent.UserAgent()
        self.arch, self.exe = platform.architecture()

    def ShowAbout(self):
        QMessageBox.about(self, "About Simple PPT 0.0.2", self.msgabout)

    def OpenFeedback(self):
        webbrowser.open_new("https://github.com/Simple-PPT/Simple-PPT/issues/new")

    def checkupdate(self):
        newversion = self.session.get('https://api.github.com/repos/Simple-PPT/Simple-PPT/releases/latest').json()
        tagnewversion = newversion["tag_name"]
        name = newversion["name"]
        try:
            tagname = float(newversion["tag_name"])
        except Exception as e:
            QMessageBox.critical(self, QCoreApplication.translate("MessageBox", u"Error", None), QCoreApplication.translate("MessageBox", u"Error:<br/>%s<br/><br/><a href=https://github.com/Simple-PPT/Simple-PPT/issues/new>Feedback Error</a>", None)%e, QMessageBox.Ok)
        else:
            if tagname > self.version:
                to_update = QMessageBox.question(self, QCoreApplication.translate("MessageBox", u"New version", None), QCoreApplication.translate("MessageBox", u"Find a new version:%s.\nWould you like to update?", None)% tagnewversion, buttons=QMessageBox.Yes|QMessageBox.No, defaultButton=QMessageBox.Yes)
                if to_update == QMessageBox.Yes:
                    print(self.arch)
                    if self.arch == '64bit':
                        try:
                            req = self.session.get("https://github.com/Simple-PPT/Simple-PPT/releases/download/%s/Simple-PPT_%s_x64_Setup.exe"%(tagnewversion, name), headers={"User-Agent":self.ua.random}, stream=True)
                        except exceptions.ConnectTimeout or exceptions.ReadTimeout or exceptions.ConnectionError:
                            QMessageBox.warning(self, QCoreApplication.translate("MessageBox", u"Download time out", None), QCoreApplication.translate("MessageBox", u"Download time out.</br>Please try again.", None), QMessageBox.Ok)
                        else:
                            if req.status_code == 200:
                                downloadpath = os.path.basename("https://github.com/Simple-PPT/Simple-PPT/releases/download/%s/Simple-PPT_%s_x64_Setup.exe"%(tagnewversion, name))
                                with open(downloadpath, 'wb') as f:
                                    for i in req.iter_content(1024):
                                        if i:
                                            f.write(i)
                                downloadfilefilepath = os.path.realpath(downloadpath)
                                DFFP = downloadfilefilepath
                                Popen(DFFP)
                            else:
                                QMessageBox.critical(self, QCoreApplication.translate("MessageBox", "Error", None), QCoreApplication.translate("MessageBox", "Error:<br/>We don't know why, error code %s.<br/><br/><a href=https://github.com/Simple-PPT/Simple-PPT/issues/new>Feedback Error</a>", None)%req.status_code, QMessageBox.Ok)

                    elif self.arch == '32bit':
                        try:
                            req = self.session.get("https://github.com/Simple-PPT/Simple-PPT/releases/download/%s/Simple-PPT_%s_x32_Setup.exe"%(tagnewversion, name), headers={'User-Agent':self.ua.random}, stream=True)
                        except exceptions.ConnectTimeout or exceptions.ReadTimeout or exceptions.ConnectionError:
                            QMessageBox.warning(self, QCoreApplication.translate("MessageBox", u"Download time out", None), QCoreApplication.translate("MessageBox", u"Download time out.</br>Please try again.", None), QMessageBox.Ok)
                        else:
                            if req.status_code == 200:
                                downloadpath = os.path.basename("https://github.com/Simple-PPT/Simple-PPT/releases/download/%s/Simple-PPT_%s_x32_Setup.exe"%(tagnewversion, name))
                                with open(downloadpath, 'wb') as f:
                                    for i in req.iter_content(1024):
                                        if i:
                                            f.write(i)
                                downloadfilefilepath = os.path.realpath(downloadpath)
                                DFFP = downloadfilefilepath
                                Popen(DFFP)
                            else:
                                QMessageBox.critical(self, QCoreApplication.translate("MessageBox", "Error", None), QCoreApplication.translate("MessageBox", "Error:<br/>We don't know why, error code %s.<br/><br/><a href=https://github.com/Simple-PPT/Simple-PPT/issues/new>Feedback Error</a>", None)%req.status_code, QMessageBox.Ok)
            else:
                QMessageBox.information(self, QCoreApplication.translate("MessageBox", u"No new version", None), QCoreApplication.translate("MessageBox", u"Your version is latest."), QMessageBox.Yes)
    def chagefile(self):
        filePath, filetype = QFileDialog.getOpenFileName(self, QCoreApplication.translate("QFileDialog", u"Open a file", None), r"c:\\", QCoreApplication.translate("QFileDialog", u"Documentation(*.docx *.md)", None))
        if filePath == None or filePath == "":
            pass
        else:
            if os.path.isfile(filePath):
                if filePath.endswith(".docx"):
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
