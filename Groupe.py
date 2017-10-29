#! /usr/bin/python3.5
#-*- coding: utf-8 -*-

class Groupe:

    def __init__(self, eleves):
        self.eleves = eleves
        self.notes = []#liste des satisfactions de chaque éleves groupe
        for eleve in self.eleves:
            eleve.calculNote()
            self.notes.append(eleve.note())

    def getNote(self):
        return self.note

    # Correspond à setNote
    def calculSatisfaction(self):
        """ Fonction calculant la satisfaction de ce groupe
        @In :
        @Out :
        L'ordre sera le suivant :
            AR = 0      Toutes les combinaisons avec AR
            I = 1       Toutes les combinaisons avec I
            P = 2       P + P
            P+ = 3      AB + P
            AB- = 4     B + P       ||  TB + P
            AB = 5      AB + AB
            AB+ = 6     B + AB
            B- = 7      TB + AB
            B = 8       B + B
            B+ = 9      TB + B
            TB = 10     TB + TB
        """
        
        #e1 = eleves[0]
        #e2 = eleves[1]
        #if len(self)==3:
            #if eleves[2]
        #if e1 == "TB"  :
        # Do the thing
        #elif x == 'b':
        # Do the other thing
        #if x in 'bc':
        # Fall-through by not using elif, but now the default case includes case 'a'!
        #elif x in 'xyz':
        # Do yet another thing
        #else:
        # Do the default


    def getEleves(self):
        return self.eleves
