"""
testing file
Dylan Assinner (dylan.assinner@student.uatwerpen.be)
last updated: 27/04/2026
"""

import matplotlib.pyplot as plt
from shapes import Point, SphereSim, BeamSim, Simulator
from particle import Neutron, Uranium

if __name__ == '__main__':
    print('Welcome to the critical mass simulation.')
    print('')
    print(Point(0, 0, 0))
    print(Simulator(1, 100, Point(0, 0, 0)))
    print(BeamSim(1, 1, 100, Point(0, 0, 0)))
    print(BeamSim(1, 0.5, 100, Point(0, 0, 0)))
    print(SphereSim(1, 100, Point(0, 0, 0)))
    print(Neutron(1,1,1))
    print(Uranium(1,1,1))
    plt.show(block=False)
    plt.close()