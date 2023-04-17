

import sys

from PyQt6.QtWidgets import QApplication,QLabel,QMainWindow,QLineEdit,QPushButton
from PyQt6.QtWidgets import QApplication,QLabel,QMainWindow,QLineEdit,QPushButton


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        self.setWindowTitle("Verificar si es un numero primo")
        self.setGeometry(270,270,300,300)


        self.label_text = QLabel("Ingresa un numero",self)
        self.label_text.setGeometry(70,30,100,50)

        self.num_input= QLineEdit(self)
        self.num_input.setGeometry(70,100,100,50)
        self.num_input.textChanged(self.convertir_numero)
      
        self.butom=QPushButton("Presiona",self)
        self.butom.setGeometry(70,200,100,50)
        
        self.butom.clicked.connect(self.primo)

        self.label_output = QLabel(self)
        self.label_output.setGeometry(70,250,100,50)

    def convertir_numero(self):
        try:
            # Convertir el texto a un número y mostrarlo en la consola
            num = float(self.num_input.text())
            print(num)
        except ValueError:
            # Si no se puede convertir el texto a un número, mostrar un mensaje de error
            print("No se puede convertir el texto a un número")



    def primo(self):
        num=self.num_input()
        i=0
        for i in range(1,num):
            if num%i == 0:
                return self.label_output.setText("El numero no es primo")
            else:
                return self.label_output.setText("El numero es primo")

                
if __name__=="__main__":
    app=QApplication(sys.argv)
    Window=MainWindow()
    Window.show()

    sys.exit(app.exec())

        

                

