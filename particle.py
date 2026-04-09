"""
particle class and subclasses
Dylan Assinner (dylan.assinner@student.uantwerpen.be)
last updated: 31/03/2026
"""
import numpy as np
from matplotlib import pyplot as plt

class Particle:
    """Particle class"""
    def __init__(self,xpos,ypos,zpos):
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
    def __repr__(self):
        """Printable representation of particle"""
        return f'{self.__class__.__name__}(xpos={self.xpos}, ypos={self.ypos}, zpos={self.zpos})'
    def __str__(self):
        """Printable representation of particle"""
        return f'{self.__class__.__name__} at point (x={self.xpos}, y={self.ypos}, z={self.zpos})'
class Neutron(Particle):
    """Neutron class"""
    def __init__(self,xpos,ypos,zpos):
        """initialize the random number generator"""
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
        """dist setter"""
        self._dist=dist
    def randomphi(self):
        """randomizing phi"""
        randkey_phi=np.random.default_rng()
        randnum_phi=randkey_phi.uniform(0,1)
        randval_phi=2*np.pi*randnum_phi
        return randval_phi
    def randomtheta(self):
        """randomizing theta"""
        randkey_theta=np.random.default_rng()
        randnum_theta=randkey_theta.uniform(-1, 1)
        randval_theta=np.arccos((randnum_theta))
        return float(randval_theta)
    def randomdistance(self):
        randkey_dist=np.random.default_rng()
        randnum_dist=randkey_dist.uniform(0,1)
        return float(randnum_dist)

if __name__ == '__main__':
    myparticle=Neutron(1,2,3)
    mypar=Particle(7,42,69)
    print(myparticle)
    print(mypar)
    print(myparticle.theta,myparticle.phi,myparticle.dist)
