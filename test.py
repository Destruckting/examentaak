"""
testing file
Dylan Assinner (dylan.assinner@student.uatwerpen.be)
last updated: 2/05/2026
"""

import matplotlib.pyplot as plt
from termcolor import colored
import tabulate as tab
from shapes import SphereSim, BeamSim
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
    print('To continue the program when a plot pops up, '
          +colored('close the plot','yellow')+
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
    # examples of sphere and beam
    print('We will first showcase the simulation of the sphere. '
          'This simulation takes the same input arguments as'
          ' the parent class.')
    print(colored('SphereSim','green')+'('+colored('mass','blue')+
          ', '+colored('amount of points','blue')+')')
    sphereshowcase=SphereSim(1, 100)
    print(sphereshowcase)
    print('\nWe then get the survivor fraction:')
    print(sphereshowcase.surviror_fraction())
    print('\nFor the plot we get the following result:')
    print('(Please note that the success of the simulation '
          'will vary every time this program is executed.)')
    input(colored("Press enter to show plot...", 'yellow', attrs=['bold']))
    sphereshowcase.visual_simulation()
    plt.show()
    print('\nThe simulation of the beam works the same, '
          'with an added input argument: \na scale factor that determines '
          'the relation between the depth and the width and height.')
    print(colored('SphereSim', 'green') + '(' + colored('mass', 'blue') +
          ', ' + colored('scale','blue') + ', ' +
          colored('amount of points', 'blue') + ')')
    beamshowcase = BeamSim(1, 1.5, 100)
    print(beamshowcase)
    print('\nWe then get the survivor fraction:')
    print(beamshowcase.surviror_fraction())
    print('\nFor the plot we get the following result:')
    input(colored("Press enter to show plot...", 'yellow', attrs=['bold']))
    beamshowcase.visual_simulation()
    plt.show()
    print('\nNow that we know how the program works, we can start with the tasks')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    print("\033[H\033[2J", end="")
    # first task
    print(colored('First task: finding the critical mass'
                  ' of a cube.',attrs=['bold'])+ '\n')
    print('First, we will estimate the mass using relatively large intervals.')
    header=["Mass", "Survivor fraction"]
    table=[]
    for i in [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]:
        simobject=BeamSim(i, 1, 100)
        table.append([i,simobject.surviror_fraction().fraction])
    print(tab.tabulate(table, headers=header, tablefmt="grid"))
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    print("\nWe see that the critical mass is somewhere around 1.5 "
          "if we do these simulations multiple times.\n"
          "We will now use smaller intervals to get closer to "
          "a survivor fraction of 1."
          "\nWe will also set the amount of simulated points to"
          " 1000 for a more precise estimate.\n")
    body=[]
    for i in [1.45, 1.46, 1.47, 1.48, 1.49, 1.5,
              1.51, 1.52, 1.53, 1.54, 1.55]:
        simobject2 = BeamSim(i, 1, 1000)
        body.append([i, simobject2.surviror_fraction().fraction])
    print(tab.tabulate(body, headers=header, tablefmt="grid"))
    print('\nIf we run these simulations a couple of times,'
          ' we see that the value fluctuates.\n'
          'We therefore conclude that the critical mass is 1.5,'
          ' with an error margin of 0.3. ')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    print('We can then do a last refinement in this region: (note that this may take a bit longer as we are simulating 10000 points)')
    lastone=[]
    for i in [1.47, 1.48, 1.49, 1.5, 1.51, 1.52, 1.53]:
        simobject3 = BeamSim(i, 1, 10000)
        lastone.append([i, simobject3.surviror_fraction().fraction])
    print(tab.tabulate(lastone, headers=header, tablefmt="grid"))
    print('\nThis confirms our error margin, thus we can say that our estimate is valid.')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    print("\033[H\033[2J", end="")
    # second task
    print(colored('Second task: finding the critical mass of a beam with scale 1.5 and 0.5.', attrs=['bold']))
    print('\nWe will do the same calculations as the previous task.')
    print('First, the beam with scale 1.5:')
    table = []
    for i in [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]:
        simobject = BeamSim(i, 1.5, 100)
        table.append([i, simobject.surviror_fraction().fraction])
    print(tab.tabulate(table, headers=header, tablefmt="grid"))
    print('We see that the critical mass should be somewhere around 1. \nWe will use a smaller interval to define an error margin, using 1000 points for the simulation.')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    body = []
    for i in [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3,]:
        simobject2 = BeamSim(i, 1.5, 1000)
        body.append([i, simobject2.surviror_fraction().fraction])
    print(tab.tabulate(body, headers=header, tablefmt="grid"))
    print('\nWe see that our guess of 1 is quite accurate. We will try to get a more accurate error margin.')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    lastone=[]
    for i in [0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2]:
        simobject3 = BeamSim(i, 1.5, 10000)
        lastone.append([i, simobject3.surviror_fraction().fraction])
    print(tab.tabulate(lastone, headers=header, tablefmt="grid"))
    print('\nWe see that our guess of 1 with an error margin of 0.2 was accurate enough.')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    print("\033[H\033[2J", end="")
    print('Now that we know the critical mass of the scale factor 1.5, we will also try a scale of 0.5.')
    print('Because the critical mass for a scale of 1.5 was slightly lower than the mass for a scale of 1 (cube), we expect the critical mass of scale 0.5 to be slightly higher.')
    table = []
    for i in [ 1, 1.5, 2, 2.5, 3]:
        simobject = BeamSim(i, 0.5, 100)
        table.append([i, simobject.surviror_fraction().fraction])
    print(tab.tabulate(table, headers=header, tablefmt="grid"))
    print('\nWe see that the critical mass is unexpectedly low. we will use slightly more acurate values of 1000 points to hopefully get a better estimate.')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    body = []
    for i in [1, 10, 20 ,50, 100, 200, 500, 1000]:
        simobject2 = BeamSim(i, 0.5, 1000)
        body.append([i, simobject2.surviror_fraction().fraction])
    print(tab.tabulate(body, headers=header, tablefmt="grid"))
    print("We see that the value never quite reaches 1, even for a mass of 1000, so we conclude that for some reason this system doesn't work if the scale gets too small. ")
    print('To verify our suspicion, we will also do a less acurate simulation of a scale of 2 and 0.9')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    print("\033[H\033[2J", end="")
    print('For a scale of 2, we get the following critical mass:')
    table = []
    for i in [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]:
        simobject = BeamSim(i, 2, 100)
        table.append([i, simobject.surviror_fraction().fraction])
    print(tab.tabulate(table, headers=header, tablefmt="grid"))
    print('We see that the critical mass is somewhere around 0.5.')
    body = []
    for i in [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]:
        simobject2 = BeamSim(i, 2, 1000)
        body.append([i, simobject2.surviror_fraction().fraction])
    print(tab.tabulate(body, headers=header, tablefmt="grid"))
    input(colored('\nPress enter to continue...', 'yellow', attrs=['bold']))
    close_all()
    print("\033[H\033[2J", end="")
    print('For the scale of 0.9, we will verify if this shows the same behavior as 0.5')
    body = []
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        simobject2 = BeamSim(i, 0.9, 1000)
        body.append([i, simobject2.surviror_fraction().fraction])
    print(tab.tabulate(body, headers=header, tablefmt="grid"))
    print('Because a scale of 0.9 becomes critical at a mass of around 3, we can conclude that the needed critical mass grows exponentially for smaller scale factors.')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    print("\033[H\033[2J", end="")
    # third task
    print(colored('Third task: determining the critical mass of a sphere ',attrs=['bold']))
    print('For this task, we can reuse the code from the first task, but now with the '+colored('SphereSim','green')+' class.')
    spheretab1=[]
    for i in [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]:
        sphereobject=SphereSim(i,100)
        spheretab1.append([i, sphereobject.surviror_fraction().fraction])
    print(tab.tabulate(spheretab1, headers=header, tablefmt="grid"))
    print('\nBy redoing this simulation multiple times, we can see that the critical mass is somewhere between 0.75 and 1.25.')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    spheretab2=[]
    for i in [0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.2, 1.25]:
        sphereobject2=SphereSim(i, 1000)
        spheretab2.append([i, sphereobject2.surviror_fraction().fraction])
    print(tab.tabulate(spheretab2, headers=header, tablefmt="grid"))
    print('We see that the critical mass fluctuates between 0.75 and 1. We will thus take a closer look at this section for our final estimate.')
    input(colored("\nPress enter to continue...", 'yellow', attrs=['bold']))
    close_all()
    spheretab3=[]
    for i in [0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1]:
        sphereobject3=SphereSim(i,10000)
        spheretab3.append([i, sphereobject3.surviror_fraction().fraction])
    print(tab.tabulate(spheretab3, headers=header, tablefmt="grid"))
    print('We will conclude that  this range (0.875 plus/minus 0.125) is the critical mass.')
    input(colored("\nPress enter to close program...", 'yellow', attrs=['bold']))
    close_all()
    print('\033[H\033[2J', end="")
    print('Thank you for using this program, goodbye!')

