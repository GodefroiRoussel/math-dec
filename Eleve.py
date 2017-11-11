#! /usr/bin/python3.5
#-*- coding: utf-8 -*-

from mention import mention#dictionnaire des mentions
from Groupe import *

class Eleve:

    def __init__(self, id, prenom, nom):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.g = Groupe();

    def getId(self):
        return self.id

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getRanking(self):
        return self.liste

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
        return self.mentions[ei-1] #car ei est indexé à 1

    def setGroupe(self, groupe):
        self.g = groupe

    def getGroupe(self):
        return self.g

    def getNote(self):
        return self.note

    def calculNote(self):
        """ Fonction retournant la note d'un élève par rapport à son groupe. C'est-à-dire sa satisfaction minimale.
        @In  :
        @Out :  note de l'élève comprise entre 0 et 10
        """
        eleves = self.getGroupe().getEleves()
        satisfaction = mention["TB"]
        for eleve in eleves:
            if (self != eleve and self.S(eleve.getId())<satisfaction):
                satisfaction = self.S(eleve.getId())
        self.note = satisfaction

    def trierMentions(self):
        """Fonction pour trier les mentions"""
        return self.mentions.sort()

    def trierEleves(self):
        """ Fonction retournant la liste des eleves triés par ordre croissant selon la satisfaction.
        @In  :
        @Out :  liste des eleves triés
        """
        eleves = self.getGroupe().getEleves()
    	self.liste=[]
    	self.mentions=self.trierMentions()
    	#self.mentions.remove("X") Bug je ne sais pas pourquoi

    	for eleve in eleves:
    		if (S(e,e1)==mention["TB"]):
    		      self.liste.append(e1)

    	for eleve in eleves:
    		if (S(e,e1)==mention["B"]):
    		      self.liste.append(e1)
    	for eleve in eleves:
    		if (S(e,e1)==mention["AB"]):
    		      self.liste.append(e1)
    	for eleve in eleves:
    		if (S(e,e1)==mention["P"]):
    		      self.liste.append(e1)
    	for eleve in eleves:
    		if (S(e,e1)==mention["I"]):
    		      self.liste.append(e1)

    	for eleve in eleves:
    		if (S(e,e1)==mention["AR"]):
    		      self.liste.append(e1)
        return self.liste
