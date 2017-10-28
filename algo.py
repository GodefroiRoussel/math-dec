#! /usr/bin/python3.5
#-*- coding: utf-8 -*-

import math
import copy
from eleve import Eleve
from groupe import Groupe

# Initialisation des données
n = 10
#nbTrinome = n % 3
nbTrinome = 0
#nbBinome = (n - nbTrinome * 2) // 2 # // correspond à une division entière
nbBinome = 5

print(n)
print(nbTrinome)
print(nbBinome)

#TODO: Un système pour rentrer manuellement les données et non pas dans le code
e1 = Eleve("Godefroi","Roussel")
e1.setSatisfaction(["X","I","B","P","TB","AB","P","P","B","AB"])
e2 = Eleve("Kévin","Hassan")
e2.setSatisfaction(["B","X","AB","I","AR","AR","AR","B","TB","AB"])
e3 = Eleve("Soufiane","Benchraa")
e3.setSatisfaction(["AB","P","X","P","I","P","TB","AB","B","I"])
e4 = Eleve("Pierre","Durand")
e4.setSatisfaction(["B","TB","TB","X","B","AB","B","I","AB","AR"])
e5 = Eleve("Maximme","Dupont")
e5.setSatisfaction(["TB","I","P","P","X","AB","B","I","AB","AR"])
e6 = Eleve("Aurélien","Cotentin")
e6.setSatisfaction(["AB","B","TB","TB","TB","X","B","AR","I","AR"])
e7 = Eleve("Guillaume","Tranchant")
e7.setSatisfaction(["I","AR","AR","AR","AR","AR","X","AR","TB","AR"])
e8 = Eleve("Clément","Farge")
e8.setSatisfaction(["B","AB","B","P","P","AB","TB","X","B","AR"])
e9 = Eleve("Evelyne","Dhélia")
e9.setSatisfaction(["B","AR","I","B","TB","AB","AB","B","X","AR"])
e10 = Eleve("Charlie","Brown")
e10.setSatisfaction(["AB","TB","TB","I","TB","P","AB","B","P","X"])

eleves = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
groupes = []

#TODO: Faire pour tous les binomes et trinomes possibles
#Ici cela ne concerne que cet exemple précis
for i in range(0,5):
        g = Groupe([eleves[0],eleves[1]])
        groupes.append(g)
        del eleves[0]
        del eleves[0]



def permutation(e1, e2):
        """ Fonction échangeant 2 élèves.
        @In :   e1 = Eleve
                e2 = Eleve
        @Out :
        """
