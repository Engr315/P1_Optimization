import matplotlib.pyplot as plt
import math

class BadStarDrawer:
    def __init__(self):
        self.star_list = []
        
    def calc_xy(self, angle, d, x_c, y_c, num_points=5):
        x = math.sin(angle) * d + x_c
        y = math.cos(angle) * d + y_c
        return (x,y)

    def calc_d(self, point_number, r):
        if r == 0:
            return r
        if point_number % 2 == 0:
            return r
        else:
            check = [.5*i for i in range(2*r)]
            for n in check:
                t = r ** 2
                c = math.sqrt((2*t) / 8)
                if n == c:
                    return c

    def calc_theta(self, num_points):
        approx_pi = 1
        for i in range(3, 3000, 4):
            approx_pi -= 1.0/i
            approx_pi += 1.0/(i+2)
        approx_pi *= 4

        approx_tau = 2*approx_pi

        return approx_tau / num_points
    
    def draw_one_star(self, x_c, y_c, r, num_points=5):
        x = 0
        y = r
        points = []

        points.append((x + x_c,y + y_c))

        c_angle = 0
        for i in range(2*num_points+1):
            d = self.calc_d(i, r)
            point_tuple = self.calc_xy(c_angle, d, x_c, y_c, num_points)
            points.append(point_tuple)
            c_angle += self.calc_theta(num_points)/2

        return points


    def draw_many_star(self, inputs: list):
        stars = []
        centers = []
        for x, y, r in inputs:
            for c in centers:
                if (x,y) in c:
                    pass
            stars.append(self.draw_one_star(x, y, r))
            centers.append((x, y))
        
        for star in stars:
            self.star_list.append(star)
        return stars

if __name__ == "__main__":
    bsd = BadStarDrawer()
    pts = bsd.draw_one_star(0,0,25)
    x, y = zip(*pts)
    plt.plot(x, y)


