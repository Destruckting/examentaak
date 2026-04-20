"""
particle class and subclasses
Dylan Assinner (dylan.assinner@student.uantwerpen.be)
last updated: 20/04/2026
"""
from collections import namedtuple
import numpy as np
from termcolor import colored

class Particle:
    """Particle class"""
    def __init__(self,xpos : float, ypos : float, zpos : float):
        """Initialise particle"""
        self.xpos=xpos
        self.ypos=ypos
        self.zpos=zpos
    @property
    def xpos(self):
        """Particle x position"""
        return self._xpos
    @xpos.setter
    def xpos(self,newxpos):
        """Particle x position setter"""
        if not isinstance(newxpos,(float,int)):
            raise TypeError
        self._xpos=newxpos
    @property
    def ypos(self):
        """Particle y position"""
        return self._ypos
    @ypos.setter
    def ypos(self, newypos):
        """Particle y position setter"""
        if not isinstance(newypos, (float, int)):
            raise TypeError
        self._ypos = newypos
    @property
    def zpos(self):
        """Particle z position"""
        return self._zpos
    @zpos.setter
    def zpos(self, newzpos):
        """Particle z position setter"""
        if not isinstance(newzpos, (float, int)):
            raise TypeError
        self._zpos = newzpos
    def __repr__(self) -> str:
        """Printable representation of particle"""
        return f'{self.__class__.__name__}(xpos={self.xpos}, ypos={self.ypos}, zpos={self.zpos})'
    def __str__(self) -> str:
        """Printable representation of particle"""
        return f'{self.__class__.__name__} at point (x={self.xpos}, y={self.ypos}, z={self.zpos})'

class Neutron(Particle):
    """Neutron class"""
    def __init__(self,xpos,ypos,zpos):
        """initialize the class with integrated random number generator"""
        super().__init__(xpos,ypos,zpos)
        self.phi=self.randomphi()
        self.theta=self.randomtheta()
        self.dist=self.randomdistance()
    @property
    def theta(self):
        """theta property"""
        return self._theta
    @theta.setter
    def theta(self,theta):
        """theta setter"""
        self._theta=theta
    @property
    def phi(self):
        """phi property"""
        return self._phi
    @phi.setter
    def phi(self,phi):
        """phi setter"""
        self._phi=phi
    @property
    def dist(self):
        """distance property"""
        return self._dist
    @dist.setter
    def dist(self,dist):
        """distance setter"""
        self._dist=dist
    @staticmethod
    def randomphi() -> float:
        """randomizing phi"""
        randkey_phi=np.random.default_rng()
        randnum_phi=randkey_phi.uniform(0,1)
        randval_phi=2*np.pi*randnum_phi
        return randval_phi
    @staticmethod
    def randomtheta() -> float:
        """randomizing theta"""
        randkey_theta=np.random.default_rng()
        randnum_theta=randkey_theta.uniform(-1, 1)
        randval_theta=np.arccos(randnum_theta)
        return float(randval_theta)
    @staticmethod
    def randomdistance() -> float:
        """randomizing distance"""
        randkey_dist=np.random.default_rng()
        randnum_dist=randkey_dist.uniform(0,1)
        return float(randnum_dist)
    def endpoint(self) -> tuple:
        """calculates the endpoint of the particle"""
        newx=self.xpos+self.dist*np.sin(self.theta)*np.cos(self.phi)
        newy=self.ypos+self.dist*np.sin(self.theta)*np.sin(self.phi)
        newz=self.zpos+self.dist*np.cos(self.theta)
        out=namedtuple('newpositions','x y z')
        output=out(float(newx),float(newy),float(newz))
        return output

class Uranium(Particle):
    """Uranium class"""
    def __init__(self,neutron : Neutron):
        if not type(neutron)==Neutron:
            raise TypeError(colored("This type of input is not supported."))
        self.xpos=neutron.endpoint().x
        self.ypos=neutron.endpoint().y
        self.zpos=neutron.endpoint().z
    def fission(self) -> Neutron:
        newneutron1=Neutron(self.xpos,self.ypos,self.zpos)
        newneutron2=Neutron(self.xpos,self.ypos,self.zpos)
        out=namedtuple('fission','neutron1 neutron2')
        output=out(newneutron1,newneutron2)
        return output

if __name__ == '__main__':
    myparticle=Neutron(0,0,0)
    myuranium=Uranium(myparticle)
    print(myuranium)
    print(myuranium.fission())
    Uranium("Hello World!")
