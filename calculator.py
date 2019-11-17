from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QTextEdit
from PyQt5.QtGui import QFont, QIcon
import sys

saveInput = ''

class CalculatorApp(QWidget):
	def __init__(self):
		super(CalculatorApp, self).__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(400, 400, 350, 400)
		self.setWindowIcon(QIcon('calc.ico'))
		self.setWindowTitle('Calculator')
		self.setStyleSheet('background-color: white')

		grid = QGridLayout()

		self.disp = QTextEdit()
		grid.addWidget(self.disp, 1, 0, 1, 4)
		self.disp.setReadOnly(True)
		self.disp.setText(saveInput)
		self.disp.setFont(QFont("Arial", 40))
		self.disp.setGeometry(10, 10, 340, 200)
		self.disp.setStyleSheet('background-color: #f1f3f4; border: 1px solid #b3b3b3; border-radius: 10px')

		leftBracketButton = QPushButton('(')
		grid.addWidget(leftBracketButton, 2, 0)
		leftBracketButton.setMinimumSize(82, 48)
		leftBracketButton.setFont(QFont("Arial", 13))
		leftBracketButton.setStyleSheet('background-color: #dfe1e5; border-radius: 10px')
		leftBracketButton.clicked.connect(lambda: self.calculate('('))

		rightBracketButton = QPushButton(')')
		grid.addWidget(rightBracketButton, 2, 1)
		rightBracketButton.setMinimumSize(82, 48)
		rightBracketButton.setFont(QFont("Arial", 13))
		rightBracketButton.setStyleSheet('background-color: #dfe1e5; border-radius: 10px')
		rightBracketButton.clicked.connect(lambda: self.calculate(')'))

		powButton = QPushButton('x²')
		grid.addWidget(powButton, 2, 2)
		powButton.setMinimumSize(82, 48)
		powButton.setFont(QFont("Arial", 13))
		powButton.setStyleSheet('background-color: #dfe1e5; border-radius: 10px')
		powButton.clicked.connect(lambda: self.calculate('pow'))

		deleteButton = QPushButton('AC')
		grid.addWidget(deleteButton, 2, 3)
		deleteButton.setMinimumSize(82, 48)
		deleteButton.setFont(QFont("Arial", 13))
		deleteButton.setStyleSheet('background-color: #dfe1e5; border-radius: 10px')
		deleteButton.clicked.connect(lambda: self.calculate('AC'))

		sevenButton = QPushButton('7')
		grid.addWidget(sevenButton, 3, 0)
		sevenButton.setMinimumSize(82, 48)
		sevenButton.setFont(QFont("Arial", 13))
		sevenButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		sevenButton.clicked.connect(lambda: self.calculate('7'))


		eightButton = QPushButton('8')
		grid.addWidget(eightButton, 3, 1)
		eightButton.setMinimumSize(82, 48)
		eightButton.setFont(QFont("Arial", 13))
		eightButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		eightButton.clicked.connect(lambda: self.calculate('8'))

		nineButton = QPushButton('9')
		grid.addWidget(nineButton, 3, 2)
		nineButton.setMinimumSize(82, 48)
		nineButton.setFont(QFont("Arial", 13))
		nineButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		nineButton.clicked.connect(lambda: self.calculate('9'))

		divisionButton = QPushButton('÷')
		grid.addWidget(divisionButton, 3, 3)
		divisionButton.setMinimumSize(82, 48)
		divisionButton.setFont(QFont("Arial", 15))
		divisionButton.setStyleSheet('background-color: #dfe1e5; border-radius: 10px')
		divisionButton.clicked.connect(lambda: self.calculate('/'))

		fourButton = QPushButton('4')
		grid.addWidget(fourButton, 4, 0)
		fourButton.setMinimumSize(82, 48)
		fourButton.setFont(QFont("Arial", 13))
		fourButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		fourButton.clicked.connect(lambda: self.calculate('4'))

		fiveButton = QPushButton('5')
		grid.addWidget(fiveButton, 4, 1)
		fiveButton.setMinimumSize(82, 48)
		fiveButton.setFont(QFont("Arial", 13))
		fiveButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		fiveButton.clicked.connect(lambda: self.calculate('5'))

		sixButton = QPushButton('6')
		grid.addWidget(sixButton, 4, 2)
		sixButton.setMinimumSize(82, 48)
		sixButton.setFont(QFont("Arial", 13))
		sixButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		sixButton.clicked.connect(lambda: self.calculate('6'))

		multipButton = QPushButton('×')
		grid.addWidget(multipButton, 4, 3)
		multipButton.setMinimumSize(82, 48)
		multipButton.setFont(QFont("Arial", 15))
		multipButton.setStyleSheet('background-color: #dfe1e5; border-radius: 10px')
		multipButton.clicked.connect(lambda: self.calculate('*'))

		oneButton = QPushButton('1')
		grid.addWidget(oneButton, 5, 0)
		oneButton.setMinimumSize(82, 48)
		oneButton.setFont(QFont("Arial", 13))
		oneButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		oneButton.clicked.connect(lambda: self.calculate('1'))

		twoButton = QPushButton('2')
		grid.addWidget(twoButton, 5, 1)
		twoButton.setMinimumSize(82, 48)
		twoButton.setFont(QFont("Arial", 13))
		twoButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		twoButton.clicked.connect(lambda: self.calculate('2'))

		threeButton = QPushButton('3')
		grid.addWidget(threeButton, 5, 2)
		threeButton.setMinimumSize(82, 48)
		threeButton.setFont(QFont("Arial", 13))
		threeButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		threeButton.clicked.connect(lambda: self.calculate('3'))

		minusButton = QPushButton('-')
		grid.addWidget(minusButton, 5, 3)
		minusButton.setMinimumSize(82, 48)
		minusButton.setFont(QFont("Arial", 15))
		minusButton.setStyleSheet('background-color: #dfe1e5; border-radius: 10px')
		minusButton.clicked.connect(lambda: self.calculate('-'))

		zeroButton = QPushButton('0')
		grid.addWidget(zeroButton, 6, 0)
		zeroButton.setMinimumSize(82, 48)
		zeroButton.setFont(QFont("Arial", 13))
		zeroButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		zeroButton.clicked.connect(lambda: self.calculate('0'))

		pointButton = QPushButton('.')
		grid.addWidget(pointButton, 6, 1)
		pointButton.setMinimumSize(82, 48)
		pointButton.setFont(QFont("Arial", 15))
		pointButton.setStyleSheet('background-color: #f1f3f4; border-radius: 10px')
		pointButton.clicked.connect(lambda: self.calculate('.'))

		resultButton = QPushButton('=')
		grid.addWidget(resultButton, 6, 2)
		resultButton.setMinimumSize(82, 48)
		resultButton.setStyleSheet('background-color: #c33357; color: white; border: 1px; border-radius: 10px')
		resultButton.setFont(QFont("Arial", 15))
		resultButton.clicked.connect(lambda: self.calculate('='))

		plusButton = QPushButton('+')
		grid.addWidget(plusButton, 6, 3)
		plusButton.setMinimumSize(82, 48)
		plusButton.setFont(QFont("Arial", 15))
		plusButton.setStyleSheet('background-color: #dfe1e5; border-radius: 10px')
		plusButton.clicked.connect(lambda: self.calculate('+'))

		self.setLayout(grid)

	def calculate(self, symbol):
		global saveInput
		if symbol == 'AC':
			saveInput = ''
		elif symbol == 'pow':
			try: saveInput = str(pow(int(saveInput), 2))
			except: saveInput = ''
		elif symbol != '=':
			saveInput += symbol
		else:
			try: saveInput = str(eval(saveInput))
			except: saveInput = ''
		self.disp.setText(saveInput)
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = CalculatorApp()
	win.show()
	sys.exit(app.exec_())