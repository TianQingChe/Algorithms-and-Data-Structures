# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 21:05:30 2017

@author: XPS 13 9350
"""
import pylab as plt
mySamples=[]
myLinear=[]
myQuadratic=[]
myCubic=[]
myExponential=[]

for i in range(0,30):
	mySamples.append(i)
	myLinear.append(i)
	myQuadratic.append(i**2)
	myCubic.append(i**3)
	myExponential.append(1.5**i)

plt.plot(mySamples,myLinear)
plt.plot(mySamples,myQuadratic)
plt.plot(mySamples,myCubic)
plt.plot(mySamples,myExponential)

plt.figure('lin')
plt.plot(mySamples,myLinear)
plt.figure('qua')
plt.plot(mySamples,myQuadratic)
plt.figure('cub')
plt.plot(mySamples,myCubic)
plt.figure('exp')
plt.plot(mySamples,myExponential)

plt.figure('lin')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples,myLinear)
plt.figure('qua')
plt.plot(mySamples,myQuadratic)
plt.figure('cub')
plt.plot(mySamples,myCubic)
plt.figure('exp')
plt.plot(mySamples,myExponential)
plt.figure('lin')
plt.title('Linear')
plt.figure('qua')
plt.title('Quadratic')

plt.figure('lin')
plt.ylim(0,1000)
plt.plot(mySamples,myLinear,label='linear')

plt.figure('qua')
plt.ylim(0,1000)
plt.plot(mySamples,myQuadratic,label='quadratic')

plt.figure('lin quad')
plt.plot(mySamples,myLinear,label='linear')
plt.plot(mySamples,myQuadratic,label='quadratic')
plt.legend(loc='upper right')
