
#Definimos las clases que utilizaremos para la construccion del automata de thompson        
class Transition:
    
    def __init__(self, sy = None, st = None):
        symbol = ""
        next_state = -1
        
    def __init__(self, sy, st):
        self.symbol = sy
        self.next_state = st
    
    def getSymbol(self):
        return self.symbol
    
    def getState(self):
        return self.next_state
    
    def setSymbol(self, sy):
        self.symbol = sy
    
    def setState(self, st):
        self.next_state = st
        
    def __str__(self):
        return "Symbol: " + self.symbol + " Next State: " + str(self.next_state)+ "\n"
        

class State:
    def __init__(self, i, transition, ini, fin):
        self.id = i #Id es el numero de estado
        self.l_transitions = []
        if transition != None:
            self.l_transitions = [transition] #Lista de 
        self.initial_state = ini
        self.final_state = fin
    
    def getIniState(self):
        return self.initial_state
    
    def getFinalState(self):
        return self.final_state
    
    def getTransitions(self):
        return self.l_transitions
    
    def getId(self):
        return self.id
    
    def setIniState(self, i):
        self.initial_state = i
    
    def setFinalState(self, f):
        self.final_state = f
    
    def setId(self, i):
        self.id = i
        
    def addTransition(self, t):
        if (self.getTransitions() == None):
            self.l_transitions = []
        self.l_transitions.append(t)
    
    def displayTransitions(self):
        i = 0
        NTransitions = len(self.l_transitions)
        for s in self.l_transitions:
            if (self.l_transitions[i] != None and i < NTransitions):
                print("To State: " + str(self.l_transitions[i].getState()) + " with Symbol: " + self.l_transitions[i].getSymbol())
                i+=1
    
    def __str__(self):
        return "Id: " + str(self.id) + " | Initial State: " + str(self.initial_state) + " | Final State: " + str(self.final_state) + "\n"
    

#Para la lista _______________________________________________________________________

# Definición de la clase Node

class Node:
    def __init__(self, s):
        self.state = s
        self.next = None

# Clase para la lista enlazada
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, state):
        new_node = Node(state)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def prepend(self, state):
        new_node = Node(state)
        new_node.next = self.head
        self.head = new_node

    def delete(self, state):
        if not self.head:
            return

        if self.head.state == state:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.state == state:
                current.next = current.next.next
                return
            current = current.next 
    
    def getTail(self): #Obtiene el ultimo estado de la lista
        current = self.head
        while current.next:
            current = current.next
        return current.state
    
    def getLastNode(self): #Obtiene el ultimo nodo de la lista
        current = self.head
        while current.next:
            current = current.next
        return current
    
    def getNode(self, n):
        if not self.head:
            return None
        count = 1
        current = self.head
        while current.next:
            current = current.next
            count+=1
        return count
    
    def CountNodes(self):
        if not self.head:
            return None
        count = 1
        current = self.head
        while current.next:
            current = current.next
            count+=1
        return count
    
    def concatenateWith(self, List):
        self.getLastNode().next = List.head
    
    def display(self):
        current = self.head
        while current:
            print(current.state)
            current.state.displayTransitions()
            current = current.next
            if current != None:
                print(end=" -> ")
    

'''
____________________________________________________________________________________________________

Se planea hacer una función por cada uno de los casos posibles

____________________________________________________________________________________________________
'''
def CorrectNumerarion(List, adder): 
    current = List.head
    while current:
            current.state.setId(current.state.getId()+adder)  
            if current.state.getTransitions() != None: #Se añadio esta condicion para evitar errores
                for t in current.state.l_transitions:
                    t.setState(t.getState() + adder)
            current = current.next 
    return


def SingleLetter(sym):
    List_SingleLetter = LinkedList()
    t = Transition(sym, 1)
    state1 = State(0, t, True, False)
    state2 = State(1,None, False, True)
    
    #Creamos el nodo
    List_SingleLetter.append(state1)
    List_SingleLetter.append(state2)

    #List_SingleLetter.display()
    return List_SingleLetter

def Concatenation(L1,L2):
    #Quitamos que el estado final de la primera lista sea final
    L1.getTail().setFinalState(False)
    
    #Corregimos la numeracion de las transiciones de la segunda lista  y
    #Copiamos las transiciones del estado que se va a borrar 
    for t in L2.head.state.l_transitions:
        t.setState(t.getState() + 1)
        L1.getTail().addTransition(t)

    #Eliminamos el estado inicial de la segunda lista    
    L2.delete(L2.head.state)
    
    #Corregimos la numeracion de la segunda lista aumentandole 1 a cada estado
    CorrectNumerarion(L2,1)
    
    #Concatenamos las listas
    L1.concatenateWith(L2)
    
    #Imprimimos la lista
    L1.display()
    
    return L1
    

def Union(L1, L2): #L1 y L2 son listas enlazadas
    CorrectNumerarion(L1,1)
    L1.head.state.setIniState(False) #El primer estado de la primera lista ya no es inicial
    #Obtenemos el ultimo id para poder numerar los estados de la segunda lista
    sum = L1.getTail().getId() + 1 
    sum  = sum - L2.head.state.getId()
    CorrectNumerarion(L2,sum)
    #Una vez corregidas las numeraciones concaenetamos las listas
    t1 = Transition("λ",L1.head.state.getId()) #Enlace con la primera lista
    t2 = Transition("λ",L2.head.state.getId()) #Enlace con la primera lista
    state1 = State(0, t1, True, False) #El que se va a agregar al inicio
    state1.addTransition(t2)
    
    
    L1.prepend(state1)
     
    state2 = State(L2.getTail().getId()+1,None, False, True) #El que se va a agregar al final
   
    
    #Corregimos la bandera de estado final, añadimos la transicion y añadimos el último estado
    t3 = Transition("λ", L2.getTail().getId()+1) #Transicion para el que se agrega al final, se agrega al último de ambas litas
    #print(t3)
    L1.getTail().setFinalState(False)
    L2.getTail().setFinalState(False)

    L1.getTail().addTransition(t3)    
    L2.getTail().addTransition(t3)

    L2.append(state2)
    
    L1.concatenateWith(L2)

    #Imprimimos la lista
    #L1.display()
    
    return L1
    
def Cerradura_de_Kleene(List): #Recibe como parametro una única lista enlazada
    #Creamos las transiciones nueva y estados nuevos
    CorrectNumerarion(List,1) #Corregimos la numeracion de la lista
    
    List.head.state.setIniState(False) #El primer estado de la lista ya sera el inicial
    List.getTail().setFinalState(False) #El ultimo estado de la lista ya no sera final
    
    t1 = Transition("λ",List.head.state.getId())  #Transicion para llegar a la lista
    t2 = Transition("λ",List.getTail().getId()+1) #Transicion con el edo final
    state1 = State(0,t1,True,False) #Declaramos el nuevo estado inicial
    state1.addTransition(t2) 
    List.prepend(state1) #Añadimos el estado inicial a la lista
    
    state2 = State(List.getTail().getId()+1,None,False,True) #Declaramos el nuevo estado final
    t3 = Transition("λ",List.getTail().getId()+1) #Transicion para llegar al estado final
    t4 = Transition("λ",List.head.state.getId()+1) #Transicion para llegar al estado inicial + 1 (Lo que lo hace while)
    List.getTail().addTransition(t3) #Añadimos la transicion al estado final de la lista
    List.getTail().addTransition(t4) 
    List.append(state2) #Añadimos el estado final a la lista
    
    List.display()
    
    return List
    

def Cerradura_opcional(L):
    #Corregimos la numeracion de la lista, añadindo 1 porque agregaremos un nuevo edo inicial
    CorrectNumerarion(L,1)
    #Corregimos la bandera de estado inicial del primer estado de la lista
    L.head.state.setIniState(False)
    #Corregimos la bandera de estado final del ultimo estado de la lista
    L.getTail().setFinalState(False)
    #Creamos las transiciones nuevas y estados nuevos
    
    t1 = Transition("λ",L.head.state.getId()) #Transicion para llegar a la lista
    t2 = Transition("λ",L.getTail().getId()+1) #Transicion para llegar al estado final
    state1 = State(0,t1,True,False) #Declaramos el nuevo estado inicial
    state1.addTransition(t2)
    
    L.prepend(state1) #Añadimos el estado inicial a la lista
    
    t3 = Transition("λ",L.getTail().getId()+1) #Transicion para llegar al estado final
    L.getTail().addTransition(t3) #Añadimos la transicion al estado final de la lista
    state2 = State(L.getTail().getId()+1,None,False,True) #Declaramos el nuevo estado final
    L.append(state2) #Añadimos el estado final a la lista
    
    #Impresion de la lista
    L.display()
    
    return L

def Cerradura_Positiva(L):
    #Corregimos la numeracion de la lista, ya que añadiremos un nuevo estado inicial
    CorrectNumerarion(L,1)
    #Corregimos la bandera de estado inicial del primer estado de la lista
    L.head.state.setIniState(False)
    #Corregimos la bandera de estado final del ultimo estado de la lista
    L.getTail().setFinalState(False)
    
    #Creamos las transiciones nuevas y estados nuevos
    t1 = Transition("λ",L.head.state.getId()) #Transicion para llegar a la lista
    state1 = State(0,t1,True,False) #Declaramos el nuevo estado inicial
    L.prepend(state1) #Añadimos el estado inicial a la lista
    
    t2 = Transition("λ",L.getTail().getId()+1) #Transicion para llegar al estado final
    t3 = Transition("λ",L.head.state.getId()+1) #Transicion para llegar al estado inicial + 1
    L.getTail().addTransition(t2) 
    L.getTail().addTransition(t3)
    state2 = State(L.getTail().getId()+1,None,False,True) #Declaramos el nuevo estado final
    L.append(state2) #Añadimos el estado final a la lista
    
    return L   
    
'''
____________________________________________________________________________________________________


SCRIPT PRINCIPAL

____________________________________________________________________________________________________
'''

L1 = SingleLetter("a")
L2 = SingleLetter("b")

#L1 = Union(L1,L2)
#Concatenation(L1,L2)
#Cerradura_de_Kleene(L1)
#Cerradura_opcional(L1)