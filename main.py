import sys
from PyQt6.QtWidgets import QApplication
from mvc_view import View
from mvc_controller import Controller


'''
Main Program
'''
if __name__ == "__main__":
    # UI intialize
    app = QApplication(sys.argv)
    # generate main View objectpip up
    view = View()
    # Let Controller setup the Logic flow
    mainController = Controller(view=view)

    sys.exit(app.exec())  # loop in ui event
