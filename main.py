import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from MainWindow import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

    def btn_FaceCollection_onClicked(self):
        self.stackedWidget.setCurrentIndex(0)
        pass

    def btn_Train_onClicked(self):
        self.stackedWidget.setCurrentIndex(1)
        pass

    def btn_Encrypt_onClicked(self):
        self.stackedWidget.setCurrentIndex(2)
        pass

    def btn_Decrypt_onClicked(self):
        self.stackedWidget.setCurrentIndex(3)
        pass

    def btn_Detect_onClicked(self):
        self.stackedWidget.setCurrentIndex(4)
        pass


if __name__=='__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())