from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from data_reader import Ui_MainWindow  # importing our generated file

import sys
import json


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint | Qt.WindowMinMaxButtonsHint)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        # declaring variables which will be used while running of program
        self.json_data = None
        self.current_index = -1
        self.labels = []
        self.file_path = None
        self.html_template = "{}"

        # declaring connections of objects to functions
        self.ui.actionOpen.triggered.connect(self.triggered_action_open)

        self.ui.openFileBtn.clicked.connect(self.triggered_action_open)

        self.ui.actionReset.triggered.connect(self.triggered_action_reset)

        self.ui.actionExit.triggered.connect(self.triggered_action_exit)

        self.ui.nextBtn.clicked.connect(self.next_entry)

        self.ui.previousBtn.clicked.connect(self.previous_entry)

        self.ui.comboBox.currentIndexChanged.connect(self.open_file)

    def triggered_action_exit(self):
        pass

    def triggered_action_open(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose Hackerrank Submission Extracted Json", "", "Json Files (*.json)", options=options)

        if self.file_path is not None:
            with open(self.file_path, "r") as file:
                self.json_data = json.load(file)

        for entry in self.json_data:
            self.labels.append(entry['label'])
        self.clean_labels()
        self.ui.fileNameTextBox.setText(str(self.file_path))
        self.ui.comboBox.addItems(self.labels)
        #self.open_file()

    def clean_labels(self):
        temp_dict= dict()
        final = []
        for entry in self.labels:
            if entry in temp_dict:
                temp_dict[entry] += 1
                final.append("{} - {}".format(entry,temp_dict[entry]))
            else:
                temp_dict[entry] = 0
                final.append(entry)
        self.labels = final

    def open_file(self):
        self.current_index = self.ui.comboBox.currentIndex()

        if self.current_index == 0:
            self.ui.previousBtn.setDisabled(True)
        else:
            self.ui.previousBtn.setDisabled(False)

        if self.current_index == len(self.labels)-1:
            self.ui.nextBtn.setDisabled(True)
        else:
            self.ui.nextBtn.setDisabled(False)

        self.ui.statementWebView.setHtml(self.html_template.format(self.json_data[self.current_index]['statement']))
        self.ui.solutionWebView.setHtml(self.html_template.format(self.json_data[self.current_index]['code']))

    def triggered_action_reset(self):
        pass

    def next_entry(self):
        index = int(self.ui.comboBox.findText(str(self.labels[int(self.current_index)+1])))
        print(self.current_index)
        print(self.labels[self.current_index])
        print(index)
        self.ui.comboBox.setCurrentIndex(index)


    def previous_entry(self):
        pass
        #self.ui.comboBox.setCurrentIndex(self.ui.comboBox.findData(self.labels[self.current_index-1]))

    def goto_entry(self):
        pass



app = QtWidgets.QApplication([])

application = Window()

application.show()

sys.exit(app.exec())