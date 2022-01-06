import math

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
        QSizePolicy, QToolButton, QWidget)


class Button(QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    NumDigitButtons = 10
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)

        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.pendingPowerOperator = ''

        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.powerSoFar = 0.0
        self.waitingForOperand = True

        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        
        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        self.digitButtons = []
        
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i),
                    self.digitClicked))

        self.pointButton = self.createButton(".", self.pointClicked)
        self.changeSignButton = self.createButton(u"\N{PLUS-MINUS SIGN}",
                self.changeSignClicked)

        self.backspaceButton = self.createButton("Backspace",
                self.backspaceClicked)
        self.clearAllButton = self.createButton("Clear All", self.clearAll)

        self.powerButton = self.createButton("x"+self.get_super("y"),self.xpowerdbyy)
        self.power1yButton = self.createButton(self.get_super("y")+"√x",self.xpowerdby1y)

        self.logButton = self.createButton("log",self.unaryOperatorClicked)
        self.lnButtton = self.createButton("ln",self.unaryOperatorClicked)
        self.factorialButton = self.createButton("x!",self.unaryOperatorClicked)

        self.tanButton = self.createButton("tan",self.unaryOperatorClicked)
        self.cosButton = self.createButton("cos",self.unaryOperatorClicked)
        self.sinButton = self.createButton("sin",self.unaryOperatorClicked)
        self.radButton = self.createButton("rad",self.unaryOperatorClicked)


        self.divisionButton = self.createButton(u"\N{DIVISION SIGN}",
                self.multiplicativeOperatorClicked)
        self.timesButton = self.createButton(u"\N{MULTIPLICATION SIGN}",
                self.multiplicativeOperatorClicked)
        self.minusButton = self.createButton("-", self.additiveOperatorClicked)
        self.plusButton = self.createButton("+", self.additiveOperatorClicked)

    
        self.reciprocalButton = self.createButton("1/x",
                self.unaryOperatorClicked)
        self.equalButton = self.createButton("=", self.equalClicked)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 8)
        mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        

        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            mainLayout.addWidget(self.digitButtons[i], row, column)

        mainLayout.addWidget(self.digitButtons[0], 5, 1)
        mainLayout.addWidget(self.pointButton, 5, 2)
        mainLayout.addWidget(self.changeSignButton, 5, 3)

        mainLayout.addWidget(self.divisionButton, 2, 4)
        mainLayout.addWidget(self.timesButton, 3, 4)
        mainLayout.addWidget(self.minusButton, 4, 4)
        mainLayout.addWidget(self.plusButton, 5, 4)


        mainLayout.addWidget(self.powerButton, 3, 5)
        mainLayout.addWidget(self.power1yButton,2,5)
        mainLayout.addWidget(self.reciprocalButton, 4, 5)
        mainLayout.addWidget(self.equalButton, 5, 5)


        mainLayout.addWidget(self.sinButton,2,6)
        mainLayout.addWidget(self.cosButton,3,6)
        mainLayout.addWidget(self.tanButton,4,6)
        mainLayout.addWidget(self.radButton,5,6)


        mainLayout.addWidget(self.clearAllButton, 2, 7)
        mainLayout.addWidget(self.factorialButton,3,7)
        mainLayout.addWidget(self.logButton,4,7)
        mainLayout.addWidget(self.lnButtton,5,7)

        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator")

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())

        if self.display.text() == '0' and digitValue == 0.0:
            return

        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False

        self.display.setText(self.display.text() + str(digitValue))

    def unaryOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        
        if clickedOperator == u"x\N{SUPERSCRIPT TWO}":
            result = math.pow(operand, 2.0)
        elif clickedOperator == "1/x":
            if operand == 0.0:
                self.abortOperation()
                return

            result = 1.0 / operand
        elif clickedOperator == "sin":
            result = math.sin(math.radians(operand))
            
        elif clickedOperator == "cos":
            result = math.sin(math.radians(operand))
            
        elif clickedOperator == "tan":
            result = math.sin(math.radians(operand))
            
        elif clickedOperator == "rad":
            result = math.radians(operand)

        elif clickedOperator == "x!":
            result = math.factorial(operand)
            
        elif clickedOperator == "ln":
            result = math.log2(operand)
        elif clickedOperator == "log":
            result = math.log10(operand)
        
        self.display.setText(str(result))
        self.waitingForOperand = True

   

    def additiveOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True

    def xpowerdby1y(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingPowerOperator:
            if not self.calculate(operand, self.pendingPowerOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.powerSoFar))
        else:
            self.powerSoFar = operand

        self.pendingPowerOperator = clickedOperator
        self.waitingForOperand = True




    def xpowerdbyy(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingPowerOperator:
            if not self.calculate(operand, self.pendingPowerOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.powerSoFar))
        else:
            self.powerSoFar = operand

        self.pendingPowerOperator = clickedOperator
        self.waitingForOperand = True




    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True

    def equalClicked(self):
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingPowerOperator:
            if not self.calculate(operand, self.pendingPowerOperator):
                self.abortOperation()
                return

            operand = self.powerSoFar
            self.powerSoFar = 0.0
            self.pendingPowerOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    def pointClicked(self):
        if self.waitingForOperand:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False

    def changeSignClicked(self):
        text = self.display.text()
        value = float(text)

        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]

        self.display.setText(text)

    def backspaceClicked(self):
        if self.waitingForOperand:
            return

        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True

        self.display.setText(text)

    def clearAll(self):
        self.powerSoFar = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        self.pendingPowerOperator = ''
        self.display.setText('0')
        self.waitingForOperand = True

    

    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

    def abortOperation(self):
        self.clearAll()
        self.display.setText("####")

    def calculate(self, rightOperand, pendingOperator):
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == u"\N{MULTIPLICATION SIGN}":
            self.factorSoFar *= rightOperand

        elif pendingOperator == self.get_super("y")+"√x":
            self.powerSoFar **= (1/rightOperand)

        elif pendingOperator == "x"+self.get_super("y"):
            self.powerSoFar **= rightOperand
        elif pendingOperator == u"\N{DIVISION SIGN}":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        

        return True

    def get_super(self,x):
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
        super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
        res = x.maketrans(''.join(normal), ''.join(super_s))
        return x.translate(res)
    

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())