#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:24:08 2022

@author: paulo
"""

n1 = float(input("Introduz o 1.º número:"))
n2 = float(input("Introduz o 2.º número:"))
n3 = float(input("Introduz o 3.º número:"))



if ( (n1!=n2) and (n2!=n3) and (n1!=n3) ):
    if ( (n1<n2) and (n2<n3) ):
        print("A ordem é:", n1, n2, n3)
    if ( (n1<n3) and (n3<n2) ):
        print("A ordem é:", n1, n3, n2)
    if ( (n2<n3) and (n3<n1) ):
        print("A ordem é:", n2, n3, n1)
    if ( (n2<n1) and (n1<n3) ):
        print("A ordem é:", n2, n1, n3)
    if ( (n3<n1) and (n1<n2) ):
        print("A ordem é:", n3, n1, n2)
    if ( (n3<n2) and (n2<n1) ):
        print("A ordem é:", n3, n2, n1)
else:
    printf("Existem números iguais")