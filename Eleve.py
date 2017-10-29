#! /usr/bin/python3.5
#-*- coding: utf-8 -*-

from mention import mention#dictionnaire des mentions

class Eleve:

    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getSatisfactions(self):
        return self.mentions

    def setSatisfaction(self, liste):
        #convertie les satisfactions de l'élève en fonction des valeurs du dictionnaire
        l = []
        for i in liste:
            l.append(mention[i])
        self.mentions = l

    def S(self, ei):
        """ Fonction permettant de retourner la satisfaction de l'élève sur un élève ei
        @In  : ei = indice de l'élève
        @Out : Satisfaction envers cet élève.
        """
        return self.mentions[ei]

    def setGroupe(self, groupe):
        self.g = groupe

    def getGroupe(self):
        return self.g

    def note(self):
        return self.note

    def calculNote(self):
        """ Fonction retournant la note d'un élève par rapport à son groupe. C'est-à-dire sa satisfaction minimale.
        @In  :
        @Out :  note de l'élève comprise entre 0 et 10
        """
        eleves = self.getGroupe().getEleves()
        satisfaction = mention["TB"] 
        for eleve in eleves:
            if (self != eleve and self.S(eleve)<satisfaction):
                satisfaction = self.S(eleve)

        self.note = satisfaction
        return self.note
