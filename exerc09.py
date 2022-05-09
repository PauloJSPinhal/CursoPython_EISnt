#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:55:59 2022

@author: paulo
"""

#implementar um login

segredo = "adivinha"

palavra = input("Escreve a palavra passe: ")

if (segredo == palavra):
    print("Palavra está certa")
else:
    print("Palavra está errada")


