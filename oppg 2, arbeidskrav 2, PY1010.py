# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:17:51 2024

@author: Jakob Sødal
"""
'''
Oppg 2, PY1010 Arbeidskrav 2

Program som regner ut antall pizza man trenger basert på antall elever
'''

#%%
antall_elever = int(input('Skriv inn antall elever: ')) #antall elever

antall_pizza = (antall_elever)*0.25 # En elev spiser 0.25 pizza

import math
rund_antall_pizza = math.ceil(antall_pizza) # runder OPP til nærmeste heltall.(må kjøpe hel pizza, ikke bare andel spist)

print('Antall pizza som må handles inn til festen: ', int(rund_antall_pizza))