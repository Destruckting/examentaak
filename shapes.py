"""
shapes and subclasses
Dylan Assinner (dylan.assinner@student.uantwerpen.be)
last updated: 20/04/2026
"""
from termcolor import colored
import numpy as np
from collections import namedtuple

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, newx):
        if not isinstance(newx, (int, float)):
            raise TypeError(colored('x must be an integer or a float', 'red'))
        self._x = newx

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, newy):
        if not isinstance(newy, (int, float)):
            raise TypeError(colored('y must be an integer or a float', 'red'))
        self._y = newy

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self,newz):
        if not isinstance(newz, (int, float)):
            raise TypeError(colored('z must be an integer or a float', 'red'))
        self._z = newz

    def __add__(self, other):
        """Adding two points"""
        if not isinstance(other, Point):
            raise TypeError(colored('Second point must be an instance'
                                    ' of Point', 'red'))
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        """Subtracting two points"""
        if not isinstance(other, Point):
            raise TypeError(colored('Second point must be an instance'
                                    ' of Point','red'))
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    def spherecoord(self):
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
        return self._amount

    @amount.setter
    def amount(self, newamount):
        if not isinstance(newamount,int):
            raise TypeError(colored('amount must be an integer', 'red'))
        if not newamount>0:
            raise ValueError(colored('amount must be a value greater than zero','red'))
        self._amount = newamount

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, newcenter):
        if not isinstance(newcenter,Point):
            raise TypeError(colored('center must be a Point','red'))
        self._center = newcenter

