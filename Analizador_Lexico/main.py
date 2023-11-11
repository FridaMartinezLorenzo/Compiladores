from Cargado_Datos import *
import re

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
        flag_found1 = False
        flag_id = False
        flag_number = False
        flag_float = False
        for char in line:
            #print("flag_string: ",flag_string)
            aux+=char
            if (char == ' ' or char == '\n' ) and flag_string == False: 
                aux=""
                pass
            print("aux:",aux)
            if char == '"' and flag_string == False: #Es una cadena, se empieza a guardar y se enciende la bandera y asi si esta la bandera encendida esperamos el siguiente
                flag_string = True
                pass
            
            elif char == '"' and flag_string == True: #Se encontro el fin de la cadena
                tokenList.append(element_TokenTable(aux, "varCadena", nline)) #Agregamos a la lista de tokens
                flag_string = False
                aux=""
                pass
            
            print("flag_number:",flag_number)
            print("flag_string:",flag_string)
            if char in lista_simbolos and flag_string == False and flag_number == False: #Es un simbolo
                print("Evaluacion de simbolo")
                tokenList.append(element_TokenTable(char, char, nline)) #Agregamos a la lista de tokens
                aux=""
                pass
            print("char:",char)
            if char.isdigit() and flag_string == False and flag_id == False: #Es un numero
                print("Se encontró un numero")
                flag_number = True
                pass
            
            #Deteccion de los numeros de punto flotante
            elif flag_number == True: #Evaluar si es un numero entero o flotante
                print("Evaluando un numero\n")
                if char == '.':
                    flag_float = True
    
                elif(es_float_re(aux) and flag_float == True):
                        print("Evaluando un flotante")
                        tokenList.append(element_TokenTable(aux, "nfloat", nline))                      
                        aux=""
                        aux+=char
                        flag_number = False
                        
                if (not char.isdigit()) and flag_float == False:# Se había detectado un numero, se lee hasta que no sea un numero
                    aux = aux[:-1] #"le restamos uno porque el ultimo no es un numero"
                    tokenList.append(element_TokenTable(aux, "nint", nline))                      
                    aux=""
                    aux+=char
                    flag_number = False
                pass
            
            if char.isalpha(): #Existe la posibilidad de que sea un identificador 
                #print("Evaluacion de identificador")
                #flag_id = True
                pass
            if flag_string == False:
                #print("Evaluacion de palabra reservada")
                flag_found1 = word_search(aux, nline, tokenList)
                #print("flag_found1: ",flag_found1)
                if (flag_found1 == True):
                    flag_found1 = False
                    aux=""
                pass       
                    



def word_search(word, nline, tokenList):
    if word in lista_pReservadas:
        tokenList.append(element_TokenTable(word, word, nline)) #Agregamos a la lista de tokens
        return 1
    return 0
    
def es_numero(cadena):
    try:
        int(cadena) # Intenta convertir la cadena a un entero
        return True
    except ValueError:
        return False # La conversión a entero falló, no es un número
    
def es_nint_re(cadena):
    prueba = re.match(r'[0-9]*(?!\.)', cadena)    # Cualquier repetición de números, pero sin un punto decimal al final
    if prueba is not None:
        return True
    return False

def es_float_re(cadena):
    prueba = re.match(r'[0-9]*\.[0-9]', cadena)   # Dos repeticiones de números, con un punto decimal entre ellas
    if prueba is not None:
        return True
    return False
    
def es_id(cadena):
    prueba = re.match('[a-zA-Z][a-zA-z0-9$_]f*', cadena)
    if prueba is not None:
        return True     # Encontró un nombre que empieza por letra, y contiene letras, números, $ ó _
    return False

def es_cad(cadena):
    prueba = re.match('".*"', cadena)
    if prueba is not None:
        return True     # Encontró una frase que está encerrada entre comillas dobles
    return False

def es_car(cadena):
    prueba = re.match("'.'", cadena)
    if prueba is not None:
        return True     # Encuentra un solo caracter entre comillas simples
    return False
    
    
#_____________________________________________________________________________________________________________________________________
# Leer el archivo de entrada


file = 'prueba.java'
with open(file, 'r') as f:
    lines_entry_file = f.readlines()

tokenList = []
#print(es_float_re("1.2f;"))

file_breakdown(lines_entry_file, tokenList)   
for token in tokenList:
    print(token)
#word_search(cad, 1, tokenList)
#print(tokenList[0])