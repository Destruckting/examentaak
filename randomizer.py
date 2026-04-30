"""
randomizer of theta, phi and distance for fission simulation (testing file)
Dylan Assinner (dylan.assinner@student.uantwerpen.be)
last update: 30/04/2026
"""
import numpy as np
from matplotlib import pyplot as plt


class Randomizer:
    """Randomizer class"""
    def __init__(self):
        """initialize the random number generator"""
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
    def __repr__(self):
        """representing the random number generator"""
        return f'Randomizer(dist={self.dist}, phi={self.phi}, theta={self.theta})'
    def __str__(self):
        """representing the random number generator"""
        self.theta=float(self.theta*(180/np.pi))
        return f'randomized numbers: distance={self.dist}, phi={self.phi}, theta={self.theta}'
    def randomphi(self):
        """randomizing phi"""
        randkey_phi=np.random.default_rng()
        randnum_phi=randkey_phi.uniform(0,1)
        randval_phi=2*np.pi*randnum_phi
        return randval_phi
    def randomtheta(self):
        """randomizing theta"""
        randkey_theta=np.random.default_rng()
        randnum_theta=randkey_theta.uniform(-0.5, 0.5)
        randval_theta=np.arccos((randnum_theta))
        return float(randval_theta)
    def randomdistance(self):
        randkey_dist=np.random.default_rng()
        randnum_dist=randkey_dist.uniform(0,1)
        return float(randnum_dist)

if __name__=='__main__':
    cosnorm=np.zeros(1000)
    for i in range (1000):
        cosnorm[i] = float(Randomizer().theta * 180 / np.pi)
    thetanorm=np.zeros(1000)
    for i in range (1000):
        thetanorm[i] = float(np.random.default_rng().uniform(0, 180))
    _,axs=plt.subplots(nrows=2,ncols=2)
    count1,bin1=np.histogram(cosnorm,bins=100)
    count2,bin2=np.histogram(thetanorm,bins=100)
    count3,bin3=np.histogram(np.cos(cosnorm),bins=100)
    count4,bin4=np.histogram(np.cos(thetanorm),bins=100)
    axs[0,0].stairs(count1, bin1)
    axs[0,0].set_title('cosnorm')
    axs[0,1].stairs(count2, bin2)
    axs[0,1].set_title('thetanorm')
    axs[1,0].stairs(count3, bin3)
    axs[1,0].set_title('cos(cosnorm)')
    axs[1,1].stairs(count4, bin4)
    axs[1,1].set_title('cos(thetanorm)')
    plt.show()
