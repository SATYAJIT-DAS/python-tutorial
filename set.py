# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 00:23:15 2019

@author: user
"""
reply=input('enter your name :')
names=reply.split()
print('firstName :',names[0] )
print('LsrtName :',names[1] )
age = int(input( 'Enter your age in years:'))
max_heart_rate = 206.9 -(0.67 * age) 
print(max_heart_rate)
target = 0.6556 *max_heart_rate
print( 'Your target fat-burning heart rate is' , target)
alpha=[2,3,4,5,6]
beta=alpha
beta+=[7,8]
beta=beta+[10,9]
print(alpha)
print(beta)
print(len(beta))
print(max(beta))
print(sum(beta))
print(sorted(beta))
for j in range(10):
    if j== 5:
        continue 
    print(j)