#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:55:59 2022

@author: paulo
"""

#implementar um login

palavraDesconhecia = "adivinha"
palavraIntroduzida  = ""
i=0

while (palavraDesconhecia != palavraIntroduzida):
    i+=1
    palavraIntroduzida = input("Escreve a palavra passe: ")
    print("Palavra está errada")
    
print("Acertou ao fim de", i, "tentativas")