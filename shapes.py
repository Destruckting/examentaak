"""
shapes and subclasses
Dylan Assinner (dylan.assinner@student.uantwerpen.be)
last updated: 20/04/2026
"""

from collections import namedtuple
from particle import Neutron, Uranium
from termcolor import colored
import numpy as np


class Point:
    """Point class"""
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    @property
    def x(self):
        """x property"""
        return self._x

    @x.setter
    def x(self, newx):
        """x setter"""
        if not isinstance(newx, (int, float)):
            raise TypeError(colored('x must be an integer or a float', 'red'))
        self._x = newx

    @property
    def y(self):
        """y property"""
        return self._y

    @y.setter
    def y(self, newy):
        """y setter"""
        if not isinstance(newy, (int, float)):
            raise TypeError(colored('y must be an integer or a float', 'red'))
        self._y = newy

    @property
    def z(self):
        """z property"""
        return self._z

    @z.setter
    def z(self,newz):
        """z setter"""
        if not isinstance(newz, (int, float)):
            raise TypeError(colored('z must be an integer or a float', 'red'))
        self._z = newz

    def __add__(self, other) -> Point:
        """Adding two points"""
        if not isinstance(other, Point):
            raise TypeError(colored('Second point must be an instance'
                                    ' of Point', 'red'))
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other) -> Point:
        """Subtracting two points"""
        if not isinstance(other, Point):
            raise TypeError(colored('Second point must be an instance'
                                    ' of Point','red'))
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    def spherecoord(self) -> tuple:
        """converting to spherical coordinates"""
        dist = float(np.sqrt(self.x**2+self.y**2+self.z**2))
        phi = float(np.arccos(self.z/dist))
        theta = float(np.arctan(self.y/self.x))
        sph=namedtuple(
            'sphere_coord', 'dist theta phi')
        sphere=sph(dist,theta,phi)
        return sphere


class Simulator:
    """shapes parent class"""
    def __init__(self, amount_of_points=100, center=Point(0, 0, 0)):
        """init shapes class"""
        self.amount = amount_of_points
        self.center = center

    @property
    def amount(self):
        """amount property"""
        return self._amount

    @amount.setter
    def amount(self, newamount):
        """amount setter"""
        if not isinstance(newamount,int):
            raise TypeError(colored('amount must be an integer', 'red'))
        if not newamount>0:
            raise ValueError(colored('amount must be a value greater than zero','red'))
        self._amount = newamount

    @property
    def center(self):
        """center property"""
        return self._center

    @center.setter
    def center(self, newcenter):
        """center setter"""
        if not isinstance(newcenter,Point):
            raise TypeError(colored('center must be a Point','red'))
        self._center = newcenter


class BeamSim(Simulator):
    """simulates beam of uranium"""
    def __init__(self, mass: float, scale: float, amount_of_points=100, center=Point(0, 0, 0)):
        """init beam simmulator class"""
        super().__init__(amount_of_points, center)
        self.mass = mass
        self.scale = scale
        self._a=(self.mass*self.scale)**(1/3)
        self._b=(self.mass/(self.scale**2))**(1/3)

    @property
    def mass(self):
        """mass property"""
        return self._mass

    @mass.setter
    def mass(self, newmass):
        """mass setter"""
        if not isinstance(newmass, (int, float)):
            raise TypeError(colored('mass must be an integer or a float', 'red'))
        if not newmass>0:
            raise ValueError(colored('mass must be a value greater than zero','red'))
        self._mass = newmass

    @property
    def scale(self):
        """scale property"""
        return self._scale

    @scale.setter
    def scale(self, newscale):
        """scale setter"""
        if not isinstance(newscale, (int, float)):
            raise TypeError(colored('scale must be an integer or a float', 'red'))
        if not newscale>0:
            raise ValueError(colored('scale must be a value greater than zero','red'))
        self._scale = newscale

    @property
    def a(self):
        """a property"""
        return self._a
    @property
    def b(self):
        """b property"""
        return self._b

    @staticmethod
    def randomx(self) -> float:
        """ x randomizer"""
        randkey_x = np.random.default_rng()
        randnum_x = randkey_x.uniform(-0.5, 0.5)
        x_value= self.a*randnum_x
        return float(x_value)
    @staticmethod
    def randomy(self) -> float:
        """y randomizer"""
        randkey_y = np.random.default_rng()
        randnum_y = randkey_y.uniform(-0.5, 0.5)
        y_value=self.a*randnum_y
        return float(y_value)
    @staticmethod
    def randomz(self) -> float:
        """z randomizer"""
        randkey_z = np.random.default_rng()
        randnum_z = randkey_z.uniform(-0.5, 0.5)
        z_value=self.b*randnum_z
        return float(z_value)

    def in_particle(self,x ,y ,z):
        if (x>(self.center.x-self.a/2) and x<(self.center.x+self.a/2)
                and (y>self.center.y-self.a/2) and (y<self.center.y+self.a/2)
                and (z>self.center.z-self.a/2) and (z<self.center.z+self.a/2)):
            return True
        else:
            return False
    def survirorfrac(self)->float:
        """calculate surviror fraction"""
        in_volume=0
        out_volume=0
        for i in range(self.amount):
            neutron=Neutron(self.randomx(),self.randomy(),self.randomz())
            uranium=Uranium(neutron)
            for i,particle in uranium.fission():
                if self.in_particle(particle.xpos,particle.ypos,particle.zpos):
                    in_volume=in_volume+1
                else:
                    out_volume=out_volume+1
        fraction=in_volume/self.amount
        percent_in=in_volume/(2*self.amount)
        percent_out=out_volume/(2*self.amount)
        tup=namedtuple('data','percent_in percent_out survivor_fraction')
        data=tup(percent_in,percent_out,fraction)
        return data



