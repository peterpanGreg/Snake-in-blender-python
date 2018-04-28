from random import choice


class Table():
    def __init__(self,x,y):
        self.cord={}
        for i in range(y):
            for k in range(x):
                self.cord[(k,i)]=True
        self._keys=[]
        for i in self.cord.keys():
            self._keys.append(i)
        self._values=[]
        for i in self.cord.values():
            self._values.append(i)

    def __repr__(self):
        return  str(self.cord)
    
    def __iter__(self):
        return iter(self.cord)

    def __getitem__(self,cord):
        return self.cord[cord]
    
    def __setitem__(self,cord,value):
        if (cord in self.cord)==True:
            self.cord[cord]=value
    
    def __contains__(self,i):
        return i in self.cord

    def keys(self):
        """Renvoie toutes les cordonnées de l'objet sous forme de liste"""
        return self._keys

    def values(self):
        """Renvoie tous les états des cordonnées de l'objet sous forme de liste"""    
        return self._values

    def items(self):
        """Renvoie une liste [ (cordonnées,état) , (...) , ... ]"""
        a=[]
        for i in self.cord.items():
            a.append(i)
        return a    

    def remplir(self,cord=None):
        """Change l'état d'une ou plusieures cordonnée(s) True=>False"""
        if cord==None:
            for key in self:
                self.cord[key]=False
        elif len(cord)==2 and (cord in self.cord)==True:
            self.cord[cord]=False
 
                
    def nettoyer(self,cord=None):
        """Change l'état d'une ou plusieures cordonnée(s) False=>True"""
        if cord==None:
            for key in self:
                self.cord[key]=True
        elif len(cord)==2 and (cord in self.cord)==True:
            self.cord[cord]=True


class Pomme:
    def __init__(self,cords,cord=None):
        self.cords=cords
        if cord!=None:
            self.cord=(cord)
        else:    
            cord=choice(cords.keys())
            good=False
            while good!=True:
                if cords[cord]==True:
                    self.cord=cord
                    good=True
    
    def __repr__(self):
        return repr(self.cord)
    
    def __len__(self):
        return len(self.cord)
    
    def change(self):
        cord=choice(self.cords.keys())
        good=False
        while good!=True:
            if self.cords[cord]==True:
                self.cord=cord
                good=True

class Serpent:
    def __init__(self,cord=[(5,2),(4,2),(3,2),(2,2)],direct="E",cords=None):
        self.cord=cord
        self.tete=cord[0]
        self.queue=cord[1:]
        self.bout=cord[len(cord)-1]
        self.direct=direct
        x=0
        y=0
        for _x,_y in cords:
            if _x>x:
                x=_x
            if _y>y:
                y=_y
        self.limite=(x,y)
        
    def __repr__(self):
        return repr(self.cord)
    
    def __len__(self):
        return len(self.cord)
    
    def __iter__(self):
        return iter(self.cord)

    def __contains__(self,cord):
        return cord in self.cord

    def avancer(self,direct):
        if direct=='N':
            x,y=self.tete
            cord=[(x,y-1)]
            for key,i in enumerate(self.queue):
                cord.append(self.cord[key])
            self.cord=cord
            self.tete=cord[0]
            self.queue=cord[1:]
            self.direct=direct
        elif direct=='S': 
            x,y=self.tete
            cord=[(x,y+1)]
            for key,i in enumerate(self.queue):
                cord.append(self.cord[key])
            self.cord=cord
            self.tete=cord[0]
            self.queue=cord[1:]
            self.direct=direct
        elif direct=='W':
            x,y=self.tete
            cord=[(x-1,y)]
            for key,i in enumerate(self.queue):
                cord.append(self.cord[key])
            self.cord=cord
            self.tete=cord[0]
            self.queue=cord[1:]
            self.direct=direct
        elif direct=='E':
            x,y=self.tete
            cord=[(x+1,y)]
            for key,i in enumerate(self.queue):
                cord.append(self.cord[key])
            self.cord=cord
            self.tete=cord[0]
            self.queue=cord[1:]
            self.direct=direct

    def avancer_bout(self):
        self.bout=self.cord[len(self.cord)-1]

    def ajout(self):
        self.cord.append(self.bout)
        self.queue=self.cord[1:]    
        
    def perdre(self):
        if (self.tete in self.queue)==True or \
        self.tete[0]>self.limite[0] or self.tete[1]>self.limite[1]\
        or self.tete[0]<0 or self.tete[1]<0:
            return True
    