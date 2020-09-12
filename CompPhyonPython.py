# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 09:01:08 2018

@author: RANJAN
"""

import numpy as np

"'setting up parameter'"
epsilon0 = 8.85e-12
hbar = 6.626e-34 / (2*np.pi)
m_e = 9.11e-31
e = 1.6e-19

"' Bohr Radius is to be calculated'"
#  This is antother way to make a comment on Spyder ipyhthon but only in one line.

a0 = 4*np.pi*epsilon0*hbar**2 / (m_e * e**2)

print (a0)

#print the resulrt in a formatted w
"'Ex %8.3 8: 8 digits  , .3  3 decimal numbers e = scientific but f = float'"


print ( 'Bohr radius is %0.9e'%(a0) )
