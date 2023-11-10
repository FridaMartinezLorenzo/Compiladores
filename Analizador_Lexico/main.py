from Cargado_Datos import *

class element_TokenTable:
    def __init__(self, lexema, token,nl):
        self.lexema = lexema
        self.token = token
        self.nlinea = nl

    def get_lexema(self):
        return self.lexema

    def get_token(self):
        return self.token
    
    def get_nlinea(self):
        return self.nlinea

    def set_lexema(self, lexema):
        self.lexema = lexema

    def set_token(self, token):
        self.token = token
    
    def set_nlinea(self, nl):
        self.nlinea = nl

    def __str__(self):
        return self.lexema + " " + self.token+ " " + str(self.nlinea)
    

def file_breakdown (lines, tokenList):
    nline = 0
    for line in lines:
        nline+=1
        aux=""
        flag_string = False
        for char in line:
            if char == ' ' or char == '\n' or char == '\t' and flag_string == False: 
                pass
            aux+=char
            if char == '"' and flag_string == True: #Se encontro el fin de la cadena
                tokenList.append(element_TokenTable(aux, "varCadena", nline)) #Agregamos a la lista de tokens
                flag_string = False
                aux=""
            if char == '"': #Es una cadena, se empieza a guardar y se enciende la bandera y asi si esta la bandera encendida esperamos el siguiente
                flag_string = True
            if char in lista_simbolos and flag_string == False: #Es un simbolo
                tokenList.append(element_TokenTable(char, char, nline)) #Agregamos a la lista de tokens
                aux=""
            if flag_string == False:
                flag_found1 = word_search(aux, nline, tokenList)
                if (flag_found1 == True):
                    aux=""



def word_search(word, nline, tokenList):
    if word in lista_pReservadas:
        tokenList.append(element_TokenTable(word, word, nline)) #Agregamos a la lista de tokens
        return True
    return False
    

    
    
#_____________________________________________________________________________________________________________________________________
# Leer el archivo de entrada


file = 'prueba.java'
with open(file, 'r') as f:
    lines_entry_file = f.readlines()

tokenList = []
file_breakdown(lines_entry_file, tokenList)   
for token in tokenList:
    print(token)
