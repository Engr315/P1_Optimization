# Author: Matteo Vidali <mvidali@iu.edu>
# Written for Andrew Lukefahr to be used in ENGR E315

# TODO: Make this bad

from math import sin, cos, pi

class BadFlowerDrawer:
    """A Poorly written flower drawer"""
    def __init__(self):
        """Nothing to see here"""
        pass

    def calc_thetas(self, num_thetas: int=5000):
        """I Wonder what I do?"""
        step = (2*pi) / num_thetas 
        return [i * step for i in range(num_thetas+1)]
        
    def draw_one_flower(self, x_c: float = 0, y_c: float = 0, petal_len: int = 1, num_petals: int = 5):
        """I think this will draw one flower ... idk"""
        thetas = self.calc_thetas()
        points = []
        for t in thetas:
            r = self.compute_r_polar(petal_len, num_petals, t)
            point = self.polar_to_cartesian(r, t, x_c, y_c)
            points.insert(len(points), point)

        return zip(*points)

    def compute_r_polar(self, a: int, n: int, theta: float):
        """Polar coordinats slap! - this is my very favorite rose function"""
        return a * cos(n * theta) + (1.3*a)
    
    def polar_to_cartesian(self, r: float, theta: float, x_c: float, y_c: float):
        """I passed precalk"""
        x = r * sin(theta) + x_c
        y = r * cos(theta) + y_c
        return (x, y)

    def draw_many_flower(self, inputs: list):
        """Why have one flower when many do trick?"""
        flowers = []

        for x, y, r in inputs:
            x, y = self.draw_one_flower(x_c=x, y_c=y, petal_len=r)
            flowers.append((x,y))

        return flowers 
