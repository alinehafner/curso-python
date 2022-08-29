import sys
from random import choice
from ms.sq import *
from PyQt5.QtWidgets import QApplication, QMainWindow


class SeqNum(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.inputMin.setText('0')
        self.inputMax.setText('60')
        self.inputNumSeq.setText('6')
        self.btnCalcular.clicked.connect(self.calcular)

    def comb(self,numeros,quantidade,por_seq=6,inicial=0,final=60):
        entrada = sorted(list(map(int, numeros.split())))
        totais = [int(str(i)+str(entrada[z])) for i in entrada for z in range(len(entrada))
                  if not int(str(i)+str(entrada[z])) == 0
                  if not int(str(i)+str(entrada[z])) > final
                  if not int(str(i)+str(entrada[z])) < inicial]
        final = []
        a = ''

        for y in range(int(quantidade)):
            copia = totais.copy()
            jogos = []
            for z in range(por_seq):
                ran = choice(copia)
                copia.remove(ran)
                jogos += [ran]
            final += [sorted(jogos)]
            a += str(sorted(jogos)) + '\n'

        self.textEdit.setText(a)

    def calcular(self):
        num = self.inputNumeros.text()
        seq = self.inputSequencias.text()
        minimo = int(self.inputMin.text())
        maximo = int(self.inputMax.text())
        num_seq = int(self.inputNumSeq.text())
        self.comb(num,seq,num_seq,minimo,maximo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = SeqNum()
    app.show()
    qt.exec_()
