#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:42:50 2022

@author: emondemoniac
"""

import math
from fractions import Fraction
import pandas as pd
def path_loss(a,b):
    
     #a = 0.20
     #b = 0.20
     c = math.sqrt( a * a + b * b)
     #cumulative_path = 0
     #first = [c].cumsum()
     #cumulative_path = sum (first, start=cumulative_path)
     
     print ('individual length:', c)
     
path_loss(0.20,0.20)
path_loss(0.55,0.75)
path_loss(0, 0.75)

total_path_length = pd.DataFrame({'individual length':[0.28284271247461906, 0.9300537618869137,0.75]})
total_path_length.index = ['qf','qd','b']
total_path_length['cumulative length'] = total_path_length['individual length'].cumsum()
print(total_path_length)