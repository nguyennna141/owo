import os, Gui, converter, sys
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtGui import QGuiApplication
except:
    os.system('pip install pyqt5')

class ConverterApp(Gui.Ui_MainWindow):
    def __init__(self):
        self.setupUi(MainWindow)
        self.converter = converter.Converter()
        self.decimal_to_binary_btn.clicked.connect(self.decimal_to_binary)
        self.decimal_to_hex_btn.clicked.connect(self.decimal_to_hex)
        self.Decimal_value.textChanged.connect(self.__check_clear_all)
        self.binary_to_decimal_btn.clicked.connect(self.binary_to_decimal)
        self.binary_to_hex_btn.clicked.connect(self.binary_to_hex)
        self.Binary_value.textChanged.connect(self.__check_clear_all)
        self.hex_to_binary_btn.clicked.connect(self.hex_to_binary)
        self.hex_to_decimal_btn.clicked.connect(self.hex_to_decimal)
        self.hex_value.textChanged.connect(self.__check_clear_all)
        self.copy_btn.clicked.connect(self.copy_result)
        self.copy_btn.setEnabled(False)
        self.clear.setEnabled(False)
        self.clear.clicked.connect(self.clear_all)
        self.result.textChanged.connect(self.__check_result)
        self.result.textChanged.connect(self.__check_clear_all)

    def __check_result(self):
        if len(self.result.toPlainText()) > 0:
            self.copy_btn.setEnabled(True)
        else:
            self.copy_btn.setEnabled(False)

    def __check_lenght_text(self, text):
        for _ in text:
            return True

    def __check_clear_all(self):
        if self.__check_lenght_text(self.Binary_value.text()) or self.__check_lenght_text(self.Decimal_value.text()) or self.__check_lenght_text(self.hex_value.text()) or self.__check_lenght_text(self.result.toPlainText()):
            self.clear.setEnabled(True)
        else:
            self.clear.setEnabled(False)

    def __send_text(self, content):
        self.result.setText(f"Dữ liệu Đầu vào không hợp lệ! Nhập lại {content} điii >>.<<")

    def __set_successful_conversion_status(self, content_conversion):
            self.status.setText(content_conversion + ' Conversion Successful ')
            self.status.setStyleSheet('color: green')

    def __set_failed_conversion_status(self):
            self.status.setText('Parameter error')
            self.status.setStyleSheet('color: red')

    def decimal_to_binary(self):
        if self.__is_decimal(self.Decimal_value.text()) and self.Decimal_value.text() != '':
            self.converter.set_decimal(int(self.Decimal_value.text()))
            self.converter.decimal_to_binary()
            self.result.setText(self.converter.get_binary())
            self.__set_successful_conversion_status('Decimal to binary')
        else:
            self.__send_text("số thập phân")
            self.__set_failed_conversion_status()
    
    def decimal_to_hex(self):
        if self.__is_decimal(self.Decimal_value.text()) and self.Decimal_value.text() != '':
            self.converter.set_decimal(int(self.Decimal_value.text()))
            self.converter.decimal_to_hex()
            self.result.setText(self.converter.get_hex())
            self.__set_successful_conversion_status('Decimal to hexadecimal')
        else:
            self.__send_text("số thập phân")
            self.__set_failed_conversion_status()
    def binary_to_decimal(self):
        if self.__is_binary(self.Binary_value.text()):
            self.converter.set_binary(self.Binary_value.text())
            self.converter.binary_to_decimal()
            self.result.setText(str(self.converter.get_decimal()))
            self.__set_successful_conversion_status('Binary to decimal')
        else:
            self.__send_text("dãy nhị phân")
            self.__set_failed_conversion_status()
    def binary_to_hex(self):
        if self.__is_binary(self.Binary_value.text()):
            self.converter.set_binary(self.Binary_value.text())
            self.converter.binary_to_decimal()
            self.converter.decimal_to_hex()
            self.result.setText(self.converter.get_hex())
            self.__set_successful_conversion_status('Binary to hexadecimal')
        else:
            self.__send_text("dãy nhị phân")
            self.__set_failed_conversion_status()

    def hex_to_decimal(self):
        if self.__is_hex(self.hex_value.text()):
            self.converter.set_hex(self.hex_value.text())
            self.converter.hex_to_decimal()
            self.result.setText(str(self.converter.get_decimal()))
            self.__set_successful_conversion_status('Hexadecimal to decimal')
        else:
            self.__send_text("hệ 16")
            self.__set_failed_conversion_status()

    def hex_to_binary(self):
        if self.__is_hex(self.hex_value.text()):
            self.converter.set_hex(self.hex_value.text())
            self.converter.hex_to_decimal()
            self.converter.decimal_to_binary()
            self.result.setText(self.converter.get_binary())
            self.__set_successful_conversion_status('Hexadecimal to binary')
        else:
            self.__send_text("hệ 16")
            self.__set_failed_conversion_status()
    def copy_result(self):
        clipboard = QGuiApplication.clipboard()  
        clipboard.setText(self.result.toPlainText())
        self.status.setText('Successful copy')
        self.status.setStyleSheet('color: green')

    def clear_all(self):
        self.result.clear()
        self.Binary_value.clear()
        self.hex_value.clear()
        self.Decimal_value.clear()
        self.status.setText('Successful clear all')
        self.status.setStyleSheet('color: green')

    def __is_binary(self, binary):
        for i in binary:
            if i != '1' and i != '0':
                return False
        return True
    
    def __is_hex(self, hex):
        char_hex = '0123456789ABCDEF'
        for i in hex:
            if i not in char_hex:
                return False
        return True
    
    def __is_decimal(self, decimal):
        decimal_char = '0123456789'
        for i in decimal:
            if i not in decimal_char:
                return False
        return True

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ConverterApp()
    MainWindow.show()
    sys.exit(app.exec_())


