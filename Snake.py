from Function import *
from Entree_sortie import *

cont=logic.getCurrentController()
own=cont.owner

table=Table(20,20)
snake=Serpent(cords=table)
aple=Pomme(table)
direct=Direct("E")
score = len(snake)

for i in snake:
    table.remplir(i)
table.remplir(aple)

def Main():
    
    direct.change()                 #entrées
    
    snake.avancer(direct.direct)    #avancer du Serpent
    
    for i in snake:                 #remplissage des cordonées
        table.remplir(i)
    
    table.remplir(aple)
    
    if snake.tete==aple.cord:       #ajout si besoin d'une cordonnée au Serpent
        snake.ajout()
        aple.change()
    
    score=len(snake)-4                #mise à jour du score
        
    snake.avancer_bout()            #avancer le bout du Serpent
    

    print(snake.tete)
    print(direct)
    

    #rendu
    Rendu(snake,aple)
    
    if snake.perdre()==True:          #PERDU!!!!!!!!!
        print("PERDU!!!!!!")
        cont.activate(own.actuators["Fin"]) 
        
         
    table.nettoyer()                   #nettoyage des cordonées

