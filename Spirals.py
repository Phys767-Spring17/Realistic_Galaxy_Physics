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
    :param npts: number of points for line
    :param t: time start
    :param tmax: time end
    :param dt: time interval
    :param iframe: inline frame
    :return: spiral
    """

    r = np.arange(npts, dtype=np.float64)*(rmax - rmin)/(npts - 1.0) + rmin
    v = np.array(vel(r))
    omega = np.abs(v/r)


    while (t < tmax):

        plt.clf() # clf clears the current figure

        fig = plt.figure()
        ax = p3.Axes3D(fig)

        x = r*np.cos(omega*t)
        y = r*np.sin(omega*t)

        ax.plot(x-35.0,y,zs=-10.0,zdir='z',color='red',linestyle='solid',linewidth=12)
        ax.plot(x+35.0,-y,zs=10.0,zdir='z',color='blue',linestyle='solid',linewidth=12)

        ax.set_xlim3d([-60.0, 60.0])
        ax.set_xlabel('X')

        ax.set_ylim3d([-20.0, 20.0])
        ax.set_ylabel('Y')

        ax.set_zlim3d([-10.0, 10.0])
        ax.set_zlabel('Z')

        ax.set_title('3D Galaxy')

        #ax.axis('off')
        ax.view_init(elev=18 * t, azim=0.)

        outfile = "Spirals_%04d.png" % iframe
        plt.savefig(outfile)

        iframe += 1
        t += dt



if __name__== "__main__":
    spiral()