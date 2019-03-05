from PyQt5 import QtWidgets

from .calculator import CalculatorUi  # importing our generated file

import sys


class mywindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(mywindow, self).__init__()

        self.ui = CalculatorUi()

        self.ui.setupUi(self)


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())