# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:29:14 2019

@author: user
"""

def LRUCache(strArr): 

    # code goes here
    checked=[]
    for e in strArr:
        if e in checked:
            
            for j in range(len(checked)-1):
                checked[j]=checked[j+1]
            
            checked[-1]=e
            checked.remove(e)
        if e not in checked:
            checked.append(e)
  
   
    string= '-'.join(checked)        
    return string        
    
# keep this function call here  
print LRUCache(raw_input())  