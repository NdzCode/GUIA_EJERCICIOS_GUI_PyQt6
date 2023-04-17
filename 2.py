import sys

from PyQt6.QtCore import QSize, Qt

from PyQt6.QtWidgets import QApplication,QMainWindow, QLabel,QLineEdit,QPushButton


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Entregar el texto ingresado")
        self.setGeometry(100,100,300,200)
       
        #Ventana principal
        self.label_input = QLabel("ingresa una palabra",self) 
        self.label_input.setGeometry(50,50,200,30)


        # Ventana de input texto
        self.text_input=QLineEdit(self)    
        self.text_input.setGeometry(50,80,200,30)


        #Boton clic
        self.button_reverse= QPushButton("Mostrar al reves" ,self)
        self.button_reverse.setGeometry(50,120,200,30)
        self.button_reverse.clicked.connect(self.reverse)
        

        # Output texto 
        self.label_output= QLabel(self)
        self.label_output.setGeometry(50,160,200,30)


    # Metodo inverso de del texto
    def reverse(self):
        str=self.text_input.text()
        reverse=str[::-1]
        self.label_output.setText(reverse)




if __name__ == "__main__":
    app=QApplication(sys.argv)
    Window=MainWindow()
    Window.show()

    sys.exit(app.exec())

