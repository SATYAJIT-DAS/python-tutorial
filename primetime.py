# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:52:30 2019

@author: user
"""

def prime(n):
    primes=[]
    for possiblePrime in range(2,n+1):
        isPrime=True
        for num in range(2,int(possiblePrime**0.5)+1):
            if (possiblePrime%num==0):
                isPrime=False
        if isPrime:
            primes.append(possiblePrime)
    return primes

print(prime(20))