from PyQt5 import QtCore, QtGui, QtWidgets
from buildingsecret import Ui_MainWindow
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
        
        shifr = self.ui.lineEdit.text()
        shifr = str(shifr.replace(',', ''))
        # shifr = str(shifr.replace(' ', ''))
        shifr = str(shifr.replace(']', ''))
        shifr = str(shifr.replace('[', ''))
        shifr = [int(i) for i in shifr.split()[::1]]

        # shifr = trans(shifr)
        gamma_1 = self.ui.lineEdit_2.text().upper()
        gamma_1 = str(gamma_1.replace(',', ''))
        gamma_1 = str(gamma_1.replace(' ', ''))
        gamma_2 = self.ui.lineEdit_3.text().upper()
        gamma_2 = str(gamma_2.replace(',', ''))
        gamma_2 = str(gamma_2.replace(' ', ''))
        gamma_3 = self.ui.lineEdit_4.text().upper()
        gamma_3 = str(gamma_3.replace(',', ''))
        gamma_3 = str(gamma_3.replace(' ', ''))


        #Расшифровываем 
        def deCode(code, arr1, arr2, arr3):
            i = 0
            summa = []
            summa_1 = []
            summa_2 = []
            summa_3 = []
            summa_4 = []
            for x in code:
                x = int(x)
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
            while i < len(shifr):
                xor = summa_1[i] ^ summa_2[i] ^ summa_3[i] ^ summa_4[i]
                summa.append(xor)
                i+=1
            return summa 
        
        shifr = deCode(shifr, gamma_1, gamma_2, gamma_3)

        # Перевод в символы
        def translate_de(arr):
            trans_arr = []
            for x in arr:
                x = chr(x)
                trans_arr.append(x)
            return trans_arr

        # получаем в переменную
        shifr = translate_de(shifr)

        # Переводим в строку
        shifr = " , ".join(shifr)
        
        self.ui.textBrowser_4.setText(str(shifr))
                
        

class main():
     #запуск
    app = QtWidgets.QApplication([])
    application = S_break()
    application.show()

    #закрытие
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
   
