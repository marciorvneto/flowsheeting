class Vertice:
    def __init__(self,nome='Vertice',listaEntradas=None,listaSaidas=None):
        self.listaEntradas=listaEntradas
        if listaEntradas==None:
            self.listaEntradas=[]
        self.listaSaidas=listaSaidas
        if listaSaidas==None:
            self.listaSaidas=[]
        self.nome=nome
    def __repr__(self):
        return self.nome
    def addEntrada(self,entrada):
        self.listaEntradas.append(entrada)
    def addSaida(self,saida):
        self.listaSaidas.append(saida)
    def getEntradas(self):
        return self.listaEntradas
    def getSaidas(self):
        return self.listaSaidas

def conectaOneWay(VA,VB):
    VA.addSaida(VB)
    VB.addEntrada(VA)

def conectaTwoWay(VA,VB):
    conectaOneWay(VA,VB)
    conectaOneWay(VB,VA)

def SW(inicio):
    


A=Vertice('A')
B=Vertice('B')
C=Vertice('C')
D=Vertice('D')
E=Vertice('E')
F=Vertice('F')
G=Vertice('G')
H=Vertice('H')
I=Vertice('I')
J=Vertice('J')
K=Vertice('K')
L=Vertice('L')
M=Vertice('M')

conectaOneWay(A,B)
conectaOneWay(B,C)
conectaOneWay(C,M)
conectaOneWay(M,E)
conectaOneWay(C,D)
conectaOneWay(D,E)
conectaOneWay(D,L)
conectaOneWay(F,G)
conectaTwoWay(G,H)
conectaOneWay(H,D)
conectaOneWay(E,I)
conectaOneWay(I,L)
conectaOneWay(L,E)
conectaOneWay(I,J)
conectaOneWay(J,K)
conectaOneWay(H,C)

