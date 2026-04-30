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
    # initial welcome and layout test file
    print('\nWelcome to the critical mass simulation. \n')
    print('To continue the program when a plot pops up,'
          ' simply '+colored('close the plot','yellow')+
          '. At times multiple plot windows may open and close rapidly.\n'
          'This is for memory management, as the plot window is an'
          ' inherent attribute of the simulator classes.')
    print('We will first explain the way the classes work, '
          'before doing the actual simulations.')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    print("\033[H\033[2J", end="")
    # Particles
    print("The first two classes we will introduce are the "+
          colored('Neutron','green')+' class and '+
          colored('Uranium','green')+' class.')
    print('These are both instances of a '+colored('Particle','green')+
          ' parent class, which contains the input protection and the '+
          colored('__str__','green')+' and '+colored('__repr__','green')
          +' methods.\n')
    print('The '+colored('Neutron','green')+
          ' class has a randomizer built in, '
          'to calculate the endpoint of the neutron.')
    neutron=Neutron(0, 0, 0)
    print('A neutron that starts at coordinates (0,0,0) for example,'
          ' has endpoint: '+f'({neutron.endpoint().x: 1.5f}, '
                            f'{neutron.endpoint().y: 1.5f}, '
                            f'{neutron.endpoint().z: 1.5f})\n')
    print('The '+colored('Uranium','green')+
          ' class also takes coordinates as input, and generates two '+
          colored('Neutron','green')+
          ' class objects that start at that point.')
    headlineuranium=['Particle type', 'x','y','z']
    uranium=Uranium(0, 0, 0)
    body=[['Uranium', uranium.xpos, uranium.ypos, uranium.zpos]]
    for _, part in enumerate(uranium.fission()):
        body.append(['Neutron',part.endpoint().x,
                     part.endpoint().y, part.endpoint().z])
    print(tab.tabulate(body, headers=headlineuranium, tablefmt="grid"))
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    print("\033[H\033[2J", end="")
    # Simulators
    print('The other classes we made are the '+colored('Simulator','green')+
          ' parent class with its subclasses.')
    print('These classes are made with inheritance in mind.'
          ' \nWe will thus explain the Simulator class and mention'
          ' only the added features for the subclasses.')
    print('\nThe '+colored('Simulator','green')+
          ' class supports the two main methods of the simulation: '
          'calculating the '+colored('survivor fraction','green')+
          ' and the '+colored('visual simulation','green')+
          '. \nIt also provides a general input protection.')
    print('\nThe '+colored('survivor_fraction()','green')+
          ' method determines the survivor fraction by simulating '+
          colored('N','blue')+
          ' starting points as input for the '+colored('Uranium','green')+
          ' class. \nThe function then evaluates whether these points'
          ' are still inside the volume. \nThe amount of points that are '
          'still inside the volume compared to the amount of starting points'
          ' is the survivor fraction.')
    print('\nThe '+colored('visual_simulation()','green')+
          ' method uses a random starting point as zeroth generation. '
          '\nIt then calculates up to seven generations (maximum 128 points) of fission '
          'and plots the point on a 3D matplotlib plot.')
    print('\nThe '+colored('Simulator','green')+' class has two subclasses: '+
          colored('BeamSim','green')+' and '+colored('SphereSim','green'))
    print('These use the functions from the parent class with added'
          ' restraints for the checks, startpoint generation and'
          ' they also add a visualization of the shape on the plot.')
    print('\nIn the next section, we will show how these methods work.')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    print("\033[H\033[2J", end="")
    print('We will first showcase the simulation of the sphere. '
          'This simulation takes the same input arguments as'
          ' the parent class')
    print(colored(''))
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    print("\033[H\033[2J", end="")
    # first task
    print(colored('First task: finding the critical mass'
                  ' of a square.',attrs=['bold'])+ '\n')
    print('First, we will estimate the mass using big steps')
    header=["Mass", "Survivor fraction"]
    table=[]
    for i in [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]:
        simobject=BeamSim(i, 1, 100)
        table.append([i,simobject.surviror_fraction().fraction])
    print(tab.tabulate(table, headers=header, tablefmt="grid"))
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    print("\nWe see that the critical mass is somewhere around 1.5 "
          "if we do these simulations multiple times. "
          "We will now take a smaller step to get closer to "
          "a survivor fraction of 1."
          "\nWe will also set the amount of simmulated points to"
          " 500 for a more precise estimate.\n")
    body=[]
    for i in [1.45, 1.46, 1.47, 1.48, 1.49, 1.5,1.51,1.52,1.53,1.54,1.55]:
        simobject2 = BeamSim(i, 1, 500)
        body.append([i, simobject2.surviror_fraction().fraction])

    print(tab.tabulate(body, headers=header, tablefmt="grid"))
    print('\nIf we run these simulations a couple of times,'
          ' we see that the value fluctuates.'
          ' We therefore conclude that the critical mass is 1.5,'
          ' with an error margin of 0.3. ')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    print("\033[H\033[2J", end="")
    # second task

