# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:34:26 2024

@author: Jakob Sødal
"""
'''
oppg 4, Arbeidskrav 2, PY1010


'''

#%% 
# a) #dictionary av ulike land som keys: {'Land': ['Hovedstad', innbyggere]}

data = {'Norge': ['Oslo', 0.634],       #dict: {'Land': ['hovedstad', innbyggere]}
        'England': ['London', 8.982],
        'Frankrike': ['Paris', 2.161],
        'Italia': ['Roma', 2.873]
        }

# b) #Brukeren skriver inn land og får tilbake hovedstad og innbyggertall.

land = input('Skriv inn et land fra dictionary-en og få tilbake dens hovedstad og innbyggertall: ')

if land in data:

    print(f'{data[land][0]} er hovedstaden i', land, 'og det er', data[land][1], 'mill. innbyggere i', data[land][0])
if land not in data:
    print('Dette landet er ikke i dictionary-en')


# c) #Brukeren kan legge til nye land i dictionary-en.

nytt_land = input('legg til ett nytt land i dictionary-en ved å skrive det her:')

if nytt_land in data:
    print('Dette landet eksisterer allerede i dictionary-en')

if nytt_land not in data:
    nytt_land_hovedstad = input('Skriv hva hovedstaden til dette landet:')
    nytt_land_inbyggertall = input('Hva er inbyggertallet i hovedstaden oppgitt i millioner?')
    data.update({nytt_land: [nytt_land_hovedstad, float(nytt_land_inbyggertall)]})
    print(f'',nytt_land, 'er lagt til dictionary-en med', nytt_land_hovedstad, 'som hovedstad og', nytt_land_inbyggertall, 'mill. inbyggere.')
    print('Her er den oppdaterte dictionary-en:', data)



  