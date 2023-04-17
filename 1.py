'''
Integrante : Nicolas Aberto Vega Diaz
Asignatura Taller Programacion Aplicada

'''


import sys # sys,proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete.

import numpy as np
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtWidgets import QApplication,QMainWindow, QPushButton,QLabel

# UNa clase que define el comportamiento de una ventata

class MainWindow(QMainWindow):# hereda QMainWindow, se utiza para crear la ventana principal

    def __init__(self):
        super().__init__() # permitee inincialiszar los atributos de la clase QMainWindow
       

        self.setWindowTitle("Generar de numeros aleatorios ") # Titulo la clase de la ventana
        self.setGeometry(100,100,300,200) # posicion,y tamaño de la ventana principal
        

        self.label=QLabel(self) # crea una etiqueta, y la asigna como widget a la ventana principal
        self.label.setGeometry(50,50,200,30)



        self.button= QPushButton("Presioname ",self) # crea un botom en la ventana principal
        self.button.setGeometry(100,100,100,30) #posicion y tamaños de la ventana
        self.button.clicked.connect(self.reaccionar) # conecta la señal cliscked del botom a la funcion reaccionar



    # se ejecuta al precinar clic en el botom
    def reaccionar(self):

        # genera un numero seudoaleatorio entre o y 100
        num= np.random.randint(0,100)
        
        # esstablece el texto de la etiqueta con el numero generado
        self.label.setText(f"El numero aleatorio es : {num}")


if __name__ == "__main__":
    app=QApplication(sys.argv)

    Window= MainWindow()
    Window.show() # obligatorio

    sys.exit(app.exec())