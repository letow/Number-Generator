# -*- coding: utf-8 -*-

import sys, random
from PyQt5.QtWidgets import QWidget, QPushButton, QInputDialog, QApplication, QLabel

#класс генератора
class Generator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # настройка интерфейса
    def initUI(self):
        # и объявление пары переменных
        self.b = []
        self.i = 0
        self.lbl1 = QLabel('', self)
        self.lbl1.move(190, 25)
        #self.lbl1.adjustSize()
        self.lbl11 = QLabel('Entered number:', self)
        self.lbl11.move(100, 25)
        #self.lbl11.adjustSize()
        self.lbl2 = QLabel('', self)
        self.lbl2.move(205, 65)
        self.lbl22 = QLabel('Generated number:', self)
        self.lbl22.move(100, 65)
        self.lbl3 = QLabel('', self)
        self.lbl3.move(100, 100)

        self.btn1 = QPushButton('Enter number', self)
        self.btn1.move(20, 20)
        self.btn1.clicked.connect(self.showDialog)
        self.btn2 = QPushButton('Generate', self)
        self.btn2.move(20, 60)
        self.btn2.setEnabled(False)
        self.btn2.clicked.connect(self.bongiorno)

        self.setGeometry(800, 400, 290, 150)
        self.setWindowTitle('Number Generator')
        self.show()
    # диалоговое окно, спрашивающее число у юзера
    def showDialog(self):
        number, ok = QInputDialog.getInt(self, 'Input Dialog', 'Enter your number:')
        if ok:
            self.lbl1.setText(str(number))
            self.lbl1.adjustSize()
            self.btn2.setEnabled(True)
            self.b.clear()
            self.i = 0
            self.lbl3.clear()


    # ф-ция генерирующая числа из диапазона и проверяющая число на "новизну"
    def bongiorno(self):
        number = int(self.lbl1.text())
        a = random.randint(1, number)
        if self.i < number:
            while True:
                if a not in self.b:
                    self.lbl2.setText(str(a))
                    self.b.append(a)
                    self.lbl2.adjustSize()
                    #self.lbl3.setText(str(self.b))
                    #self.lbl3.adjustSize()
                    break
                else:
                    while a in self.b:
                        a = random.randint(1, number)
                    self.lbl2.setText(str(a))
                    self.b.append(a)
                    self.lbl2.adjustSize()
                    #self.lbl3.setText(str(self.b))
                    #self.lbl3.adjustSize()
                    break
            self.i += 1
        else:
            self.lbl3.setText('Numbers are over!\nEnter new number')
            self.lbl3.adjustSize()
            self.btn2.setEnabled(False)
            self.i = 0
            self.b.clear()
# инициализация
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Generator()
    sys.exit(app.exec_())
