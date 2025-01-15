# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:59:09 2024

@author: Jakob Sødal
"""
'''
Oppg 6, Arbeidskrav 2, PY1010

Plot av funksjonen f(x)= -x^2 - 5 i array med 200 punkter fordelt på intervallet [-10, 10].
'''

#%%

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200) #array

y = -𝑥**2 - 5   #𝑓(𝑥) = −𝑥^2 − 5

plt.title('f(x) = −x2 − 5') 
plt.xlabel('x') 
plt.ylabel('f(x)')
plt.grid()
plt.plot(x, y)
plt.show()

'''
Har brukt AI for å hjelpe meg å forstå hvordan f(x) fungerte og gi meg en y verdi, da jeg ikke fant ut av dette gjennom å se forelesningen og søk på google, håper det går fint.
Jeg har ellers skrevet programmet selv.
'''