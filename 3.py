import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow,QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contador de string")
        self.setGeometry(100,100,300,300)


        self.label_input= QLabel("Contador de palabras",self)
        self.label_input.setGeometry(80,80,200,50)


        self.text_input=QLineEdit(self)
        self.text_input.setGeometry(50,160,200,30)

        self.butom_count =QPushButton("Presiona",self)
        self.butom_count.setGeometry(50,200,200,50)
        self.butom_count.clicked.connect(self.count)
        
        
        self.text_output=QLabel(self)
        self.text_output.setGeometry(50,250,200,50)   
        
        
    def count(self):
        count= self.text_input.text()
        count=len(count)
        self.text_output.setText(f"La cantidad de palabras es {count}")
        
            
            

            

        


if __name__ == "__main__":
    app=QApplication(sys.argv)
    Window=MainWindow()
    Window.show()


    sys.exit(app.exec())

      

