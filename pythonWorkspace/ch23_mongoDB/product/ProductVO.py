class Product:
    def __init__(self, prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo):
        self.__prdNo = prdNo
        self.__prdName = prdName
        self.__prdPrice = prdPrice
        self.__prdMaker = prdMaker
        self.__prdColor = prdColor
        self.__ctgNo = ctgNo

    def get_pNo(self):
        return self.__prdNo

    def get_pName(self):
        return self.__prdName

    def get_pPrice(self):
        return self.__prdPrice

    def get_pMaker(self):
        return self.__prdMaker

    def get_pColor(self):
        return self.__prdColor

    def get_cNo(self):
        return self.__ctgNo