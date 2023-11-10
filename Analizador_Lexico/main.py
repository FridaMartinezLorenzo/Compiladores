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
        return self.lexema + " " + self.token

def file_breakdown (lines, tokenList):
    nline = 1
    for line in lines:
        words_list = line.split()
        for word in words_list:
            word_search(word, nline, tokenList)
        nline += 1


def word_search(word, nline, tokenList):
    if word in lista_pReservadas:
        tokenList.append(element_TokenTable(word, word, nline)) #Agregamos a la lista de tokens
        return True
    return False
    
    
def not_word_search(word, nline, tokenList):
    aux=""
    for char in word:
        aux+=char
        print(word_search(word, nline, tokenList))
        if (flag == False):
        #print(aux)
    
        
    
    
#_____________________________________________________________________________________________________________________________________
# Leer el archivo de entrada


file = 'prueba.java'
with open(file, 'r') as f:
    lines_entry_file = f.readlines()

tokenList = []
#file_breakdown(lines_entry_file, tokenList)   

not_word_search("String", 1, tokenList)