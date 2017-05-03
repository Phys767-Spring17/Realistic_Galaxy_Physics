import math
import numpy as np
import matplotlib.pyplot as plt

# define the rotation curve
def vel(r1):

    ar1 = math.fabs(r1)
    if (ar1 <= 5.0):
        v1 = 1.4*ar1*math.exp(-ar1/20.0)
    elif (ar1 > 5.0 and ar1 < 6.0):
        max = 1.4*5*math.exp(-5.0/20.0)
        min = 5.0
        m = (max - min)/(-1.0)
        v1 = m*(ar1 - 5.0) + max
    else:
        v1 = 5.0

    return v1

def vel(r2):

    ar2 = math.fabs(r2)
    if (ar2 <= 5.0):
        v2 = 1.4*ar2*math.exp(-ar2/20.0)
    elif (ar2 > 5.0 and ar2 < 6.0):
        max = 1.4*5*math.exp(-5.0/20.0)
        min = 5.0
        m = (max - min)/(-1.0)
        v2 = m*(ar2 - 5.0) + max
    else:
        v2 = 5.0

    return v2

def vel(r3):

    ar3 = math.fabs(r3)
    if (ar3 <= 5.0):
        v3 = 1.4*ar3*math.exp(-ar3/20.0)
    elif (ar3 > 5.0 and ar3 < 6.0):
        max = 1.4*5*math.exp(-5.0/20.0)
        min = 5.0
        m = (max - min)/(-1.0)
        v3 = m*(ar3 - 5.0) + max
    else:
        v3 = 5.0

    return v3



def spiral():

    rmin = -20
    rmax = 20
    npts1 = 16
    npts2 = 8
    npts3 = 4

    r1 = np.arange(npts1, dtype=np.float64)*(rmax - rmin)/(npts1 - 1.0) + rmin
    r2 = np.arange(npts2, dtype=np.float64) * (rmax - rmin) / (npts2 - 1.0) + rmin
    r3 = np.arange(npts3, dtype=np.float64) * (rmax - rmin) / (npts3 - 1.0) + rmin

    omega = np.zeros( (npts1) )
    gamma = np.zeros( (npts2) )
    beta = np.zeros( (npts3) )

    n1 = 0
    while (n1 < npts1):
        omega[n1] = math.fabs(vel(r1[n1])/r1[n1])
        n1 += 1
    n2 = 0
    while (n2 < npts2):
        gamma[n2] = math.fabs(vel(r2[n2])/r2[n2])
        n2 += 1
    n3 = 0
    while (n3 < npts3):
        beta[n3] = math.fabs(vel(r3[n3])/r3[n3])
        n3 += 1


    t = 0.0
    tmax = 20.0
    dt = 0.04

    iframe = 0

    while (t < tmax):


        plt.clf() # clf clears the current figure

        x1 = r1*np.cos(omega*t)
        y1 = r1*np.sin(omega*t)
        x2 = r2*np.cos(gamma*t)
        y2 = r2*np.sin(gamma*t)
        x3 = r3*np.cos(beta*t)
        y3 = r3*np.sin(beta*t)

        plt.plot(x1,y1,'ro',x2,y2+5,'bo',x3,y3-5,'yo')


        plt.axis([1.2*rmin,1.2*rmax,1.2*rmin,1.2*rmax]) # the axis function takes four variables (xmin,xmax,ymin,ymax)
        #plt.axis("off")

        f = plt.gcf() # gcf returns the current figure
        f.set_size_inches(6.0,6.0)

        outfile = "stardistribution_%04d.png" % iframe
        plt.savefig(outfile)

        iframe += 1
        t += dt



if __name__== "__main__":
    spiral()