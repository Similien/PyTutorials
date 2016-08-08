# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 13:51:36 2016

@author:Similien
"""
# making a program that checks the availability of a jersey
# continue means go to the next iteration of the loop.  
numbersTaken = [2, 5, 12, 13, 17]

print("Here are the available jersey numbers")

for n in range(1, 20):
    if n in numbersTaken:
        continue
    print(n)

