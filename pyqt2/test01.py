from pyqt2.untitled import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import sys
if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    # window.resize(400, 200)
    mainWindow.show()

    sys.exit(app.exec_())