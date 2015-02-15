from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


class FX:
            
    def BS_Analytics_Foreign(self, Sf_t, Y_t, K_sf, t, T, r_f, v_sf, selector):
	
         d1 = (np.log(Sf_t/K_sf) +(r_f + 0.5*np.power(v_sf, 2.0))*(T - t))/(v_sf*np.sqrt(T - t))
         d2 = d1 - v_sf*np.sqrt(T - t)
	
         if selector == 1:
             P = Y_t*(Sf_t*norm.cdf(d1) - K_sf*np.exp(-r_f*(T - t))*norm.cdf(d2))
             return P
         elif(selector == 2):
             P = Y_t*(-Sf_t*norm.cdf(-d1) + K_sf*np.exp(-r_f*(T - t))*norm.cdf(-d2))
             return P
         else:
		    print "Wrong input inserted, the program is now closing" + "\n"
		    exit()



        