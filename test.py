import numpy

# PySpace PlanetArray imports
from pyspace.planet import PlanetArray

# PySpace Simulator imports
from pyspace.simulator import BruteForceSimulator

# Import BarnesSimulator instead of BruteForceSimulator
from pyspace.simulator import BarnesSimulator

x, y, z = numpy.mgrid[0:500:5j, 0:500:5j, 0:500:5j]
x = x.ravel(); y = y.ravel(); z = z.ravel()

pa = PlanetArray(x=x, y=y, z=z)

G = 1
dt = 0.1

sim = BruteForceSimulator(pa, G, dt, sim_name = "square_grid")

theta = 0.1
sim = BarnesSimulator(pa, G, dt, theta, sim_name = "square_grid")

epsilon = 1
G = 1
dt = 0.1

sim = BruteForceSimulator(pa, G = G, dt = dt, epsilon = epsilon, sim_name = "square_grid")

# Simulate for 1000 secs, ie. 1000/0.1 = 10e4 time steps
sim.simulate(total_time = 1000, dump_output = True)

# Do all imports and set up the PlanetArray as done above

# Set up the simulator
sim = BruteForceSimulator(pa, G, dt, sim_name = "square_grid")

# Use set_data() to tell the simulator what to dump
# For this problem, lets say you only need a_x, a_y and a_z
sim.set_data(a_x = 'a_x', a_y = 'a_y', a_z = 'a_z')

sim.simulate(total_time = total_time, dump_output = True)