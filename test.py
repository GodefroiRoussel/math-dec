#! /usr/bin/python3.5
#-*- coding: utf-8 -*-

import math
from Eleve import *
from Groupe import *

# Fonctions pour les tests
def pause():
        print("\n")
        programPause = raw_input("Press the <ENTER> key to continue...")

def permutation(e1, e2):
        """ Fonction échangeant 2 élèves.
        @In :   e1 = Eleve
                e2 = Eleve
        @Out :
        """
        # On enlève e1 de son groupe
        e1.getGroupe().removeEleve(e1)
        # On sauvegarde le groupe de e1
        tampon = e1.getGroupe()
        # On lui attribue le groupe g2, on l'ajoute dans g2
        e1.setGroupe(e2.getGroupe())
        e1.getGroupe().setEleve(e1)

        # On enlève e2 de son groupe, on lui attribue le groupe g1, on l'ajoute dans g1
        e2.getGroupe().removeEleve(e2)
        e2.setGroupe(tampon)
        e2.getGroupe().setEleve(e2)

# Initialisation des données
n = 10
nbBinome = 5

print("Nombre d'élève :" , n)
print("Binomes: " , nbBinome)

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
print("Affichage des élèves")
print(eleves)
pause()
print("\n")
print("Avant permutation")
for i in range(0,5):
        print("\n")
        print("Voici le groupe ",i)
        g = Groupe()
        eleves[0].setGroupe(g)
        eleves[1].setGroupe(g)
        g.setEleve(eleves[0])
        g.setEleve(eleves[1])
        groupes.append(g)
        del eleves[0]
        del eleves[0]
        print("La satisfaction de ce groupe est de :")
        g.calculSatisfaction()
        print("Et il est composé des élèves :")
        for eleve in groupes[i].getEleves():
                print(eleve)

pause()
print("\n")
print("\n")
print("On effectue une permutation entre e1 et e3")
print("Donc on va obtenir maintenant les groupes e1, e4 et e2, e3")
permutation(e1,e3)
for i in range(0,5):
        groupes[i].calculSatisfaction()
        for eleve in groupes[i].getEleves():
                print(eleve)

pause()
print("\n")
print("\n")
print("On effectue encore une permutation sur e1 et e3 pour vérifier que notre algorithme est stable.")
permutation(e1,e3)
for i in range(0,5):
        groupes[i].calculSatisfaction()



print("\n")
print("\n")

print(" Je trie les choix pour un eleve")
e.trierEleves(eleves)
for eleve in e.listeTriee:
print(eleve.id)

gb=Groupe()
e1.setGroupe(gb)
e5.setGroupe(gb)
e7.setGroupe(gb)
gb.eleves.append(e1)
gb.eleves.append(e5)
gb.eleves.append(e7)

print("je teste calcul satisfaction")
print(gb.calculSatisfactionBis())

