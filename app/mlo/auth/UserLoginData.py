from pydantic import BaseModel, validator

class UserLoginData(BaseModel):
    email: str
    password: str

    @validator('email')
    def emptyEmail(cls, v):
        if v == '':
            raise ValueError('O email é um campo vazio')
        return v
    
    @validator('password')
    def emptyPassword(cls, v):
        if v == '':
            raise ValueError('A senha é um campo vazio')
        return v
    
    @validator('password')
    def shortPassword(cls, v):
        if len(str(v)) < 6:
            raise ValueError('A senha não pode ter menos do que 6 caracteres')
        return v

    @validator('password')
    def longPassword(cls, v):
        if len(str(v)) > 20:
            raise ValueError('A senha não pode ter mais do que 20 caracteres')
        return v
    
    @validator('password')
    def specialCharacterInPassword(cls, v):
        if (str(v)).isalnum() == False:
            raise ValueError('A senha não pode ter caracteres especiais')
        return v

    @validator('password')
    def wrongFormatPassword(cls, v):
        cbaixa = False
        calta = False
        digito = False

        for i in range(len(str(v))):
            c = str(v)[i]  # Caractere

            if (c.isdigit()) and (digito == False):
                digito = True
            else:
                if (c.islower()) and (cbaixa == False):
                    cbaixa = True
                elif (c.isupper()) and (calta == False):
                    calta = True

        if (cbaixa == False) or (calta == False) or (digito == False):
            raise ValueError('A senha deve ter ao menos uma letra minúscula, uma letra maiúscula e um dígito')
        return v
    
    @validator('email')
    def withoutAtSignEmail(cls, v):
        if (str(v)).find('@') == -1:
            raise ValueError('O email deve ter um @ separando a parte local do domínio')
        return v

    @validator('email')
    def withoutDotComEmailDomain(cls, v):
        if len(str(v)) - (str(v)).find(".com") != 4:
            raise ValueError('O email deve terminar com \'.com\'')
        return v

    @validator('email')
    def wrongFirstOrLastCharacterEmailDomain(cls, v):
        ini = (str(v)).find('@') + 1
        fim = (str(v)).find(".com") - 1

        ini = str(v)[ini]
        fim = str(v)[fim]

        if (ini.isalnum() == False) or (fim.isalnum() == False):
            raise ValueError('O domínio do email deve ter uma letra ou um dígito no início e antes do \'.com\'')
        return v
    
    @validator('email')
    def wrongFormatEmailDomain(cls, v):
        ini = (str(v)).find('@') + 2
        fim = (str(v)).find(".com") - 1
        sent = True

        for i in range(ini, fim):
            c = str(v)[i]  # Caractere

            if c.isalnum() == False:
                if c != '-':
                    sent = False
                    break

        if sent == False:
            raise ValueError('O domínio do email não pode ter caractere especial diferente de hífen')
        return v
    
    @validator('email')
    def wrongFirstOrLastCharacterEmailLocalPart(cls, v):
        sent = True
        c = str(v)[0]

        if c.isalnum() == False:
            if (c != '-') and (c != '_'):
                sent = False
        else:
            c = str(v)[(str(v)).find('@')-1]

            if c.isalnum() == False:
                if (c != '-') and (c != '_'):
                    sent = False

        if sent == False:
            raise ValueError('A parte local do email não pode ter caractere especial diferente de hífen e underscore no começo e/ou final')
        return v

    @validator('email')
    def wrongFormatEmailLocalPart(cls, v):
        sent = True
        fim = (str(v)).find('@') - 1

        for i in range(0, fim):
            c = str(v)[i]  # Caractere

            if c.isalnum() == False:
                if (c != '.') and (c != '-') and (c != '_'):
                    sent = False
                    break

        if sent == False:
            raise ValueError('A parte local do email não pode ser composta por caracteres especiais diferentes de ponto, hífen e underscore')
        return v
    
    @validator('email')
    def ConsecutiveDotsEmailLocalPart(cls, v):
        if (str(v)).find("..") != -1:
            raise ValueError('A parte local do email não pode ter mais de um ponto consecutivo')
        return v