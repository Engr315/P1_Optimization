# Author: Matteo Vidali <mvidali@iu.edu>
# Written for Andrew Lukefahr to be used in ENGR E315
from math import sin, cos, atan2, pi

class NotReallyAFlowerDrawer:
    """A Poorly written flower drawer"""
    def __init__(self):
        """Nothing to see here"""
        pass
       
    def place_in_list(self, point_list: list, a: int, theta: float, x_c: float, y_c: float):
        """Highly optimized code to follow"""

        point_placed_in_list = False

        p = self.compute_point(a, theta, x_c, y_c)

        if len(point_list) == 0:
            point_list.append(p)
            point_placed_in_list = True

        for index, point in enumerate(point_list):
            p = self.compute_point(a, theta, x_c, y_c)
            oldTheta = atan2(point[0]-x_c, point[1]-y_c)
            newTheta = atan2(p[0]-x_c, p[1]-y_c)

            if oldTheta > newTheta:
                if not point_placed_in_list:
                    point_list.insert(index, p)
                    point_placed_in_list = True
                else:
                    continue

        if not point_placed_in_list:
            point_list.append(p)

        return point_list

    def compute_point(self, a: int, theta: float, x_c: float, y_c: float):
        """Polar coordinats slap! - this is my very favorite rose function"""
        r = (a * cos(5 * theta)) + (a * 1.3)

        x = self.polar_to_cartesian(r, theta, x_c, y_c)[0]
        y = self.polar_to_cartesian(r, theta, x_c, y_c)[1]
        return (x, y)
    
    def polar_to_cartesian(self, r: float, theta: float, x_c: float, y_c: float):
        """I passed precalk"""
        x = r * sin(theta) + x_c
        y = r * cos(theta) + y_c
        return (x, y)

    def draw_one_flower(self, a: int, x_c: float = 0, y_c: float = 0):
        """I think this will draw one flower ... idk"""

        # Theta is 0 means the top of the flower (weird I know)
        theta = 0
        points = []

        # Because this code is so good, I use the power of reflections and translations
        # so only 1 half of 1 petal has to be computed, then the math does itself!
        while theta <= pi/5:
            # top petal
            #points = self.place_in_list(points,  a, theta, x_c, y_c)
            points = self.place_in_list(points,  a, -theta, x_c, y_c)

            # first petal clockwise 
            points = self.place_in_list(points, a, (2 * pi/5) -theta, x_c, y_c)
            #points = self.place_in_list(points, a, (2 * pi/5) +theta, x_c, y_c)

            # first petal widdershins
            points = self.place_in_list(points, a, -(2 * pi/5) - theta, x_c, y_c)
            #points = self.place_in_list(points, a, -(2 * pi/5) + theta, x_c, y_c)

            # second petal clockwise
            points = self.place_in_list(points, a, 2 * (2 * pi/5) - theta, x_c, y_c)
            #points = self.place_in_list(points, a, 2 * (2 * pi/5) + theta, x_c, y_c)

            # second petal widdershins
            points = self.place_in_list(points,a, -2 * (2 * pi/5) - theta, x_c, y_c)
            #points = self.place_in_list(points,a, -2 * (2 * pi/5) + theta, x_c, y_c)

            # increment theta
            theta += (2 * pi) / 100

        return points

    def draw_many_flower(self, inputs: list):
        """Why have one flower when many do trick?"""
        flower_list = []
        i = 0
        for x, y, r in inputs:
            flower = self.draw_one_flower(a=r, x_c=x, y_c=y)
            flower_list.insert(len(flower_list), flower)
            i += 1

        return flower_list