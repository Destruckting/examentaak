"""
shapes and subclasses
Dylan Assinner (dylan.assinner@student.uantwerpen.be)
last updated: 20/04/2026
"""

from collections import namedtuple
from math import sqrt
from termcolor import colored
import numpy as np
from particle import Neutron, Uranium


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
    def z(self, newz):
        """z setter"""
        if not isinstance(newz, (int, float)):
            raise TypeError(colored('z must be an integer or a float', 'red'))
        self._z = newz

    def __repr__(self):
        """repr method"""
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __str__(self):
        """str method"""
        return f'(x={self.x}, y={self.y}, z={self.z})'

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
                                    ' of Point', 'red'))
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    def spherecoord(self) -> tuple:
        """converting to spherical coordinates"""
        dist = float(np.sqrt(self.x**2+self.y**2+self.z**2))
        phi = float(np.arccos(self.z/dist))
        theta = float(np.arctan(self.y/self.x))
        sph = namedtuple(
            'sphere_coord', 'dist theta phi')
        sphere = sph(dist, theta, phi)
        return sphere


class Simulator:
    """shapes parent class"""
    def __init__(self, mass: float, amount_of_points=100,
                 center=Point(0, 0, 0)):
        """init shapes class"""
        self.amount = amount_of_points
        self.center = center
        self.mass = mass

    @property
    def amount(self):
        """amount property"""
        return self._amount

    @amount.setter
    def amount(self, newamount):
        """amount setter"""
        if not isinstance(newamount, int):
            raise TypeError(colored('amount must be an integer', 'red'))
        if not newamount > 0:
            raise ValueError(colored('amount must be a value greater'
                                     ' than zero', 'red'))
        self._amount = newamount

    @property
    def center(self):
        """center property"""
        return self._center

    @center.setter
    def center(self, newcenter):
        """center setter"""
        if not isinstance(newcenter, Point):
            raise TypeError(colored('center must be a Point', 'red'))
        self._center = newcenter

    @property
    def mass(self):
        """mass property"""
        return self._mass

    @mass.setter
    def mass(self, newmass):
        """mass setter"""
        if not isinstance(newmass, (int, float)):
            raise TypeError(colored('mass must be an integer or a float',
                                    'red'))
        if not newmass > 0:
            raise ValueError(colored('mass must be a value greater than zero',
                                     'red'))
        self._mass = newmass

    def __repr__(self):
        return (f'{self.__class__.__name__}: N={self.amount},'
                f' center={self.center}, mass={self.mass}')

    def __str__(self):
        return (f'Simulator parent class, does {self.amount} simulations for '
                f'an object wit center {self.center} and mass {self.mass}')

    def in_object(self, x: float, y: float, z: float) -> bool:
        """checks if the given coordinates are in the volume """
        return True

    def randomstart(self) -> tuple:
        """random starting point"""
        return 1, 1, 1

    def survirorfrac(self) -> tuple:
        """calculate surviror fraction"""
        in_volume = 0
        out_volume = 0
        for _ in range(self.amount):
            startpos = self.randomstart()
            uranium = Uranium(startpos.x, startpos.y, startpos.z)
            for _, particle in enumerate(uranium.fission()):
                if self.in_object(particle.endpoint().x,
                                  particle.endpoint().y,
                                  particle.endpoint().z):
                    in_volume += 1
                else:
                    out_volume += 1
        fraction = in_volume/self.amount
        frac_in = in_volume/(2*self.amount)
        frac_out = out_volume/(2*self.amount)
        outtup = namedtuple('survival',
                            'fraction percent_in_volume percent_out_volume')
        output = outtup(fraction, frac_in, frac_out)
        return output


class BeamSim(Simulator):
    """simulates beam of uranium"""
    def __init__(self, mass: float, scale: float, amount_of_points=100,
                 center=Point(0, 0, 0)):
        """init beam simmulator class"""
        super().__init__(mass, amount_of_points, center)
        self.scale = scale
        self._a = (self.mass*self.scale)**(1/3)
        self._b = (self.mass/(self.scale**2))**(1/3)

    @property
    def scale(self):
        """scale property"""
        return self._scale

    @scale.setter
    def scale(self, newscale):
        """scale setter"""
        if not isinstance(newscale, (int, float)):
            raise TypeError(colored('scale must be an integer or a float',
                                    'red'))
        if not newscale > 0:
            raise ValueError(colored('scale must be a value greater'
                                     ' than zero', 'red'))
        self._scale = newscale

    @property
    def a(self):
        """a property"""
        return self._a

    @property
    def b(self):
        """b property"""
        return self._b

    def __repr__(self):
        return (f'{self.__class__.__name__}: N={self.amount},'
                f' center={self.center}, M={self.mass}, S={self.scale},'
                f' a={self.a}, b={self.b}')

    def __str__(self):
        return (f'Beam simulation: does {self.amount} simulations around'
                f' point {self.center} for a mass of {self.mass} and'
                f' dimensions: width={self.a}, height={self.a} and'
                f' depth={self.b}')

    def randomstart(self) -> tuple:
        """ starting point randomizer"""
        randkey_x = np.random.default_rng()
        randnum_x = randkey_x.uniform(-0.5, 0.5)
        x_value = self.a*randnum_x
        randkey_y = np.random.default_rng()
        randnum_y = randkey_y.uniform(-0.5, 0.5)
        y_value = self.a*randnum_y
        randkey_z = np.random.default_rng()
        randnum_z = randkey_z.uniform(-0.5, 0.5)
        z_value = self.b*randnum_z
        outtup = namedtuple('startpos', 'x y z')
        output = outtup(x_value, y_value, z_value)
        return output

    def in_object(self, x: float, y: float, z: float) -> bool:
        return bool(((self.center.x - self.a / 2) < x <
                     (self.center.x + self.a / 2) and
                     (self.center.y-self.a/2) < y <
                     (self.center.y+self.a/2) and
                     (self.center.z-self.a/2) < z <
                     (self.center.z+self.a/2)))


class SphereSim(Simulator):
    """simulates sphere of uranium"""
    def __init__(self, mass, amount_of_points=100, center=Point(0, 0, 0)):
        super().__init__(mass, amount_of_points, center)
        self.radius = float(np.cbrt(3*self.mass/(4*np.pi)))

    @property
    def radius(self):
        """radius property"""
        return self._radius

    @radius.setter
    def radius(self, newradius):
        """radius setter"""
        if not isinstance(newradius, (int, float)):
            raise TypeError(colored('radius must be an integer or a float',
                                    'red'))
        if not newradius > 0:
            raise ValueError(colored('radius must be a value greater'
                                     ' than zero', 'red'))
        self._radius = newradius

    def __repr__(self):
        return (f'{self.__class__.__name__}: N={self.amount},'
                f' center={self.center}, r={self.radius}')

    def __str__(self):
        return (f'Sphere simulation: does {self.amount} simulations around'
                f' point {self.center} for a mass of {self.mass} and'
                f' a radius of {self.radius}.')

    def randomstart(self) -> tuple:
        """start position randomizer"""
        neutron = Neutron(0, 0, 0)
        # dummy Neutron object to be able to use the static methods
        randomx = (self.center.x + (self.radius * neutron.randomdistance()) *
                   np.sin(neutron.randomtheta()) * np.cos(neutron.randomphi())
                   )
        randomy = (self.center.y + (self.radius * neutron.randomdistance()) *
                   np.sin(neutron.randomtheta()) * np.sin(neutron.randomphi())
                   )
        randomz = (self.center.z + (self.radius*neutron.randomdistance()) *
                   np.cos(neutron.randomtheta())
                   )
        outtup = namedtuple('startpos', 'x y z')
        output = outtup(randomx, randomy, randomz)
        return output

    def in_object(self, x, y, z) -> bool:
        return bool(sqrt((x - self.center.x) ** 2 +
                         (y - self.center.y) ** 2 +
                         (z-self.center.z) ** 2)
                    <= self.radius)


if __name__ == '__main__':
    testsim = BeamSim(1, 1, 100, Point(0, 0, 0))
    print(testsim)
    print(testsim.survirorfrac())
    testsphere = SphereSim(1, 100, Point(0, 0, 0))
    print(testsphere)
    print(testsphere.survirorfrac())
