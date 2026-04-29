"""
testing file
Dylan Assinner (dylan.assinner@student.uatwerpen.be)
last updated: 27/04/2026
"""

import matplotlib.pyplot as plt
from termcolor import colored
import tabulate as tab
from shapes import Point, SphereSim, BeamSim, Simulator
from particle import Neutron, Uranium

def close_all():
    """function to close plots that we don't want to show"""
    # This is necessary because the fig and ax argument of a plot
    # are inherent values of the objects
    plt.show(block=False)
    plt.close('all')

if __name__ == '__main__':
    print("\033[H\033[2J", end="")
    print('Welcome to the critical mass simulation. \n')
    print('To continue the program when a plot pops up,'
          ' simply close the plot. At times multiple plot windows'
          ' may open and close rapidly.\nThis is for memory management,'
          ' as the plot window is an inherent attribute of the'
          ' simulator classes.')
    input(colored("Press enter to continue...", 'yellow', attrs=['bold']))
    print("\033[H\033[2J", end="")
    print(colored('First task: finding the critical mass'
                  ' of a square.',attrs=['bold'])+ '\n')
    print('First, we will estimate the mass using big steps')
    header=["Mass", "Survivor fraction"]
    table=[]
    for i in [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]:
        simobject=BeamSim(i, 1, 100, Point(0,0,0))
        table.append([i,simobject.surviror_fraction().fraction])
    close_all()
    print(tab.tabulate(table, headers=header, tablefmt="grid"))
    input(colored("Press enter to continue...", 'yellow', attrs=['bold']))
    print("\nWe see that the critical mass is somewhere below 1.5."
          " We will now take a smaller step to get closer to a"
          " survivor fraction of 1.\nWe will also set the amount of simmulated"
          " points to 500 for a more precise estimate.\n")
    body=[]
    for i in [1.45, 1.46, 1.47, 1.48, 1.49, 1.5,1.51,1.52,1.53,1.54,1.55]:
        simobject2 = BeamSim(i, 1, 500, Point(0, 0, 0))
        body.append([i, simobject2.surviror_fraction().fraction])
    close_all()
    print(tab.tabulate(body, headers=header, tablefmt="grid"))
    print('\nIf we run these simulations a couple of times,'
          ' we see that the value fluctuates.'
          ' We therefore conclude that the critical mass is 1.5,'
          ' with an error margin of 0.3. ')
    input(colored("Press enter to continue...", 'yellow', attrs=['bold']))
    print("\033[H\033[2J", end="")

