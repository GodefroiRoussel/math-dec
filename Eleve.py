#! /usr/bin/python3.5
#-*- coding: utf-8 -*-


class Eleve:

    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getSatisafactions(self):
        return self.mentions

    def setSatisfaction(self, liste):
        self.mentions = liste

    def S(self, ei):
        """ Fonction permettant de retourner la satisfaction de l'élève sur un élève ei
        @In  : ei = indice de l'élève
        @Out : Satisfaction envers cet élève.
        """
        return self.mentions[i]
