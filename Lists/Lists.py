# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:05:51 2016

@author: Smith Similien
"""

# list of numbers

players = [29, 58, 66, 71, 87 ]

print(players [2])

print( players)

players [2] = 69

print(players)

# add more to the end of the list
# wrong way
players + [90, 91, 98]

# right way but temporary
print (players+ [90, 91, 98])

# perm changes
players.append(120)

print(players)

#slicing 
#slicing = where do you want to stop at
players[:2]

# equals new values at once
players[:2] = [0, 0]
print(players)

#remove items
players[:2] = []
print(players)


#empty your list
players[:] = []
print(players)