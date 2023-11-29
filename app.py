import sys
from PyQt5 import QtWidgets
from MainWindowUI import Ui_MainWindow
from Controller import MainController


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    mainController = MainController(ui)
    mainController.adjust_mainWindow()

    MainWindow.show()
    sys.exit(app.exec_())