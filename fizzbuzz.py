# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:45:57 2019

@author: user
"""

for j in range(1,101):
    #print(j)
    multiplyOfThree=j%3==0
    multiplyOfFive=j%5==0
    if(multiplyOfThree and multiplyOfFive):
        print('fizzBuzz')
    elif(multiplyOfThree):
        print('fizz')
    elif(multiplyOfFive):
        print('BUZZ')
    else:
        print(j)
        
        
    