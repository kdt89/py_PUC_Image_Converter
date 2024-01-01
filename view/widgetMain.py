from view.qt_ui.main_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow


# class for object Main window of application
class WidgetMain(QMainWindow):

    # message = ""

    # update status bar message
    def updateSttBar(self, message: str):
        self.ui.statusbar.showMessage(message, 1000)
        self.ui.statusbar.repaint()


    def updateMessage(self, message: str):
        self.ui.txtbrowserOperationMessage.append(message)
        self.ui.txtbrowserOperationMessage.repaint()


    def __init__(self):
        super(WidgetMain, self).__init__()
        # GUI Main form
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)