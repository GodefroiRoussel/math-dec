# math-dec
Ce dossier va comporter un algorithme pour attribuer des élèves dans des groupes et ensuite attribuer un projet à un groupe.



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
