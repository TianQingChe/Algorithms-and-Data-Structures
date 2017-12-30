# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:24:39 2017

@author: XPS 13 9350
"""

def genPrimes():
   """
   a generator of prime number
   A candidate number x is prime if (x % p) != 0 for all earlier primes p,
   prime_list is to maintain all earlier primes
   """
   prime_list=[2]
   number=2
   yield 2
   while True:
      number+=1
      flag=True
      for p in prime_list:
         if number%p==0:
            flag=False
            break
      if flag:
        prime_list.append(number)
        yield number