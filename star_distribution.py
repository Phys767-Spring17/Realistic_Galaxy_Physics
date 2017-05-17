import numpy as np
import matplotlib.pyplot as plt

# define the rotation curve

def vel(r):

    ar = np.abs(r)
    if np.any(ar <= 5.0):
        v = 1.4*ar*np.exp(-ar/20.0)
    elif np.any(ar > 5.0) and np.any(ar < 6.0):
        max = 1.4*5*np.exp(-5.0/20.0)
        min = 5.0
        m = (max - min)/(-1.0)
        v = m*(ar - 5.0) + max
    else:
        v = 5.0

    return v



def spiral(rmin=-20, rmax=20, npts1=16, npts2=8, npts3=4, t=0.0, tmax=20.0, dt=0.04, iframe=0):

    r1 = np.arange(npts1, dtype=np.float64)*(rmax - rmin)/(npts1 - 1.0) + rmin
    r2 = np.arange(npts2, dtype=np.float64) * (rmax - rmin) / (npts2 - 1.0) + rmin
    r3 = np.arange(npts3, dtype=np.float64) * (rmax - rmin) / (npts3 - 1.0) + rmin

    v1 = np.array(vel(r1))
    v2 = np.array(vel(r2))
    v3 = np.array(vel(r3))

    omega = np.absolute(v1/r1)
    gamma = np.absolute(v2/r2)
    beta = np.absolute(v3/r3)


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