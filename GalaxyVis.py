import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

def vel(r):
    """
    vel(r) represents the velocity as a function of radius and thus defines the rotation curve.
     To obtain a spiral shape, we make the value of this function larger at smaller radii.

    In this case, for radii (ar) less than or equal to 5 units, v=1.4(ar)exp(-ar/20).
    For ar between 5 and 6, v ranges between 5.0 and 1.4(5)exp(-5/20).
    For ar greater than or equal to 6, v is a constant 5.

    :param r: radius
    :return: velocity
    """

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



def spiral(rmin=-20, rmax=20, npts=1000, t=0.0, tmax=20.0, dt=0.04, iframe=0):
    """Function that creates spiral shape. Plots x and y-positions in terms of cosine and sine
    functions of angular frequency (omega, beta, gamma) using values of radii and associated
    velocity.

    :param rmin: minimum radius
    :param rmax: maximum radius
    :param npts: number of points for 1st line #to make redgalaxy.mp4, set npts=10
    :param t: time start          #to make galaxy.mp4, set npts=10
    :param tmax: time end         #to make spiral_distribution.mp4, set npts1=16, npts2=8, npts3=4
    :param dt: time interval      #to make 3Galaxy.mp4, set npts=1000
    :param iframe: inline frame
    :return: spiral
    """

    r = np.arange(npts, dtype=np.float64) * (rmax - rmin) / (npts - 1.0) + rmin
    #r1 = np.arange(npts1, dtype=np.float64)*(rmax - rmin)/(npts1 - 1.0) + rmin #reinstate r1,r2,r3 for star_distribution.mp4
    #r2 = np.arange(npts2, dtype=np.float64) * (rmax - rmin) / (npts2 - 1.0) + rmin
    #r3 = np.arange(npts3, dtype=np.float64) * (rmax - rmin) / (npts3 - 1.0) + rmin #to obtain 3Galaxy.mp4, keep info about the third line

    v = np.array(vel(r)) #reinstate v1,v2,v3 for star_distribution.mp4
    #v1 = np.array(vel(r1))
    #v2 = np.array(vel(r2))
    #v3 = np.array(vel(r3))

    omega = np.absolute(v/r) #reinstate kappa, gamma, and beta for star_distribution.mp4
    #kappa = np.absolute(v1/r1)
    #gamma = np.absolute(v2/r2)
    #beta = np.absolute(v3/r3)


    while (t < tmax):


        plt.clf() # clf clears the current figure

        fig = plt.figure()
        ax = p3.Axes3D(fig)

        x = r*np.cos(omega*t)
        y = r*np.sin(omega*t)
        z = 0 #reinstate the below lines for if you have lines with different number of points
        #x1 = r1*np.cos(omega*t)
        #y1 = r1*np.sin(omega*t)
        #z1 = 0 #to make Opposite.mp4, remove the 3rd axis (i.e. z)
        #x2 = r2*np.cos(gamma*t)
        #y2 = -r2*np.sin(gamma*t) #to obtain 3Galaxy.mp4, make this positive
        #z2 = 0
        #x3 = r3*np.cos(beta*t)
        #y3 = r3*np.sin(beta*t)

        ax.plot(x-35,y,z-10,'r-',x-30,y+5,z-5,'bo',x-40,y-5,z-15,'yo') #these are the three lines of the first galaxy
        ax.plot(x+35,y,z+10,'b-',x+40,y+5,z+15,'yo',x+30,y-5,z+5,'ro') #these are the three lines of the second galaxy

        ax.set_xlim3d([-60.0, 60.0])
        ax.set_xlabel('X')

        ax.set_ylim3d([-25.0, 25.0])
        ax.set_ylabel('Y')

        ax.set_zlim3d([-15.0, 15.0])
        ax.set_zlabel('Z')

        ax.set_title('3D Galaxy')


        #plt.plot(x1-35,y1,'r-',x2+35,y2,'b-') #to make Opposite.mp4, reinstate this line
        #to make redgalaxy.mp4, use plt.plot(x1,y1,'ro')
        #to make galaxy.mp4 and star_distribution.mp4, use plt.plot(x1,y1,'ro',x2,y2+5,'bo',x3,y3-5,'yo')
        #to make 3Galaxy.mp4, use plt.plot(x1-40,y1,'r-',x2,y2,'b-',x3+40,y3,'y-')

        #plt.axis([3.0*rmin,3.0*rmax,rmin,rmax]) # the axis function takes four variables (xmin,xmax,ymin,ymax)
        #to make redgalaxy.mp4, galaxy.mp4, and star_distribution.mp4, multiply rmin and rmax by 1.2 for all four entries
        #to make Opposite.mp4, reinstate the first line of this block of text
        #plt.axis("off")

        #f = plt.gcf() # gcf returns the current figure
        #f.set_size_inches(18.0,6.0,6.0) #to make redgalaxy.mp4, galaxy.mp4, and star_distribution.mp4, change 18.0 to 6.0

        outfile = "GalaxyVis_%04d.png" % iframe
        plt.savefig(outfile)

        iframe += 1
        t += dt



if __name__== "__main__":
    spiral()