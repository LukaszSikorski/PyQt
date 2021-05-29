from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QDialogButtonBox
import  sys
import string
import copy

app= QApplication([])

# window= QWidget()
# window.setWindowTitle("TEST")
# window.setGeometry(400,400,400,300)
# mess= QLabel("Napis",parent=window)
# mess.move(60,15)
# layout= QHBoxLayout()
# layout.addWidget(QPushButton("Left"))
# layout.addWidget(QPushButton("Central"))
# layout.addWidget(QPushButton("Right"))
# window.setLayout(layout)
# layout.
# window.show()

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,100,300)
        self.setWindowTitle("Moje okno")
        self._QHBox= QVBoxLayout()
        self._display= QLineEdit()
        self._display.setFixedSize(300,35)
        self._keys:dict=dict()
        self._QHBox.addWidget(self._display)
        self._createButtons()
        self._functionsToButtons()
        self.setLayout(self._QHBox)
        self.show()

    def _createButtons(self):
        widget= QGridLayout()
        keys:dict = {
            "1":(0,0),
            "2":(0,1),
            "3":(0,2),
            "4":(1,0),
            "5":(1,1),
            "6":(1,2),
            "7":(2,0),
            "8":(2,1),
            "9":(2,2),
            "0":(3,0),
            "00":(3,1),
            ".":(3,2),
            "+":(0,4),
            "-":(1,4),
            "/":(2,4),
            "*":(3,4),
            "%":(0,5),
            "^":(0,5),
            "(":(1,5),
            ")":(2,5),
            "=":(3,5)
        }

        for key,value in keys.items():
            self._keys[key]= QPushButton(key)
            self._keys[key].setFixedSize(50,50)
            widget.addWidget(self._keys[key],*value)

        self._QHBox.addLayout(widget)


    def addNumberToDisplay(self,number):
        print(number)
        text= self._display.text()
        text += str(number)
        self._display.setText(text)

    def _functionsToButtons(self):
        for key,value in self._keys.items():
            if key.isnumeric():
                print(key)
                tmp=str(key)
                lam= copy.deepcopy( lambda : self.addNumberToDisplay(tmp))
                self._keys[tmp].clicked.connect(lam)

win= MainWindow()
sys.exit(app.exec_())

