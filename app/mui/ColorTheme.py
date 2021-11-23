class Color:
    azulClaroRgb = '97B9C0'
    azulEscuroRgb = '366873'
    azulCinzaRgb = '1E606F'
    azulRgba = [0.592, 0.725, 0.752, 1]
    azulMaisEscuroRgba = [148/255, 175/255, 192/255, 1]
    begeRgba = [140/255 , 80/255, 65/255, 0.5]
    cinzaRgb = '808DAD'
    brancoCinzaRgba = [245/255, 245/255, 245/255, 1]
    brancoCinzaEscuroRgba = [238/255, 238/255, 238/255, 1]
    brancoRgb = 'ffffff'
    brancoRga = [1,1,1,1]
    cinzaClaroRgb = "fcfcfc"
    laranjaRgba = [1, 170/255, 23/255, 1]
    transparenteRgba = [0,0,0,0]
    vermelhoRgb = '8C5042'
    vermelhoRga = [0.549, 0.313, 0.258, 1]

    def fundoB(self):
        return self.azulClaroRgb

    def fundoTF(self):
        return self.brancoRgb

    def bottomNavPanel(self):
        return self.azulRgba

    def bottomNavTextActive(self):
        return self.cinzaClaroRgb
    
    def bottomNavTextNormal(self):
        return self.azulCinzaRgb
    
    def detalheClaro(self):
        return self.azulClaroRgb

    def detalheEscuro(self):
        return self.azulEscuroRgb
    
    def linhaBanner(self):
        return self.azulRgba

    def linhaTFF(self):
        return self.azulEscuroRgb

    def linhaTFN(self):
        return self.azulEscuroRgb

    def textoB(self):
        return self.brancoRgb

    def textoL(self):
        return self.azulEscuroRgb
    
    def textoRFB(self):
        return self.azulEscuroRgb

    def textoTF(self):
        return self.azulEscuroRgb

    def rgbVermelho(self):
        return self.vermelhoRgb

    def rgaVermelho(self):
        return self.vermelhoRga

    def rgaBranco(self):
        return self.brancoRga
    
    def textMessageSent(self):
        return self.brancoRgb
    
    def rectangleMessageSent(self):
        return self.azulRgba
    
    def textMessageReceived(self):
        return self.brancoRgb
    
    def rectangleMessageSent(self):
        return self.azulMaisEscuroRgba
    
    def arrowIconChatScreen(self):
        return self.cinzaRgb
    
    def ellipseColor(self):
        return self.begeRgba
    
    def userNameChatScreen(self):
        return self.vermelhoRgb
    
    def chatTextBackground(self):
        return self.brancoCinzaRgba
    
    def chatText(self):
        return self.brancoCinzaEscuroRgba
    
    def chatIconButton(self):
        return self.azulClaroRgb
    
    def chatTextInputCursor(self):
        return self.azulRgba
        
    def chatTextInputForeground(self):
        return self.laranjaRgba

    def chatTextInputBackground(self):
        return self.transparenteRgba