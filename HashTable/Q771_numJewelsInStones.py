#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:08:24 2020

@author: hankui
"""

# Link to question: 


#%%
J = "aA"
S = "aAAbbbb"


#%%
class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        count = 0
        
        for i,v in enumerate(S):
            
            count += v in list(J)
            
        return count 
    

#%%
Solution.numJewelsInStones(__,J,S)