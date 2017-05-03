import math
import numpy as np
import matplotlib.pyplot as plt

# define the rotation curve
def vel(r):

    ar = math.fabs(r)
    if (ar <= 5.0):
        v = 1.4*ar*math.exp(-ar/20.0)
    elif (ar > 5.0 and ar < 6.0):
        max = 1.4*5*math.exp(-5.0/20.0)
        min = 5.0
        m = (max - min)/(-1.0)
        v = m*(ar - 5.0) + max
    else:
        v = 5.0

    return v



def spiral():

    rmin = -20
    rmax = 20
    npts = 10

    r = np.arange(npts, dtype=np.float64)*(rmax - rmin)/(npts - 1.0) + rmin

    omega = np.zeros( (npts) )

    n = 0
    while (n < npts):
        omega[n] = math.fabs(vel(r[n])/r[n])
        n += 1


    t = 0.0
    tmax = 20.0
    dt = 0.04

    iframe = 0

    while (t < tmax):


        plt.clf() # clf clears the current figure

        x = r*np.cos(omega*t)
        y = r*np.sin(omega*t)

        plt.plot(x,y,'ro', x, y + 5, 'bo', x, y - 5, 'yo')


        plt.axis([1.2*rmin,1.2*rmax,1.2*rmin,1.2*rmax]) # the axis function takes four variables (xmin,xmax,ymin,ymax)
        #plt.axis("off")

        f = plt.gcf() # gcf returns the current figure
        f.set_size_inches(6.0,6.0)

        outfile = "galaxy_%04d.png" % iframe
        plt.savefig(outfile)

        iframe += 1
        t += dt



if __name__== "__main__":
    spiral()