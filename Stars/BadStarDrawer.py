import matplotlib.pyplot as plt
import math

class BadStarDrawer:
    def __init__(self):
        pass
    
    def draw_one_star(self, x_c, y_c, r, num_points=5):
        x = 0
        y = r
        points = []

        points.append((x + x_c,y + y_c))

        theta = math.tau / num_points

        c_angle = 0
        for i in range(2*num_points+1):
            if i % 2 == 0:
                d = r
            else:
                d = r/2
            x = math.sin(c_angle) * d + x_c
            y = math.cos(c_angle) * d + y_c
            points.append((x,y))        
            c_angle += theta/2

        return points


    def draw_many_star(self, inputs: list):
        circles = []
        for x, y, r in inputs:
            circles.append(self.draw_one_star(x, y, r))

        return circles

if __name__ == "__main__":
    bsd = BadStarDrawer()
    pts = bsd.draw_one_star(0,0,25)
    x, y = zip(*pts)
    plt.plot(x, y)


