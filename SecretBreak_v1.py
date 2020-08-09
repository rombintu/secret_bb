from PyQt5 import QtCore, QtGui, QtWidgets
from breakingsecret import Ui_MainWindow
import sys
import random



#Создаем приложение
class S_break(QtWidgets.QMainWindow):
    
    
    def __init__(self):
        super(S_break, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_click)

    #Кнопка
    def on_click(self):
        secret = self.ui.lineEdit.text()
        secret = list(secret.upper())
        
        #Генерируем 3 гаммы размером равные секрету
        def gen_gam():
            gamma = []
            check = 0
            while check < len(secret):
                # генерация случайной буквы от А до Z
                simbol = chr(random.randrange(97, 122)).upper()
                gamma.append(simbol)        
                check += 1
            return gamma

        gamma_1 = gen_gam()
        gamma_2 = gen_gam()
        gamma_3 = gen_gam()

        #Получаем шифр
        def enCode(secret, arr1, arr2, arr3):
            i = 0
            summa = []
            summa_1 = []
            summa_2 = []
            summa_3 = []
            summa_4 = []
        # Создаем новые массивы, где вместо букв - числа по ascii
            for x in secret:
                x = ord(x)
                summa_1.append(x)
            for x in arr1:
                x = ord(x)
                summa_2.append(x)
            for x in arr2:
                x = ord(x)
                summa_3.append(x) 
            for x in arr3:
                x = ord(x)
                summa_4.append(x)
        # Пока не заполнится, делать XOR
            while i < len(secret):
                xor = summa_1[i] ^ summa_2[i] ^ summa_3[i] ^ summa_4[i]
                summa.append(xor)
                i+=1
            return summa 
        
        shifr_encode = enCode(secret, gamma_1, gamma_2, gamma_3) 
        

        # Переводим в строку
        gamma_1 = " , ".join(gamma_1)
        gamma_2 = " , ".join(gamma_2)
        gamma_3 = " , ".join(gamma_3)
        # shifr_encode = str(shifr_encode)
        # shifr_encode = " , ".join(shifr_encode)

        self.ui.textBrowser.setText(str(gamma_1))
        self.ui.textBrowser_2.setText(str(gamma_2))
        self.ui.textBrowser_3.setText(str(gamma_3))
        self.ui.textBrowser_4.setText(str(shifr_encode))
        
        

class main():
     #запуск
    app = QtWidgets.QApplication([])
    application = S_break()
    application.show()

    #закрытие
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
   
