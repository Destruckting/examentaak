"""
particle class and subclasses
Dylan Assinner (dylan.assinner@student.uantwerpen.be)
last updated: 31/03/2026
"""
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

if __name__ == '__main__':
    myparticle=Neutron(1,2,3)
    mypar=Particle(7,42,69)
    print(myparticle)
    print(mypar)
