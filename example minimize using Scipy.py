"""minimize an object function, using Scipy"""

import pandas as pandas
import matplotlib.pyplot as pyplot
import numpy as numpy
import scipy.optimize as spo

def f(X):
	"""given a scalar X,return some value"""
	Y=(X-1.5)**2+0.5
	print "X={}, Y={}".format(X,Y) #for tracing
	return Y

def test_run():
	Xguess=2.0
	min_result=spo.minimize(f,Xguess, method='SLSQP',options={'disp':True})
	print "minima found at:"
	print "X={},Y={}". format(min_result.x,min_result.fun)


if __name__ == '__main__':
	test_run()