# -*- coding: utf-8 -*-
"""
Created: 23.01.2025

@author: Jakob Sødal
"""
'''
Oppg 5, Arbeidskrav 2, PY1010
'''
'''
Glemte at a var diameter og ikke radius, har forsøkt å rette dette.
'''
#%% katetenes lengder iput

import math

a = float (input ('Skriv lengden til korteste katet: '))
b = float (input ('Skriv lengden til lengste katet:'))

#%% Areal 1/2 sirkel

areal_halvsirkel = (3.14*(a/2)**2)/2    # halvsirkel fordi det er kun det som er del av figuren 


#%% areal rett trekant

areal_trekant = (a * b)/2

#%% omkrets 1/2 sirkel

omkrets_halvsirkel = (2*math.pi*(a/2))/2    # halvsirkel fordi det er kun det som er del av figuren 

#%% omkrets rett trekant minus a

hypotenus = math.sqrt(a**2 + b**2)

omkrets_trekant_minus_a = hypotenus + b  # har ikke med variabelen: "a" da denne ikke er ytreomkrets


#%% svarene printet

omkrets_figur = omkrets_trekant_minus_a + omkrets_halvsirkel # figurens ytre omkrets

areal_figur = areal_trekant + areal_halvsirkel   # figurens areal




print ('Figurens ytreomkrets er: ', round(omkrets_figur, 2)) 
print ('Figurens areal er: ',round (areal_figur, 2))

'''
Innser nå at jeg kunne ha laget en variabel r istedet for å skrive a/2.
Er det mer riktig å gjøre det på den måten?
''' 