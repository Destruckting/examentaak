"""
shapes and subclasses
Dylan Assinner (dylan.assinner@student.uantwerpen.be)
last updated: 20/04/2026
"""
import os
from termcolor import colored

os.system('color')

class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,newx):
        if not isinstance(newx,(int,float)):
            raise TypeError(colored('x must be an integer or a float','red'))
        self._x=newx

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,newy):
        if not isinstance(newy,(int,float)):
            raise TypeError(colored('y must be an integer or a float','red'))
        self._y=newy

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self,newz):
        if not isinstance(newz,(int,float)):
            raise TypeError(colored('z must be an integer or a float','red'))
        self._z=newz

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError(colored('Second point must be an instance of Point','red'))
        return Point(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise TypeError(colored('Second point must be an instance of Point','red'))
        return Point(self.x-other.x,self.y-other.y,self.z-other.z)


class simulator():
    """shapes parent class"""
    def __init__(self,amount_of_points=100, center=Point(0,0,0)):
        """init shapes class"""
        self.amount=amount_of_points
        self.center=center
