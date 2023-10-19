
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
    
    def display(self):
        current = self.head
        while current:
            print(current.state)
            current.state.displayTransitions()
            current = current.next
            if current != None:
                print(end=" -> ")
    
    def display2(self):
        current = self.head
        current = current.next2
        while current:
            if current != None:
                print(end=" -> ")
            print(current.state)
            current.state.displayTransitions()
            current = current.next 

'''
____________________________________________________________________________________________________

Se planea hacer una función por cada uno de los casos posibles

____________________________________________________________________________________________________
'''
def CorrectNumerarion(List, adder): 
    current = List.head
    while current:
            current.state.setId(current.state.getId()+adder)  
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
     
    #Generamos el nuevo nodo
    #aux_state = L1.head
    
    L1.getLastNode().next = L2.head

    #L1.append(aux_state)
    
    #Imprimimos la lista
    L1.display()

    
    return L1
    
    
'''
____________________________________________________________________________________________________


SCRIPT PRINCIPAL

____________________________________________________________________________________________________
'''

L1 = SingleLetter("a")
L2 = SingleLetter("b")

L2 = Union(L1,L2)