
class Color:
    azulClaroRgb = '97b9c0'
    azulEscuroRgb = '366873'
    brancoRgb = 'ffffff'
    vermelhoRgb = '8c5042'
    vermelhoRga = [0.549, 0.313, 0.258, 1]

    def fundoB(self):
        return self.azulClaroRgb

    def fundoTF(self):
        return self.brancoRgb
    
    def detalheClaro(self):
        return self.azulClaroRgb

    def detalheEscuro(self):
        return self.azulEscuroRgb

    def textoB(self):
        return self.brancoRgb

    def textoL(self):
        return self.azulEscuroRgb

    def textoTF(self):
        return self.azulEscuroRgb

    def rgbVermelho(self):
        return self.vermelhoRgb

    def rgaVermelho(self):
        return self.vermelhoRga