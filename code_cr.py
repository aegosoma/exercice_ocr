#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint, shuffle

rond = (" ", "➀", "➁", "➂", "➃", "➄")
valeur = ("⛀", "✉", "♔", "⋄")

class coffre():
    def __init__(self, val, nbr, liste):
        self.valeur = val
        self.nombre = nbr
        self.liste = liste
        self.bak = []
        for i in self.liste: self.bak.append(i)
        self.etat = False #[False for j in range(nbre)]
    def chaines(self):
        pass
    def resetCarton():
        self.liste = []
        for i in self.bak: self.liste.append(i)

class jeu():
    def __init__(self):
        pass

class de():
    def __init__(self):
        pass
