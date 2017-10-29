#! /usr/bin/python
#-*- coding: utf-8 -*-

import math
import copy
from Eleve import *
from Groupe import *

# Initialisation des données

#print("Veuillez entrer le nombre d'étudiants :")
#n = int(input())
n = 37

nbTrinome = n // 3
#s'il nous reste une personne orphelin on enlève un trinome pour former des binomes à la place
if(n-nbTrinome*3 == 1):
        nbTrinome-=1

#nbTrinome = 0
nbBinome = (n - nbTrinome*3) // 2 
#nbBinome = 5

print("Nombre d'élève :" , n)
print("Trinomes: " , nbTrinome)
print("Binomes: " , nbBinome)

#TODO: Un système pour rentrer manuellement les données et non pas dans le code

e1 = Eleve(1,"Godefroi","Roussel")
e1.setSatisfaction(["X","I","B","P","TB","AB","P","P","B","AB"])
e2 = Eleve(2,"Kévin","Hassan")
e2.setSatisfaction(["B","X","AB","I","AR","AR","AR","B","TB","AB"])
e3 = Eleve(3,"Soufiane","Benchraa")
e3.setSatisfaction(["AB","P","X","P","I","P","TB","AB","B","I"])
e4 = Eleve(4,"Pierre","Durand")
e4.setSatisfaction(["B","TB","TB","X","B","AB","B","I","AB","AR"])
e5 = Eleve(5,"Maximme","Dupont")
e5.setSatisfaction(["TB","I","P","P","X","AB","B","I","AB","AR"])
e6 = Eleve(6,"Aurélien","Cotentin")
e6.setSatisfaction(["AB","B","TB","TB","TB","X","B","AR","I","AR"])
e7 = Eleve(7,"Guillaume","Tranchant")
e7.setSatisfaction(["I","AR","AR","AR","AR","AR","X","AR","TB","AR"])
e8 = Eleve(8,"Clément","Farge")
e8.setSatisfaction(["B","AB","B","P","P","AB","TB","X","B","AR"])
e9 = Eleve(9,"Evelyne","Dhélia")
e9.setSatisfaction(["B","AR","I","B","TB","AB","AB","B","X","AR"])
e10 = Eleve(10,"Charlie","Brown")
e10.setSatisfaction(["AB","TB","TB","I","TB","P","AB","B","P","X"])

eleves = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
groupes = []

#eleves = []
#for i in range(0, n):
        #print("Entrer le nom :" )
        #nom = input()        
        #print("Entrer le prénom :")
        #prenom = input()
        #e = Eleve(prenom,nom)
        #try:
                #print("Entrer les mentions sur les autres éléves séparées par des virgules [TB,B,AB,P,I,AR] :")
                #mentions = input().upper().split(',')
                #mentions = mentions[:i]+["X"]+mentions[i:] #ajouter une note pour soi même 
                #if(len(mentions)!=n):
                        #raise Exception("Il manque des mentions")
                #e.setSatisfaction(mentions)
                #print(mentions)
                #eleves.append(e)
        #except Exception as e : #vérifier que la taille est de n
                #print("Erreur :", e)
                #exit()
        

#TODO: Faire pour tous les binomes et trinomes possibles
#Ici cela ne concerne que cet exemple précis
for i in range(0,5):
        g = Groupe()
        eleves[0].setGroupe(g)
        eleves[1].setGroupe(g)
        g.setEleve(eleves[0])
        g.setEleve(eleves[1])
        groupes.append(g)
        del eleves[0]
        del eleves[0]
        g.calculSatisfaction()

#for i in range(0,nbTrinome):
        #g = Groupe([eleves[0],eleves[1],eleves[2]])
        #groupes.append(g)
        #del eleves[0]
        #del eleves[0]
        #del eleves[0]
#for i in range(0,nbBinome):
        #g = Groupe([eleves[0],eleves[1]])
        #groupes.append(g)
        #del eleves[0]
        #del eleves[0]


def permutation(e1, e2):
        """ Fonction échangeant 2 élèves.
        @In :   e1 = Eleve
                e2 = Eleve
        @Out :
        """
