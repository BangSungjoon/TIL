class Product:
    def __init__(self, pNo, pName, pPrice, pMaker, pColor, cNo):
        self.__pNo = pNo
        self.__pName = pName
        self.__pPrice = pPrice
        self.__pMaker = pMaker
        self.__pColor = pColor
        self.__cNo = cNo

    def get_pNo(self):
        return self.__pNo

    def get_pName(self):
        return self.__pName

    def get_pPrice(self):
        return self.__pPrice

    def get_pMaker(self):
        return self.__pMaker

    def get_pColor(self):
        return self.__pColor

    def get_cNo(self):
        return self.__cNo