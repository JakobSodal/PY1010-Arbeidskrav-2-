# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:46:27 2024

@author: Jakob Sødal
"""
'''
Et program som regner om grader til radianer.
'''

#%%
import numpy as np
v_grad = float(input('skriv inn gradtallet:'))

v_rad = v_grad*np.pi/180 # formel for omergning av grader til radianer.
v_rad_round = round(v_rad,4) 

print(v_grad, 'grader er lik', v_rad_round, 'radianer') #print av svar i radianer