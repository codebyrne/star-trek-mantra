# It was necessary to run:
# apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
# To get the QT application to run

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import startrekmantra

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Engage!")
        self.text = QtWidgets.QLabel("Click the button to generate a Trekky response",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(startrekmantra.get_random_response(startrekmantra.generate_response_list()))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(600, 300)
    widget.show()

    sys.exit(app.exec())