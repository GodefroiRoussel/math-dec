#! /usr/bin/python3.5
#-*- coding: utf-8 -*-

class Groupe:

    def __init__(self):
        self.eleves = []

    def getNote(self):
        return self.note

    def getEleves(self):
        return self.eleves

    def setEleve(self,eleve):
        self.eleves.append(eleve)

    def removeEleve(self,eleve):
        self.eleves.remove(eleve)

    # Correspond à setNote
    def calculSatisfactionBis(self):
        """ Fonction calculant la satisfaction de ce groupe
        @In :
        @Out :
        L'ordre sera le suivant :
            AR = -130      Toutes les combinaisons avec AR
            I = -50       Toutes les combinaisons avec I
            P = -10      P + P
            P+ = 0       AB + P
            AB-- = 3     B + P
            AB- = 5   	 TB + P
            AB = 10      AB + AB
            AB+ = 13     B + AB
            B- = 15      TB + AB
            B = 16       B + B
            B+ = 18      TB + B
            TB = 20      TB + TB
        """
        self.note = 0
        for eleve in self.eleves:
            eleve.calculNote()
            self.note = self.note + eleve.getNote()

        #Si le groupe est un trinôme alors on ne fait le calcul qu'avec les 2 élèves ayant la plus petite mention.
        if len(self.getEleves()) == 3:
            if self.getEleves()[0].getNote() >= self.getEleves()[1].getNote() and self.getEleves()[0].getNote() >= self.getEleves()[2].getNote():
                e = self.getEleves()[0]
            elif self.getEleves()[1].getNote() >= self.getEleves()[0].getNote() and self.getEleves()[1].getNote() >= self.getEleves()[2].getNote():
                e = self.getEleves()[1]
            else:
                e = self.getEleves()[2]

            self.note = self.note - e.getNote()
            return self.note

    def calculSatisfaction(self):
        vote01=(self.eleves[0].S(self.eleves[1].id)+self.eleves[1].S(self.eleves[0].id))/2
        if (len(self.eleves)==2):
           return vote01
        if (len(self.eleves)==3):
           vote02=(self.eleves[0].S(self.eleves[2].id)+self.eleves[2].S(self.eleves[0].id))/2
           vote12=(self.eleves[1].S(self.eleves[2].id)+self.eleves[2].S(self.eleves[1].id))/2
           return (vote02+vote01+vote12)/3
