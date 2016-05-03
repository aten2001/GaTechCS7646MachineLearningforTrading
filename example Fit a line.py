"""Fit a line to a given set of data points using optimization. """

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def error(line, data): # error function
    """Computer error between given line model and observed data.

        Parameters
        ----------
        line: tuple/list/array (c0,c1) where c0 is slope and c1 is y-intercept 
        f(x)=c0*x + c1
        data: 2D array where each row is a point (x,y)

        Returns error as a single real value.
    """
    #metric: Sum of squared Y-axis differences
    err = np.sum((data[:,1] - (line[0] * data[:,0] + line[1])) ** 2)
    return err

def fit_line(data, error_func):
    """Fit a line to given data, using a supplied error function.

    Parameters
    ----------
    data: 2D array where each row is a point (X0, Y)
    error_func: function that computer the error between a line and observed data

    Returns line that minimizes the error function.
    """
    # Generate initial guess for line model
    l = np.float32([0, np.mean(data[:, 1])]) # slope = 0, intercept = mean(y values)

    #Plot initial guess (optional)
    x_ends = np.float32([-5,5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label="Initial guess")  # m-- = magenta dashed line

    #Call optimizer to minimize error function
    result = spo.minimize(error_func, l, args=(data,), method='SLSQP', options={'disp':True})
    return result.x

    #plot initial guess(optional)
    x_ends = np.float32([-5,5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label="Initial guess") #m-- = magenta dashed line

    #Call optimizer to minimize error function
    result = spo.minimize(error_func, l, arg=(data,), method='SLSQP', options= { 'disp':True})
    return result.x

def test_run():
    # Define original line
    l_orig = np.float32([4,2])
    print "Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1])
    Xorig=np.linspace(0,10,21)
    Yorig = l_orig[0]*Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original line")  #b- = blue solid line

    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:,0], data[:,1], 'go', label = "Data points")

    # Try to fit a line to this data
    l_fit = fit_line(data,error)
    print "Fitted line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1])
    plt.plot(data[:,0], l_fit[0] * data[:,0] + l_fit[1], 'r--', linewidth=2.0, label="Fitted line") #r-- = red dashed line
    plt.title("Comparison of original line, scattered data and fitted line",fontsize=12)
    plt.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    test_run()