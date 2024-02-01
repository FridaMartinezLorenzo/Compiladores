from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from lexico import *
from Analizador_Lexico import *
from TablaAnalisisSintactico import *
from PrimerosYSiguientes import mainPyS
import re

class result_acc:
    def __init__(self, base, atrib, val):
        self.base = base
        self.atrib = atrib
        self.val = val
    
    def get_base(self):
        return self.base
    
    def get_atrib(self):
        return self.atrib
    
    def get_val(self):
        return self.val
    
    def set_base(self, base):
        self.base = base

    def set_atrib(self, atrib):
        self.atrib = atrib

    def set_val(self, val):
        self.val = val

    def __str__(self):
        return str(self.base) + "." + str(self.atrib) + ":=" + str(self.val)

def analizadorSemantico():
    VentanaPrincipal =Toplevel()
    VentanaPrincipal.title("Analizador semántico")
    VentanaPrincipal.state("zoomed")
    VentanaPrincipal.config(background="#363062")
    VentanaPrincipal.iconbitmap("Compiler.ico")
    encabezado(VentanaPrincipal)

def encabezado(VentanaPrincipal):
    font1=("Times New Roman",14)
    font2=("Times New Roman",20)
    archivoLabel=Label(VentanaPrincipal,text="Seleccionar Archivo:",font=font1,width=20,background="#363062",foreground="white")
    archivoLabel.place(x=60,y=30)
    archivoButton=Button(VentanaPrincipal,text="Cargar Gramatica",width=20,command=lambda:abrirArchivo(VentanaPrincipal),bg="#F99417",font=font1)
    archivoButton.place(x=300,y=20)
    tokenButton=Button(VentanaPrincipal,text="Abrir Archivo",width=20,bg="#F99417",font=font1,command=lambda:abrirArchivo1(VentanaPrincipal))
    tokenButton.place(x=300,y=100)
    ImprimirResultad0s=Button(VentanaPrincipal,text="Imprimir Resultados",width=20,bg="#F99417",font=font1,command=lambda:imprimirResultados(VentanaPrincipal))
    ImprimirResultad0s.place(x=500,y=60)
    limpiarButton=Button(VentanaPrincipal,text="Limpiar",width=20,bg="#F99417",font=font1,command=lambda:limpiar(VentanaPrincipal))
    limpiarButton.place(x=700,y=60)

def cargarGramatica(Ventana,direccionArchivo):
    global Gramatica
    frameGramatica=Frame(Ventana,width=300,height=600)
    frameGramatica.place(x=60,y=100)
    archivo=open(direccionArchivo,"r",encoding="utf-8")
    Gramatica=[]
    linea=archivo.readline()
    linea=archivo.readline()
    contador=0
    while linea:
        linea=archivo.readline()
        grama=linea
        grama=grama.replace("\n","")
        Gramatica.append(grama) #aqui se guarda la gramatica sin el salto de linea
        mostrarRegla=Label(frameGramatica,text=str(linea),font=("Times New Roman",14),width=20)
        mostrarRegla.grid(row=contador,column=0)
        contador+=1

def abrirArchivo(Ventana):
    global direccionArchivo2
    Ventana.grab_set()
    username=getpass.getuser()
    ruta_proyecto = r"C:\Users\{username}\Documents\ProyectoCompiladores"

    # Cambiar para que acepte cualquier gramática que se le indique
    # direccionArchivo2= "Pruebas_Archivos_Entrada_JAVA/entradaLR.txt"
    direccionArchivo2 = filedialog.askopenfilename(initialdir=ruta_proyecto, title="Cargar Gramática", filetypes=(("txt", "*.txt"),))
    cargarGramatica(Ventana,direccionArchivo2)

def abrirArchivo1(Ventana):
    global tiraTokens
    Ventana.grab_set()
    username=getpass.getuser()
    ruta_proyecto = r"C:\Users\{username}\Documents\ProyectoCompiladores"
    direccionArchivo=filedialog.askopenfilename(initialdir=ruta_proyecto,title="Abrir Archivo",filetypes=(("txt", "*.txt"),))
    tiraTokens = ObtenerTiraTokensExternaObj(direccionArchivo)

    # Cambiar esto para que tiraTokens funcione con objetos y no cadena
    #SUSTITUIMOS LOS == y simbolos compuestos por dos caracteres para que sean detectados
    for tok in tiraTokens:
        tok.set_tipo(tok.get_tipo().replace("<","menorque"))
        tok.set_tipo(tok.get_tipo().replace(">","mayorque"))
        tok.set_tipo(tok.get_tipo().replace("==","igualigual"))
        tok.set_tipo(tok.get_tipo().replace(">=","mayorigual"))
        tok.set_tipo(tok.get_tipo().replace("<=","menorigual"))
        tok.set_tipo(tok.get_tipo().replace("!=","diferente"))
        tok.set_tipo(tok.get_tipo().replace("&&","and"))
        tok.set_tipo(tok.get_tipo().replace("||","or"))
        tok.set_tipo(tok.get_tipo().replace("++","masmas"))
        tok.set_tipo(tok.get_tipo().replace("--","menosmenos"))
        tok.set_tipo(tok.get_tipo().replace("+=","masigual"))
        tok.set_tipo(tok.get_tipo().replace("-=","menosigual"))
        tok.set_tipo(tok.get_tipo().replace("*=","porigual"))
        tok.set_tipo(tok.get_tipo().replace("/=","entredosigual"))
        tok.set_tipo(tok.get_tipo().replace("%=","modigual"))
        tok.set_tipo(tok.get_tipo().replace("-", "resta"))
        tok.set_tipo(tok.get_tipo().replace("String", "string"))
    print("Tira de tokens recibida en el léxico:\n", tiraTokens)

def imprimirResultados(Ventana):
    global tiraTokens
    global direccionArchivo2
    global Gramatica
    ventanaResultados=Toplevel()
    ventanaResultados.title("Resultados")
    ventanaResultados.state("zoomed")
    ventanaResultados.grab_set()
    frameResultados=Frame(ventanaResultados,width=300,height=600)
    frameResultados.place(x=60,y=100)
    ventana2=Toplevel()
    frame2=Frame(ventana2,width=300,height=600)
    
    #Esto es lo que hay que arreglar
    datos,reglas=ImprimirResultados2(ventana2,frame2,direccionArchivo2)
    ventana2.destroy()
    setDireccionArchivo(direccionArchivo2,reglas)
    variable,simbolos,estados=ImprimirTablaAS(ventanaResultados,frameResultados)#variable es un diccionario con clave el numero de estado y la columna y contenido un label con el contenido de la tabla
    for var in variable:
        contenido=variable[var]
        cont=contenido.cget("text")
        print("clave:",var,"contenido:",cont)
    #print("simbolos:",simbolos)
    #print("estados:",estados)
        
    # Cambiar esto para que tira y tiraTokens funcionen con objetos y no cadena
    print("tiraTokens:",tiraTokens)
    tuplasimbolos=()
    arreglosimbolos=[]
    j=0
    for i in simbolos:
        j=j+1
        tuplasimbolos=(i,j)
        arreglosimbolos.append(tuplasimbolos)
    tuplaGrama=()
    arreGramatica=[]
    Gramatica=list(filter(lambda x: x is not None and x != "", Gramatica)) #aqui se quitan los elementos vacios de la lista

    #Editar para que acepte una tercera sección para las traducciones
    arreAcciones = []
    for grama in Gramatica:
        grama=grama.split("->")
        tuplaGrama=(grama[0],grama[1])
        arreGramatica.append(tuplaGrama)
        arreAcciones.append(grama[2])
    print("Gramatica:",arreGramatica)
    print("simbolos:",arreglosimbolos)
    print("Acciones:",arreAcciones)
    print("funcion")
    TablaLr(variable,arreglosimbolos,tiraTokens,arreGramatica,Ventana,arreAcciones)
    ventanaResultados.grab_release()

def TablaLr(variable,simbolos,tira,arreGramatica,Ventana,arreAcciones):
    Ventana.grab_set()
    tabla=Frame(Ventana,width=1200,height=600)
    tabla.place(x=300,y=150)
    canvas=Canvas(Ventana,width=1200,height=600)
    canvas.place(x=300,y=150)

    def on_arrow_key(event):
            if event.keysym == "Left":
                canvas.xview_scroll(-1, "units")
            elif event.keysym == "Right":
                canvas.xview_scroll(1, "units")
            #canvas.config(scrollregion=canvas.bbox("all"))    

    def on_arrow_key_v(event):
         if event.keysym == "Up":
             canvas.yview_scroll(-1, "units")
         elif event.keysym == "Down":
             canvas.yview_scroll(1, "units")
         #canvas.config(scrollregion=canvas.bbox("all"))
    
    scrollbar=ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.set(0.0, 1.0)
    scrollbar.place(x=5, y=50, height=300)

    horizontal_scrollbar = ttk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    horizontal_scrollbar.set(0.0,1.0)
    horizontal_scrollbar.place(x=0,y=0,width=300)

    tabla=Frame(canvas,width=1470,height=300)
    canvas.create_window((100, 50), window=tabla, anchor=NW)
    canvas.configure(yscrollcommand=scrollbar.set,xscrollcommand=horizontal_scrollbar.set)
    canvas.bind_all("<KeyPress-Left>", on_arrow_key)
    canvas.bind_all("<KeyPress-Right>", on_arrow_key)
    canvas.bind_all("<KeyPress-Up>", on_arrow_key_v)
    canvas.bind_all("<KeyPress-Down>", on_arrow_key_v)
    contadorFila=0
    pila=[]
    accion=[]
    pila.append(0)
    font1=("Times New Roman",14)
    labelTextPila=Label(tabla,text="Pila",width=20,font=font1,borderwidth=2,relief="solid")
    labelTextPila.grid(row=contadorFila,column=0)
    labelTextTira=Label(tabla,text="Entrada",width=30,font=font1,borderwidth=2,relief="solid")
    labelTextTira.grid(row=contadorFila,column=1)
    labelTextSalida=Label(tabla,text="Salida",width=100,font=font1,borderwidth=2,relief="solid")
    labelTextSalida.grid(row=contadorFila,column=2,columnspan=3)
    contadorFila+=1
    results_acc = []

    # Cambiar esto para que tira funcione con objetos y no con cadena
    while((len(tira)>0) & (accion!='Aceptacion') & (accion!='')):
        a=tira[0]
        sacarTira=tira[0]
        labelPila=Label(tabla,text=pilaCadena(pila),width=20,font=font1,borderwidth=2,relief="solid")
        labelPila.grid(row=contadorFila,column=0) 
        labelTira=Label(tabla,text=pilaCadena(tira),width=30,font=font1,borderwidth=2,relief="solid")
        labelTira.grid(row=contadorFila,column=1)
        simboloTira=buscarSimbolo(simbolos,sacarTira)
        print("simbolo en la tira:",simboloTira)
        estado=pila.pop()
        pila.append(estado)
        entero=int(estado)
        entero=entero+2
        print("estado en el que vamos:",entero)
        accion=buscarAccion(variable,entero,simboloTira)
        if(accion != None):
            if(accion[0]=='d'):
                tira.pop(0)
                print("salida:",accion) #imprimimos la accion de desplazamiento o reduccion
                labelSalida=Label(tabla,text=pilaCadena(accion),width=20,font=font1,borderwidth=2,relief="solid")
                labelSalida.grid(row=contadorFila,column=2)
                labelRegla=Label(tabla,text=" ",width=40,font=font1,borderwidth=2,relief="solid")
                labelRegla.grid(row=contadorFila,column=3)
                labelAccion=Label(tabla,text=" ",width=40,font=font1,borderwidth=2,relief="solid")
                labelAccion.grid(row=contadorFila,column=4)
                pila.append(a)
                estadoAgregar=int(accion[1:])
                pila.append(estadoAgregar)
                print("contenido de la pila:",pila)
                print("tira de tokens despues del desplazamiento:",tira)
            elif(accion[0]=='0'or accion[0]=='1' or accion[0]=='2' or accion[0]=='3' or accion[0]=='4' or accion[0]=='5' or accion[0]=='6' or accion[0]=='7' or accion[0]=='8' or accion[0]=='9'):
                tira.pop(0)
                print("salida:",accion) #imprimimos la accion de desplazamiento o reduccion
                labelSalida=Label(tabla,text=pilaCadena(accion),width=20,font=font1,borderwidth=2,relief="solid")
                labelSalida.grid(row=contadorFila,column=2)
                labelRegla=Label(tabla,text=" ",width=40,font=font1,borderwidth=2,relief="solid")
                labelRegla.grid(row=contadorFila,column=3)
                labelAccion=Label(tabla,text=" ",width=40,font=font1,borderwidth=2,relief="solid")
                labelAccion.grid(row=contadorFila,column=4)
                pila.append(a)
                estadoAgregar=int(accion)
                pila.append(estadoAgregar)
                print("contenido de la pila:",pila)
                print("tira de tokens despues del desplazamiento:",tira)
            elif(accion[0]=='r'):  #reducir A→β
                print("es una reduccion")
                pos=int(accion[1:])
                regla=arreGramatica[pos-1]

                acc_seman = arreAcciones[pos-1]
                # Procesamiento de la acción semántica
                cad = re.sub(r"^\s*{", "", acc_seman)
                cad = re.sub(r"}\s*$", "", cad)  # Se eliminan las llaves de los laterales
                print("cad:", cad)

                partes = []
                cad_aux = ""
                flag_cad = False
                for car in cad:         # Revisar caracter por caracter en busca de espacios que no estén en cadenas
                    if (flag_cad is True):
                        if (car == '"'):
                            flag_cad = False
                        cad_aux = cad_aux + car
                    else:
                        if (car == ' '):
                            if (cad_aux != ""):
                                partes.append(cad_aux)
                                print("Instrucción:", cad_aux)
                            cad_aux = ""
                        else:
                            if (car == '"'):
                                flag_cad = True
                            cad_aux = cad_aux + car
                
                if (cad_aux != ""):
                    partes.append(cad_aux)
                    print("Instrucción:", cad_aux)

                fase_if = 0
                se_cumple = False
                for pos in range(0, len(partes)):      # Procesar cada instrucción por separado
                    if (fase_if==0):                        # Proceso normal
                        if (partes[pos] == "if"):               # Si detecta un if
                            fase_if = 1
                        else:
                            base = re.sub(r"\..*$", "", partes[pos]).strip()
                            print("Base:", base)
                            atrib = re.sub(r":=.*$", "", re.sub(r"^.*?\.", "", partes[pos])).strip()
                            print("Atributo:",atrib)
                            val = re.sub(r"^.*:=", "", partes[pos]).strip()
                            print("Acción:", val)
                            # Para este punto la acción ya debe estar separada en base, atributo y valor
                            postVal = obtenerValor(val, results_acc, pila, False)
                            results_acc.append(result_acc(base, atrib, postVal))        # Se guarda el resultado en la pila de resultados
                    elif (fase_if==1):                      # Detecta la condición
                        se_cumple = obtenerCondicion(partes[pos], results_acc, pila)
                        fase_if = 2
                    elif (fase_if==2):
                        if (se_cumple is True):
                            base = re.sub(r"\..*$", "", partes[pos]).strip()
                            print("Base:", base)
                            atrib = re.sub(r":=.*$", "", re.sub(r"^.*?\.", "", partes[pos])).strip()
                            print("Atributo:",atrib)
                            val = re.sub(r"^.*:=", "", partes[pos]).strip()
                            print("Acción:", val)
                            # Para este punto la acción ya debe estar separada en base, atributo y valor
                            postVal = obtenerValor(val, results_acc, pila, False)
                            results_acc.append(result_acc(base, atrib, postVal))        # Se guarda el resultado en la pila de resultados
                        fase_if = 3
                    elif (fase_if==3):
                        fase_if = 4
                    elif (fase_if==4):
                        if (se_cumple is False):
                            base = re.sub(r"\..*$", "", partes[pos]).strip()
                            print("Base:", base)
                            atrib = re.sub(r":=.*$", "", re.sub(r"^.*?\.", "", partes[pos])).strip()
                            print("Atributo:",atrib)
                            val = re.sub(r"^.*:=", "", partes[pos]).strip()
                            print("Acción:", val)
                            # Para este punto la acción ya debe estar separada en base, atributo y valor
                            postVal = obtenerValor(val, results_acc, pila, False)
                            results_acc.append(result_acc(base, atrib, postVal))        # Se guarda el resultado en la pila de resultados
                        fase_if = 0

                # Imprimir la lista de resultados para verificar
                print("--- Resultados hasta ahora ---")
                for i in range(len(results_acc)-1, -1, -1):
                    print(str(results_acc[i]))

                labelSalida=Label(tabla,text=pilaCadena(accion),width=20,font=font1,borderwidth=2,relief="solid")
                labelSalida.grid(row=contadorFila,column=2)
                #imprimir la producción A→β
                print("Regla:",regla)
                labelRegla=Label(tabla,text=str(regla[0])+"->"+str(regla[1]),width=40,font=font1,borderwidth=2,relief="solid")
                labelRegla.grid(row=contadorFila,column=3)
                labelAccion=Label(tabla,text=acc_seman,width=40,font=font1,borderwidth=2,relief="solid")
                labelAccion.grid(row=contadorFila,column=4)
                tama=len(regla[1].split(' ')) #calculamos el tamaño de β
                reglasinL=regla[1].split(' ')
                if(reglasinL[0]=='λ'):
                    tama=0
                else:
                    tama=tama*2 
                print("tamaño de beta:",tama)
                print("ctm")
                for k in range(0,tama):
                    pila.pop()  #pop 2*|β| símbolos
                print("contenido de la pila despues de eliminar:",pila)
                pila.append(regla[0])   #push A
                print("contenido de la pila despues de agregar A:",pila)
                simbIra=buscarSimbolo(simbolos,pila[len(pila)-1])
                #s=Ir_a[j,A]
                es=int(pila[len(pila)-2])+2
                print(es)
                s=buscarAccion(variable,es,simbIra)
                #push s
                print(s)
                pila.append(s)
                print("contenido de la pila despues de agregar s:",pila)
                print("tira de tokens despues de la reduccion:",tira)

            
            elif(accion=='Aceptacion'):
                print("Aceptado")
                labelRegla=Label(tabla,text="Aceptacion",width=20,font=font1,borderwidth=2,relief="solid")
                labelRegla.grid(row=contadorFila,column=2)
                label2=Label(tabla,text=" ",width=40,font=font1,borderwidth=2,relief="solid")
                label2.grid(row=contadorFila,column=3)
                labelAccion=Label(tabla,text="Resultado: "+str(results_acc[len(results_acc)-1]),width=40,font=font1,borderwidth=2,relief="solid")
                labelAccion.grid(row=contadorFila,column=4)
            elif(accion==''):
                print("Error de sintaxis")
                break
        else:
            print("Error de sintaxis")
            esperaba=[]
            esperaba=buscarSeEsperaba(entero,variable,simbolos)
            print("se esperaba: ",esperaba)
            labelError=Label(tabla,text="se esperaba: "+pilaError(esperaba),width=40,font=font1,borderwidth=2,relief="solid")
            labelError.grid(row=contadorFila,column=2)
            label2=Label(tabla,text=" ",width=30,font=font1,borderwidth=2,relief="solid")
            label2.grid(row=contadorFila,column=3)
            label3=Label(tabla,text=" ",width=30,font=font1,borderwidth=2,relief="solid")
            label3.grid(row=contadorFila,column=4)
            break
        contadorFila+=1

def obtenerValor(accion, results_acc, pila, esCond):
    print("Entra a función")
    print(accion)
    band = False

    prueba_simb = re.split(r"\|\|", accion, 1)
    if (len(prueba_simb) > 1):
        # Hay una concatenación en la acción
        print("Entró a concatenación")
        # Se usa recursividad para calcular el valor del segundo segmento
        val2 = obtenerValor(prueba_simb[1], results_acc, pila, esCond)
        val1 = obtenerValor(prueba_simb[0], results_acc, pila, esCond)
        return str(val1) + str(val2)

    prueba_simb = re.split(r"\+", accion, 1)
    if (len(prueba_simb) > 1):
        # Hay una suma en la acción
        print("Entró a suma")
        # Se usa recursividad para calcular el valor del segundo segmento
        val2 = obtenerValor(prueba_simb[1], results_acc, pila, esCond)
        val1 = obtenerValor(prueba_simb[0], results_acc, pila, esCond)
        return int(val1) + int(val2)

    prueba_simb = re.split(r"-", accion, 1)
    if (len(prueba_simb) > 1):
        # Hay una resta en la acción
        print("Entró a resta")
        # Se usa recursividad para calcular el valor del segundo segmento
        val2 = obtenerValor(prueba_simb[1], results_acc, pila, esCond)
        val1 = obtenerValor(prueba_simb[0], results_acc, pila, esCond)
        return int(val1) - int(val2)

    prueba_simb = re.split(r"\*", accion, 1)
    if (len(prueba_simb) > 1):
        # Hay una multiplicación en la acción
        print("Entró a multiplicación")
        # Se usa recursividad para calcular el valor del segundo segmento
        val2 = obtenerValor(prueba_simb[1], results_acc, pila, esCond)
        val1 = obtenerValor(prueba_simb[0], results_acc, pila, esCond)
        return int(val1) * int(val2)

    prueba_simb = re.split(r"/", accion, 1)
    if (len(prueba_simb) > 1):
        # Hay una división en la acción
        print("Entró a división")
        # Se usa recursividad para calcular el valor del segundo segmento
        val2 = obtenerValor(prueba_simb[1], results_acc, pila, esCond)
        val1 = obtenerValor(prueba_simb[0], results_acc, pila, esCond)
        return int(val1) / int(val2)

    # No hay operación, se debe almacenar un valor (Caso base)
    print("No hay operador")
    prueba_simb = re.split(r"\.", accion, 1)
    if (prueba_simb[0] == "nint"):          # Si lo que se busca es un nfloat...
        for i in range(len(pila)-1, -1, -1):    # Recorrer la pila de la tabla...
            print(pila[i])
            if (isinstance(pila[i], token_tipo_val) and pila[i].get_tipo() == "nint"):    # Si el tipo es el buscado...
                print("Se encontró int")
                return pila[i].get_val()         # Obtiene el valor de la variable nint
            
    elif (prueba_simb[0] == "nfloat"):          # Si lo que se busca es un nint...
        for i in range(len(pila)-1, -1, -1):    # Recorrer la pila de la tabla...
            print(pila[i])
            if (isinstance(pila[i], token_tipo_val) and pila[i].get_tipo() == "nfloat"):    # Si el tipo es el buscado...
                print("Se encontró float")
                return pila[i].get_val()         # Obtiene el valor de la variable nfloat
            
    elif (prueba_simb[0] == "id"):          # Si lo que se busca es un id...
        for i in range(len(pila)-1, -1, -1):    # Recorrer la pila de la tabla...
            print(pila[i])
            if (isinstance(pila[i], token_tipo_val) and pila[i].get_tipo() == "id"):    # Si el tipo es el buscado...
                print("Se encontró id")
                return pila[i].get_val()         # Obtiene el valor de la variable id

    else:
        try:
            prueba_int = int(accion)
            return prueba_int
        except:
            print("No es entero")

        prueba_simb = re.search(r'^".*?"$', accion)
        if (prueba_simb is not None):
            print("Se asigna una cadena")
            result = re.sub(r'^\s*"', "", accion)
            result = re.sub(r'"\s*$', "", result)
            print(result)
            return result

        else:
            prueba_simb = re.split(r"\.", accion, 1)
            for i in range(len(results_acc)-1, -1, -1): # Se recorre la pila de resultados
                if (results_acc[i].get_base()==prueba_simb[0] and results_acc[i].get_atrib()==prueba_simb[1]):  # Si la base y el atributo coinciden...}
                    print("Se encontró el valor de la pila de resultados")
                    print(results_acc[i].get_base())
                    print(results_acc[i].get_atrib())
                    print(results_acc[i].get_val())
                    result = results_acc[i].get_val()
                    if (esCond is False):           # Si la acción debe ser ejecutada (no es comparación)
                        results_acc.pop(i)               # Asignar el valor almacenado y eliminar resultado de la pila
                    return result
        
            print("*** No se encontró valor para asociar ***")
            return None                 # Por defecto se devuelve None si no se encuentra el valor buscado
        
def obtenerCondicion(cond, results_acc, pila):
    print("Entra a condición")
    print(cond)

    prueba_op = re.split(r"!=", cond, 1)         # Busca una negación
    if (len(prueba_op) > 1):
        print("Entró a negación")
        # Se usa recursividad para calcular el valor de ambas expresiones
        exp2 = obtenerValor(prueba_op[1], results_acc, pila, True)
        exp1 = obtenerValor(prueba_op[0], results_acc, pila, True)
        print("exp1:", exp1)
        print("exp2:", exp2)
        if (exp1 != exp2):
            print("La condición se cumple")
            return True
        else:
            print("La condición no se cumple")
            return False
    
    prueba_op = re.split(r"==", cond, 1)        # Busca una afirmación
    if (len(prueba_op) > 1):
        print("Entró a afirmación")
        # Se usa recursividad para calcular el valor de ambas expresiones
        exp2 = obtenerValor(prueba_op[1], results_acc, pila, True)
        exp1 = obtenerValor(prueba_op[0], results_acc, pila, True)
        print("exp1:", exp1)
        print("exp2:", exp2)
        if (exp1 == exp2):
            print("La condición se cumple")
            return True
        else:
            print("La condición no se cumple")
            return False

def pilaError(esperaba):
    cont=0
    k=""
    for i in esperaba:
        k+=str(i)
        if(cont<len(esperaba)-1):
            k+=" o "
        cont+=1
    return str(k)

def pilaCadena(pila):
    k=""
    for i in pila:
        # Si i es de tipo token
        if isinstance(i, token_tipo_val):
            # Si es un tipo de dato con valor almacenado
            if (i.get_tipo()=="id") or (i.get_tipo()=="nint") or (i.get_tipo()=="varcadena") or (i.get_tipo()=="nfloat") or (i.get_tipo()=="literalcar"):
                k+=i.get_tipo()+"."
                #Si es de tipo id, añadir comillas
                if (i.get_tipo()=="id"):
                    k+='"'+i.get_val()+'"'
                else:
                    k+=i.get_val()
            # Si es otro tipo de dato
            else:
                k+=i.get_tipo()
        # Si i es estado o no terminal
        else:
            k+=str(i)
        k+=" "
    return str(k)

def buscarSeEsperaba(estado,variable,simbolos):
    esperaba=[]
    for simbolo in simbolos:
        clave=(estado,simbolo[1])
        if(clave in variable):
            contenido=variable[clave]
            cont=contenido.cget("text")
            if(cont[0]=='d' or cont[0]=='r'):
                esperaba.append(simbolo[0])
    return esperaba

def buscarAccion(variable,estado,posTira):  #esta es una funcion que busca la accion en la tabla de analisis sintactico
    for var in variable:
        clave=(estado,posTira)
        if(var==clave):
            contenido=variable[var]
            cont=contenido.cget("text")
            return cont
    return None

def buscarSimbolo(simbolos,tira): #esta es una funcion que busca el simbolo en la tira de tokens pero asocia el simbolo con el numero de columna
    if isinstance(tira, token_tipo_val):
        print("tira:",tira.get_tipo())
        for simbolo in simbolos:
            if(simbolo[0]==tira.get_tipo()):
                return simbolo[1]
    else:
        print("tira:",tira)
        for simbolo in simbolos:
            if(simbolo[0]==tira):
                return simbolo[1]
    return None

def limpiar(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()
    direccionArchivo=""
    encabezado(ventana)
    

direccionArchivo2=""
tiraTokens=""