#! /usr/bin/python
#-*- coding: utf-8 -*-
import sys
import math
import copy
from Eleve import *
from Groupe import *
from parser import *

# Initialisation des données




def satisfactionGenerale(groupes):
     sg=0
     n = len(groupes)
     for groupe in groupes:
             sg=sg+groupe.getNote()
     return sg//n #division entière pour obtenir la mention correspondante


groupes = []




res = parseCSV(sys.argv[1])
matrice = res[0]
listeEleves = res[1]
matriceInt = convertToInt(matrice)
eleves=[]
k=0
listePref=[]

while(k<len(listeEleves)):
    eleve=Eleve(k,listeEleves[k],"")
    l=0
    while(l<len(listeEleves)):
        eleve.mentions.append(matriceInt[k][l])
        l+=1
    eleves.append(eleve)
    k+=1


def affecterUnEleve(eleve):
   eleveAajouter=e
   d=False
   for g in groupes:
      gProvisoire=Groupe()
      gProvisoire.eleves.append(g.eleves[0])
      gProvisoire.eleves.append(g.eleves[1])
      gProvisoire.eleves.append(e)
      if ((g.calculSatisfaction()<=gProvisoire.calculSatisfaction() or gProvisoire.calculSatisfaction()>=mention["P"])  and d==False and len(g.eleves)<3 ):
         d=True #TODO: donner un vrai nom de variable 
         e.setGroupe(g)
         g.eleves.append(e)

elevesBis=eleves
elevesChoisis=[]
l=[]
for eleve in eleves:
        l.append(eleve.trierEleves(eleves))
k=0
#TODO: redéfinir les noms de variables 
for liste in l:
  for e in liste:
    if(e.id==k):
      liste.remove(e)
  k+=1



 #Trier les eleves

 #former des binomes
m=0
elevesU=eleves
elevesAffectes=[]
elevesChoisis=[]
m=0
for e in eleves:
    if (not (e in elevesAffectes)):
        j=0
        i=0
        b=False
        while(j<len(l) and b==False):
                while((l[j][i] in elevesAffectes)==False and i<len(l[j]) and b==False):
                        g1=Groupe()
                        e.setGroupe(g1)
                        l[j][i].setGroupe(g1) 
                        g1.eleves.append(l[j][i])
                        g1.eleves.append(e)
                        satisfactionBinome=g1.calculSatisfaction()
                        if(satisfactionBinome<mention["AB--"] ):
                                  b=False
                        elif (m<18 and l[j][i]!=e ): #si je dépasse pas 18 groupes
                              elevesAffectes.append(e)
                              elevesAffectes.append(l[j][i])
                              groupes.append(g1)
                              m=m+1
                              elevesChoisis1=e
                              elevesChoisis2=l[j][i]
                              b=True
                        i=i+1
                j=j+1

elevesU=eleves
elevesRestants=[value for value in elevesU if value not in elevesAffectes]

elevesRestantsAff=[]

if(m<18):
    if(len(elevesRestants)%2!=0 and len(elevesRestants)>1 ): #s'il reste plus d'un joueur
        i=0
        while(i<len(elevesRestants) and m<18 ):
                if(not(elevesRestants[i] in elevesRestantsAff) ):
                        g=Groupe()
                        elevesRestants[i].setGroupe(g)
                        elevesRestants[i+1].setGroupe(g)
                        g.eleves.append(elevesRestants[i])
                        g.eleves.append(elevesRestants[i+1])
                        elevesRestantsAff.append(elevesRestants[i])
                        elevesRestantsAff.append(elevesRestants[i+1])
                        groupes.append(g)
                        print("il reste ",len(elevesRestants)-len(elevesRestantsAff) ,"a affecter")
                        m=m+1
                i+=1

    elif ((len(elevesRestants)%2==0) and len(elevesRestants)>1):
         i=0
         while(i<len(elevesRestants) and m<18):
          if(not(elevesRestants[i] in elevesRestantsAff) and  not(elevesRestants[i+1] in elevesRestantsAff)):
              g=Groupe()
              elevesRestants[i].setGroupe(g)
              elevesRestants[i+1].setGroupe(g)
              g.eleves.append(elevesRestants[i])
              g.eleves.append(elevesRestants[i+1])
              elevesRestantsAff.append(elevesRestants[i])
              elevesRestantsAff.append(elevesRestants[i+1])
              print("il reste ",len(elevesRestants)-len(elevesRestantsAff) ,"a affecter")
              groupes.append(g)
              m=m+1
          i+=1  
    elif (len(elevesRestants)==1):
           affecterUnEleve(elevesRestants[0])
           elevesRestantsAff.append(elevesRestants[0])
if(m==18):
      b=[value for value in elevesRestants if value not in elevesRestantsAff]
      for e in b:
         affecterUnEleve(e)
         elevesRestantsAff.append(e)
         print("il reste ",len(elevesRestants)-len(elevesRestantsAff) ,"a affecter")


# récupérer le groupe qui à la note la plus petite
def minGroupe(groupes):
        min_groupe = groupes[0]
        for groupe in groupes:
                if(min_groupe.getNote()>groupe.getNote()):
                        min_groupe = groupe
        return min_groupe

# récupérer l'élève dont la satisfaction est la plus faible
def minEleve(groupe):
        min_eleve = groupe.eleves[0]
        for eleve in groupe.getEleves():
                if(min_eleve.getNote()>eleve.getNote()):
                        min_eleve = eleve
        return min_eleve

def permutation(e1, e2,groupesProvisoire):
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
        groupe2.eleves.remove(etudiant2)

        # On sauvegarde le groupe de e1
        tampon = groupe1
        # On lui attribue le groupe g2, on l'ajoute dans g2
        etudiant1.setGroupe(etudiant2.getGroupe())
        etudiant1.getGroupe().setEleve(etudiant1)
        #groupe1.calculSatisfaction()
        # On enlève e2 de son groupe, on lui attribue le groupe g1, on l'ajoute dans g1
        groupe1.eleves.remove(etudiant1)
        etudiant2.setGroupe(tampon)
        etudiant2.getGroupe().setEleve(etudiant2)
      
        return groupesProvisoire



i = 0

for groupe in groupes:
        print("\n\nGroupe ", i+1, " -> Satisfaction :", groupe.getNote(), end="\n[ ")        
        for eleve in groupe.getEleves():
                print(eleve.prenom, sep="", end=" ")                
        i+=1
        print("]")
print("\n\nLA SATISFACTION GENERALE EST DE:")

print(satisfactionGenerale(groupes))
groupesProvisoire=groupes
sfg=satisfactionGenerale(groupes)
a=0
# Initialisation

for eleve in elevesBis:
    for e in elevesBis:
                  if(e!=eleve):
                    a+=1
                    sAncienGroupe1=e.getGroupe().calculSatisfaction()
                    sAncienGroupe2=eleve.getGroupe().calculSatisfaction()
                    groupesProvisoire=permutation(eleve,e,groupesProvisoire)
                    sNouveauGroupe1=e.getGroupe().calculSatisfaction()
                    sNouveauGroupe2=eleve.getGroupe().calculSatisfaction()
                    
                    if (sfg<satisfactionGenerale(groupesProvisoire) and sAncienGroupe1<=sNouveauGroupe1 and sAncienGroupe2<=sNouveauGroupe2 ):
                        sfg=satisfactionGenerale(groupesProvisoire)
                    else:
                      groupesProvisoire=permutation(e,eleve,groupesProvisoire)

print("nous avons teste",a,"Possibilite")
print("apres l'algo")

# intervertir l'élève dont la satisfaction est minimale avec un autre élève d'un autre groupe où la satisfaction est >=
i = 0

for groupe in groupesProvisoire:
        print("\n\nGroupe ", i+1, " -> Satisfaction :", groupe.getNote(), end="\n[ ")
        for eleve in groupe.getEleves():
                print(eleve.prenom, sep="", end=" ")
        i+=1
        print("]")

print("\n\nLA SATISFACTION GENERALE EST DE :")
print(satisfactionGenerale(groupes))

#
