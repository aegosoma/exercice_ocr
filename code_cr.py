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
        n = len(self.liste)
        ch = []
        ch.append("┌─────────────┬───┐")
        une, deu, tro = " ", " ", " "
        if n >= 1: une = self.liste[0]
        if n >= 2: deu = self.liste[1]
        if n >= 3: tro = self.liste[2]
        ch.append("│ ({}) ({}) ({}) │   │".format(une, deu, tro))
        qua, cin, six = " ", " ", " "
        if n >= 4: qua = self.liste[3]
        if n >= 5: cin = self.liste[4]
        if n == 6: six = self.liste[5]
        ch.append("│ ({}) ({}) ({}) │   │".format(qua, cin, six))
        ch.append("│             │ {} │".format(self.valeur))
        ch.append("└─────────────┴───┘")
        return ch
    def resetCarton():
        self.liste = []
        for i in self.bak: self.liste.append(i)

class jeu():
    def __init__(self):
        pass

class de():
    def __init__(self):
        pass
