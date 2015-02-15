from math import *
from Tkinter import * 
import pylab as z;
import numpy as np;
import math
import time
from numpy import *
from matplotlib import pyplot
from numpy . random import standard_normal , seed
from matplotlib . pyplot import *
import warnings
from time import time
from scipy import *

def RiskNeutralProbability(down, up, r):

	q = (r - down)/(up - down)

	return q

def StockEvolution(S_0, down, up, totalsteps, upsteps):
	
	while upsteps < 0 or upsteps > totalsteps:
		
		print "You have inserted a wrong values for the variable upsteps, please provide me an acceptable one:"
		
		upsteps = input("")
		
	S = S_0*(pow(up, upsteps))*(pow(down, totalsteps - upsteps))
	return S

def CallPayoff(S, K):
	
	return max(S - K, 0.0)
	
def PutPayoff(S, K):
	
	return max(K - S, 0.0)
	
def BinomialPricer(S_0, down, up, r, steps, K):
	
#Checking the inputs
	
	if S_0 <= 0.0 or up <= -1.0 or down <= -1.0 or r <= -1.0 or up <= down:

		print "Wrong Inputs, the program is closing"
		raise SystemExit()

#Checking possible arbitrage opportunities

	if r < down or r > up:
		
		print "Wrong Inputs, the program is closing"
		raise SystemExit()
		
#Checking phase passed

	prices = [] 
	#list that stores all the values of the option
	q = RiskNeutralProbability(down, up, r)

	
	for i in xrange(0, steps + 1, 1):

		prices.append(CallPayoff(StockEvolution(S_0, down, up, steps, i), K))

	for n in xrange(steps - 1, - 1, -1):
		
		for i in xrange(0, n + 1, 1):

			prices[i] = (1 / (r)) * (prices[i + 1] * q + (1 - q) * prices[i]);

			if StockEvolution(S_0, down, up, n, i) - K > prices[i]:

				prices[i] = StockEvolution(S_0, down, up, n, i) - K

			if K - StockEvolution(S_0, down, up, n, i) > prices[i]:

				prices[i] = K - StockEvolution(S_0, down, up, n, i)
	
	
	return prices[0]; 
	#Return the price at time zero of the option


#Use this console for changing the parameters

S_0 = 36#Initial value for the stock
K = 40.0 #Strike
d = 0.2 #Down
r = 1.02 #1 + Interest rate
u = 1.5 #Up
n = 10 #Steps

print "\n" + "The price of your option is: " + str(round(BinomialPricer(S_0, d, u, r, n, K), 3))
#Plot an example of binomial tree
#function required for simulating a binomial random variable

