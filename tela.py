from PyQt6 import uic, QtWidgets
import sqlite3


def chamar_segunda_tela():
    nomeusuairo = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    if nomeusuairo == "teste" and senha == "123":
        primeira_tela.close()
        segunda_tela.show()
    else:
        print("dados incorretos")





app=QtWidgets.QApplication([])
primeira_tela = uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
primeira_tela.pushButton.clicked.connect(chamar_segunda_tela)
# segunda_tela.pushButton.clicked.connect(checar_senha)

primeira_tela.show()
app.exec()
