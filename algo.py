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
        #e = Eleve(i+1,prenom,nom)
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


elevesBis=eleves
for e in eleves:
        g1 = Groupe()
        l=e.trierEleves(eleves) #Trier les eleves
        b=False
        j=0
        while(b==False and j< len(l)):
                satisfactionBinome=l[j].S(e.id)+e.S(l[j].id)
                if (satisfactionBinome >mention["AB--"] and (e.S(l[j].id)==mention["AR"] or l[j].S(e.id)==mention["AR"] or e.S(l[j].id)==mention["I"] or l[j].S(e.id)==mention["I"]  ) ):
                        b=False
                else:
                        e.setGroupe(g1)
                        l[j].setGroupe(g1)
                        groupes.append(g1)
                        elevesBis.remove(l[j]) #supprimer l'eleve de la liste pour voir s'il va en rester des eleves pour savoir s'il nous reste des étudiants sans binome, pour faire les trinomes apres
                        b=True
                        j = j + 1


#TODO: Faire pour tous les binomes et trinomes possibles
#Ici cela ne concerne que cet exemple précis
print("Avant permutation")
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
        #g = Groupe()
        #eleves[0].setGroupe(g)
        #eleves[1].setGroupe(g)
        #g.setEleve(eleves[0])
        #g.setEleve(eleves[1])
        #groupes.append(g)
        #del eleves[0]
        #del eleves[0]
        #g.calculSatisfaction()
#for i in range(0,nbBinome):
        #g = Groupe()
        #eleves[0].setGroupe(g)
        #eleves[1].setGroupe(g)
        #eleves[2].setGroupe(g)
        #g.setEleve(eleves[0])
        #g.setEleve(eleves[1])
        #g.setEleve(eleves[2])
        #groupes.append(g)
        #del eleves[0]
        #del eleves[0]

# récupérer le groupe qui à la note la plus petite
def minGroupe(groupes):
        min_groupe = groupes[0]
        for groupe in groupes:
                if(min_groupe.getNote()>groupe.getNote()):
                        min_groupe = groupe
        return min_groupe

# récupérer l'élève dont la satisfaction est la plus faible
def minEleve(groupe):
        min_eleve = groupe.getEleves()[0]
        for eleve in groupe.getEleves():
                if(min_eleve.getNote()>eleve.getNote()):
                        min_eleve = eleve
        return min_eleve

def permutation(e1, e2):
        """ Fonction échangeant 2 élèves.
        @In :   e1 = Eleve
                e2 = Eleve
        @Out :
        """
        etudiant1 = e1
        etudiant2 = e2
        groupe1 = etudiant1.getGroupe()
        groupe2 = etudiant2.getGroupe()
        # On enlève e1 de son groupe
        groupe1.removeEleve(etudiant1)
        # On sauvegarde le groupe de e1
        tampon = groupe1
        # On lui attribue le groupe g2, on l'ajoute dans g2
        etudiant1.setGroupe(etudiant2.getGroupe())
        etudiant1.getGroupe().setEleve(etudiant1)
        groupe1.calculSatisfaction()
        # On enlève e2 de son groupe, on lui attribue le groupe g1, on l'ajoute dans g1
        groupe2.removeEleve(etudiant2)
        etudiant2.setGroupe(tampon)
        etudiant2.getGroupe().setEleve(etudiant2)
        groupe2.calculSatisfaction()
        return [groupe2,groupe1]#retourne les 2 groupes permutés


min_groupe = minGroupe(groupes)
min_eleve = minEleve(min_groupe)

i = 0
for groupe in groupes:
        print("Groupe ", i+1, "Note :", groupe.getNote())
        for eleve in groupe.getEleves():
                print(eleve.getNom())
        i+=1

# intervertir l'élève dont la satisfaction est minimale avec un autre élève d'un autre groupe où la satisfaction est >=
for groupe in groupes:
        if min_groupe != groupe:
                #dans le cas d'un groupe différent de celui avec qui on veut permuter
                for eleve in groupe.getEleves():
                        # on prend l'élève dont la note est supérieur ou égale à notre élève à permuter
                        if(eleve.getNote()>= min_eleve.getNote()):
                                #on le permute
                                l = permutation(min_eleve,eleve)
                                #si on obtient un meilleur résultat alors on garde la permutation
                                if(min_groupe.getNote()<=l[0].getNote() or groupe.getNote()>=l[1].getNote()):
                                        min_groupe = l[0]
                                        groupe = l[1]
print("\n")
print("APRES")
i = 0
for groupe in groupes:
        print("Groupe ", i+1, "Note :", groupe.getNote())
        for eleve in groupe.getEleves():
                print(eleve.getNom())
        i+=1
		


