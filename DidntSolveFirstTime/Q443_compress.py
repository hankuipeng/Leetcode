#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Sep 22 14:39:48 2020

@author: hankui

"""

# Link to question: https://leetcode.com/problems/string-compression/


#%%
chars = ["a","a","b","b","c","c","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]


#%% attempt 1
from collections import Counter
freqs = Counter(chars)

count = 0
chars = []

for v in freqs:
    #print(freqs[v])
    
    if freqs[v] == 1:
        count += 1
        chars.extend([v])
    
    if freqs[v] > 1:
        count += (len(str(freqs[v]))) + 1
        chars.extend(v) # add the letter
        chars.extend([val for val in str(freqs[v])]) # add the frequency 


#%% attempt 2
chars = ["a","a","a","b","b","a","a"]
chars = ['a']


#%%
chars0 = chars.copy()

count = 0
prev = chars[0]
freq_cnt = 1
chars.clear()

for i in range(1, len(chars0)):
    #print(i)    
    
# =============================================================================
#     import pdb
#     pdb.set_trace()
# =============================================================================
    
    if chars0[i] != chars0[i-1]:
        if freq_cnt == 1:
            count += 1
            chars.extend([chars0[i-1]])

        if freq_cnt > 1:
            count += (len(str(freq_cnt))) + 1
            chars.extend(chars0[i-1])
            chars.extend([val for val in str(freq_cnt)])
        freq_cnt = 1
        
    if chars0[i] == chars0[i-1]:
        freq_cnt += 1

if freq_cnt == 1:
    chars.extend([chars0[-1]])
else:
    count += (len(str(freq_cnt))) + 1
    chars.extend(chars0[-1])
    chars.extend([val for val in str(freq_cnt)])
    

#%% one solution:
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","b","b","c","c","c"]
chars = ['a']
    
def compress(chars):
    
    i = ii = 0
    cnt = 1
    l = 0 # the length of the resulting chars
    
    import pdb
    pdb.set_trace()
    
    for i in range(len(chars)):
        if i+1 == len(chars) or chars[i] != chars[i+1]: # if the current index is not the last index, or if the current string is different from the next string
            chars[ii] = chars[i]
            l += 1
            ii += 1
            
            if cnt > 1: 
                chars[ii: ii+len(str(cnt))] = str(cnt)
                ii += len(str(cnt))
                l += len(str(cnt))
            cnt = 0
        cnt += 1
    if len(chars) > l:
        del chars[-(len(chars)-l):]
    return ii
    

#chars = ['a','a','b','b']
compress(chars)

