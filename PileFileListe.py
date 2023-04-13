class Liste:


    def Vide():
        return Liste()


    def estVide(self):
        return self.entete is None and self.liste==[]


    def ajouteEnTete(self,x):
        if self.estVide():
            self.entete=x
        else:
            self.liste.append(self.entete)
            self.entete=x
    
    def supprEnTete(self):
        if not self.estVide():
            t=self.entete
            if len(self.liste)!=0: self.entete=self.liste.pop()
            else: self.entete=None
            return t

    def compte(self):
        if self.estVide(): return 0
        else: return len(self.liste)+1


    def __init__(self,x=None,n=[]):
        self.entete=x
        assert type(n)==list, "n, doit être une list"
        self.liste=n


    def __str__(self):
        rep="["
        for e in self.liste:
            rep+=str(e)+", "
        if self.entete is not None: rep+=str(self.entete)
        rep+="]"
        return rep

    def cons(x,L): #Méthode de classe 
        assert type(L)==Liste, "L doit être de type liste"
        l=[]
        if not L.estVide():
            for e in L.liste:
                l.append(e)
            l.append(L.entete)
        L2=Liste(x,l)
        return L2


###############################  -Fonctions isolées- ##############################################


def vide():
    return []

def estVide(L):
    assert type(L)==list, "L doit être de type list"
    return len(L)==0

def ajouteEnTete(x,L):
    assert type(L)==list, "L doit être de type list" 
    L.append(x)

def supprEnTete(L):
    assert type(L)==list, "L doit être de type list"
    if not estVide(a):
        x=L.pop()
        return x
    
def compte(L):
    assert type(L)==list, "L doit être de type list"
    return len(L)

def cons(x,L=[]):
    assert type(L)==list, "L doit être de type list"
    L2=[]
    for e in L:
        L2.append(e)
    L2.append(x)
    return L2

def insert(L,x,y):
    assert type(L)==list, "L doit être de type list"
    assert type(y)==int, "l'indice doit être un entier"
    assert y>=0,"l'indice ne doit pas être négatif"
    assert y<len(L),"l'indice doit être dans la taille du tableau"
    m=[]
    for k in range(len(L)):
        if k==y:
            m.append(x)
        m.append(L[k])
    L=m
    return L

def retire(L,y):
    assert type(L)==list, "L doit être de type list"
    assert type(y)==int, "l'indice doit être un entier"
    assert y>=0,"l'indice ne doit pas être négatif"
    assert y<len(L),"l'indice doit être dans la taille du tableau"
    m=[]
    for k in range(len(L)):
        if k==y:
            continue
        m.append(L[k])
    L=m
    return L
    
###########################################################################

######################  -Liste Chainée (Class Maillon)-  ##############################################


class Maillon: 

    def __init__(self,v=None,s=None):
        self.valeur=v
        self.suivant=s

class ListeChainee:

    def __init__(self,t):
        assert type(t)==Maillon,"t doit être de la classe Maillon"
        self.tete=t

    def Vide(self):
        return ListeChainee(Maillon())

    def estVide(self):
        return self.tete.valeur is None and self.tete.valeur is None 

    def ajouteEnTete(self,x):
        self.tete=Maillon(x,self.tete)

    def supprEnTete(self):
        if self.tete:
            pass

    def __str__(self):
        pass

###########################################################################

######################  -Pile (Class Pile)-  ##############################################

class Pile:

    def __init(self,tete=None,queue=[]):
        assert type(queue)==list,"La queue doit être une liste"
        self.tete=tete
        self.queue=queue

    def vide(self):
        return self.tete is None and self.queue==[]

    def pile():
        return Pile()

    def empiller (self,x):
        self.queue.append(self.tete)
        self.tete=x

    def depiller(self):
        assert self.vide()==False, "La liste ne doit pas être vide"
        a=self.tete
        self.tete=self.queue[len(self.queue)-1]
        self.queue.pop()
        return a

    def sommet(self):
        return self.tete

    def taille(self):
        return (len(self.queue)+1)


###############################  -Fonctions isolées- ##############################################

def Pile():
    return []

def Vide(P):
    return len(P)==0

def empiller(x,P):
    P.append(x)

def depiller(P):
    a=P.pop()
    return a

def sommet(P):
    return P[-1]

def taille(P):
    return len(p)


###########################################################################

######################  -File (Class File)-  ##############################################

class File:
    
    def __init__(self,tete=None,queue=[]):
        assert type(queue)==list,"La queue doit être une liste"
        self.tete=tete
        self.queue=queue
        self.enfiler(self.tete)

    def vide(self):
        return self.tete is None and self.queue==[]

    def file():
        return File()

    def enfiler(self,x):
        self.queue.insert(0,x)

    def defiler(self):
        assert self.vide()==False, "La liste ne doit pas être vide"
        a=self.tete
        self.tete=self.queue[0]
        self.queue.pop(0)
        return a

    def sommet(self):
        return self.tete

    def taille(self):
        return (len(self.queue)+1)

    def __str__(self):
        return str(self.tete)+str(self.queue)

###############################  -Fonctions isolées- ##############################################

def File():
    return []
    
def Vide2(F):
    return len(F)==0

def enfiler(F,x):
    F.append(x)

def defiller(F):
    return F.pop(0)

def sommet2(F):
    return F[0]

def taille2(F):
    return len(F)


