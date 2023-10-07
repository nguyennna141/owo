class Converter:
    def __init__(self):
        self.__decimal = 0
        self.__binary = ""
        self.__hexadecimal = ""

    def decimal_to_binary(self):
        decimal = self.__decimal
        if decimal == 0:
            self.__binary = "0"
            return
        binary = ""
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
        self.__binary = binary

    def decimal_to_hex(self):
        decimal = self.__decimal
        if decimal == 0:
            self.__hexadecimal = "0"
            return
        hex_str = ""
        while decimal > 0:
            temp = decimal % 16
            if temp < 10:
                hex_str = str(temp) + hex_str
            else:
                hex_str = chr(temp + 55) + hex_str
            decimal //= 16
        self.__hexadecimal = hex_str

    def binary_to_decimal(self):
        binary = self.__binary
        decimal = 0
        bit = len(binary) - 1
        for i in range(bit + 1):
            decimal += int(binary[i]) * 2 ** (bit - i)
        self.__decimal = decimal

    def hex_to_decimal(self):
        hex_str = self.__hexadecimal
        decimal = 0
        bit = len(hex_str) - 1
        b = bit
        for i in range(bit + 1):
            temp = hex_str[i]
            if temp.isdigit():
                decimal += int(temp) * 16 ** b
            else:
                decimal += (ord(temp) - 55) * 16 ** b
            b -= 1
        self.__decimal = decimal

    def set_decimal(self, decimal):
        self.__decimal = decimal

    def set_binary(self, binary):
        self.__binary = binary

    def set_hex(self, hex):
        self.__hexadecimal = hex

    def get_decimal(self):
        return self.__decimal

    def get_binary(self):
        return self.__binary

    def get_hex(self):
        return self.__hexadecimal


