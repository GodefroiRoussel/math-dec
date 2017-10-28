#! /usr/bin/python3.5
#-*- coding: utf-8 -*-

class Groupe:

    def __init__(self, eleves):
        self.eleves = eleves
        #self.note = calculSatisfaction(self)

    def getNote(self):
        return self.note

    # Correspond à setNote
    def calculSatisfaction(self):
        """ Fonction calculant la satisfaction de ce groupe
        @In :
        @Out :
        """


    def getEleves(self):
        return self.eleves
