from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt


class CalculatorApp(QWidget):
    def __init__(self):
        super(CalculatorApp, self).__init__()

        self.initUI()

    def initUI(self):
        self.saveInput = ''
        self.style = '''

            CalculatorApp {
                background-color: white;
                font-family: sans-serif;
            }

            #mainButton {
                background-color: #f1f3f4;
                border-radius: 10px;
                font-size: 13pt;
            }

            #mainButton:hover {
                background-color: #d4dadd;
            }

            #minorButton {
                background-color: #dfe1e5;
                border-radius: 10px;
                font-size: 13pt;
            }

            #minorButton:hover {
                background-color: #c7cad1;
            }

            #resultButton {
                background-color: #c33357;
                color: white;
                border: 1px;
                border-radius: 10px;
                font-size: 15pt;
                font-weight: bold;
            }

            #resultButton:hover {
                background-color: #a22a48;
            }

            #display {
                background-color: #f1f3f4;
                border: 1px solid #b3b3b3;
                border-radius: 10px;
                font-size: 40pt;
                color: #a22a48;
            }

        '''

        self.setGeometry(400, 400, 350, 400)
        self.setWindowIcon(QIcon('calc.ico'))
        self.setWindowTitle('Calculator')
        self.setStyleSheet(self.style)

        self.grid = QGridLayout()

        self.disp = QLineEdit()
        self.grid.addWidget(self.disp, 1, 0, 1, 4)
        self.disp.setMinimumSize(330, 100)
        self.disp.setObjectName('display')
        self.disp.setAlignment(Qt.AlignRight)
        self.disp.setText(self.saveInput)
        self.disp.setReadOnly(True)

        self.leftBracketButton = QPushButton('(')
        self.grid.addWidget(self.leftBracketButton, 2, 0)
        self.leftBracketButton.setMinimumSize(82, 48)
        self.leftBracketButton.setObjectName('minorButton')
        self.leftBracketButton.clicked.connect(lambda: self.calculate('('))

        self.rightBracketButton = QPushButton(')')
        self.grid.addWidget(self.rightBracketButton, 2, 1)
        self.rightBracketButton.setMinimumSize(82, 48)
        self.rightBracketButton.setObjectName('minorButton')
        self.rightBracketButton.clicked.connect(lambda: self.calculate(')'))

        self.powButton = QPushButton('x²')
        self.grid.addWidget(self.powButton, 2, 2)
        self.powButton.setMinimumSize(82, 48)
        self.powButton.setObjectName('minorButton')
        self.powButton.clicked.connect(lambda: self.calculate('pow'))

        self.deleteButton = QPushButton('AC')
        self.grid.addWidget(self.deleteButton, 2, 3)
        self.deleteButton.setMinimumSize(82, 48)
        self.deleteButton.setObjectName('minorButton')
        self.deleteButton.clicked.connect(lambda: self.calculate('AC'))

        self.sevenButton = QPushButton('7')
        self.grid.addWidget(self.sevenButton, 3, 0)
        self.sevenButton.setMinimumSize(82, 48)
        self.sevenButton.setObjectName('mainButton')
        self.sevenButton.clicked.connect(lambda: self.calculate('7'))

        self.eightButton = QPushButton('8')
        self.grid.addWidget(self.eightButton, 3, 1)
        self.eightButton.setMinimumSize(82, 48)
        self.eightButton.setObjectName('mainButton')
        self.eightButton.clicked.connect(lambda: self.calculate('8'))

        self.nineButton = QPushButton('9')
        self.grid.addWidget(self.nineButton, 3, 2)
        self.nineButton.setMinimumSize(82, 48)
        self.nineButton.setObjectName('mainButton')
        self.nineButton.clicked.connect(lambda: self.calculate('9'))

        self.divisionButton = QPushButton('÷')
        self.grid.addWidget(self.divisionButton, 3, 3)
        self.divisionButton.setMinimumSize(82, 48)
        self.divisionButton.setObjectName('minorButton')
        self.divisionButton.clicked.connect(lambda: self.calculate('/'))

        self.fourButton = QPushButton('4')
        self.grid.addWidget(self.fourButton, 4, 0)
        self.fourButton.setMinimumSize(82, 48)
        self.fourButton.setObjectName('mainButton')
        self.fourButton.clicked.connect(lambda: self.calculate('4'))

        self.fiveButton = QPushButton('5')
        self.grid.addWidget(self.fiveButton, 4, 1)
        self.fiveButton.setMinimumSize(82, 48)
        self.fiveButton.setObjectName('mainButton')
        self.fiveButton.clicked.connect(lambda: self.calculate('5'))

        self.sixButton = QPushButton('6')
        self.grid.addWidget(self.sixButton, 4, 2)
        self.sixButton.setMinimumSize(82, 48)
        self.sixButton.setObjectName('mainButton')
        self.sixButton.clicked.connect(lambda: self.calculate('6'))

        self.multipButton = QPushButton('×')
        self.grid.addWidget(self.multipButton, 4, 3)
        self.multipButton.setMinimumSize(82, 48)
        self.multipButton.setObjectName('minorButton')
        self.multipButton.clicked.connect(lambda: self.calculate('*'))

        self.oneButton = QPushButton('1')
        self.grid.addWidget(self.oneButton, 5, 0)
        self.oneButton.setMinimumSize(82, 48)
        self.oneButton.setObjectName('mainButton')
        self.oneButton.clicked.connect(lambda: self.calculate('1'))

        self.twoButton = QPushButton('2')
        self.grid.addWidget(self.twoButton, 5, 1)
        self.twoButton.setMinimumSize(82, 48)
        self.twoButton.setObjectName('mainButton')
        self.twoButton.clicked.connect(lambda: self.calculate('2'))

        self.threeButton = QPushButton('3')
        self.grid.addWidget(self.threeButton, 5, 2)
        self.threeButton.setMinimumSize(82, 48)
        self.threeButton.setObjectName('mainButton')
        self.threeButton.clicked.connect(lambda: self.calculate('3'))

        self.minusButton = QPushButton('-')
        self.grid.addWidget(self.minusButton, 5, 3)
        self.minusButton.setMinimumSize(82, 48)
        self.minusButton.setObjectName('minorButton')
        self.minusButton.clicked.connect(lambda: self.calculate('-'))

        self.zeroButton = QPushButton('0')
        self.grid.addWidget(self.zeroButton, 6, 0)
        self.zeroButton.setMinimumSize(82, 48)
        self.zeroButton.setObjectName('mainButton')
        self.zeroButton.clicked.connect(lambda: self.calculate('0'))

        self.pointButton = QPushButton('.')
        self.grid.addWidget(self.pointButton, 6, 1)
        self.pointButton.setMinimumSize(82, 48)
        self.pointButton.setObjectName('mainButton')
        self.pointButton.clicked.connect(lambda: self.calculate('.'))

        self.resultButton = QPushButton('=')
        self.grid.addWidget(self.resultButton, 6, 2)
        self.resultButton.setMinimumSize(82, 48)
        self.resultButton.setObjectName('resultButton')
        self.resultButton.clicked.connect(lambda: self.calculate('='))

        self.plusButton = QPushButton('+')
        self.grid.addWidget(self.plusButton, 6, 3)
        self.plusButton.setMinimumSize(82, 48)
        self.plusButton.setObjectName('minorButton')
        self.plusButton.clicked.connect(lambda: self.calculate('+'))

        self.setLayout(self.grid)

    def calculate(self, symbol):
        if symbol == 'AC':
            self.saveInput = ''
        elif symbol == 'pow':
            try:
                self.saveInput = str(pow(int(self.saveInput), 2))
            except:
                self.saveInput = ''
        elif symbol != '=':
            self.saveInput += symbol
        else:
            try:
                self.saveInput = str(eval(self.saveInput))
            except:
                self.saveInput = ''
        self.disp.setText(self.saveInput)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = CalculatorApp()
    win.show()
    sys.exit(app.exec_())
