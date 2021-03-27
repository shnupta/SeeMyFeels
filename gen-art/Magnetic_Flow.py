from graphics.Graphics import setup, export
from graphics.Geometry import background, color, stroke, Line, line_width, Circle, fill, background_gradient
import math
import random
import numpy

# Some variables
height, width = 1000, 1000
grid_size = 100
border, mag_border = 50, 450
step_x, step_y = (width//grid_size), (height//grid_size)
total_steps = 1000
palette = {"grayscale": [(0.0, 0.0, 0.0), (0.5, 0.5, 0.5)]}

'''
Parameters:
1. Magnet Strength
2. Velocity
3. Number of magnets
4. Number of particles
5. 
'''

# Particle class
class Particle:
    def __init__(self, x, y, vel_x, vel_y, start_col, end_col):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.frc_x = 0
        self.frc_y = 0
        self.lx, self.ly = self.x, self.y
        self.start_col = start_col
        self.end_col = end_col
        self.draw_stroke = True

    def update(self):

        self.x = self.x + self.frc_x
        self.y = self.y + self.frc_y

        # self.vel_x = self.vel_x * 0.9
        # self.vel_y = self.vel_y * 0.9

        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y

    def edges(self):
        if self.x <= 50 or self.x >= width-50 or self.y <= 50 or self.y >= height-50:
            self.draw_stroke = False
        else:
            self.draw_stroke = True

    def reset_force(self):
        self.frc_x = 0
        self.frc_y = 0

    def set_force(self, fx, fy):
        self.frc_x = self.frc_x + fx
        self.frc_y = self.frc_y + fy

    def set_last_pos(self):
        self.lx, self.ly = self.x, self.y

    def calculate_force(self, mx, my, mp):
        dy = mx - self.x
        dx = my - self.y
        angle = math.atan2(dy, dx) * mp
        sx = math.sin(angle)
        sy = math.cos(angle)
        return [sx, sy]

    def draw(self, step):
        if self.draw_stroke is not False:
            line_width(0.9)
            col_diff = numpy.subtract(self.end_col, self.start_col)
            gradient_pos = col_diff * (step / total_steps)
            r, g, b = self.start_col
            color(r + gradient_pos[0], g + gradient_pos[1], b + gradient_pos[2], 1.0)
            Line(self.lx, self.ly, self.x, self.y)
            stroke()


# Magnet Class
class magnet:
    def __init__(self, x, y, pole):
        self.x = x
        self.y = y
        self.p = pole

    def draw(self):
        if self.p > 0:
            color(1.0, 0.0, 0.0, 1.0)
        else:
            color(0.0, 1.0, 0.0, 1.0)
        Circle(self.x, self.y, 10)
        fill()


def draw(num_magnets):
    background_gradient(100, 100, width, height, (123/255, 67/255, 151/255), (220/255, 36/255, 48/255))
    color(0.0, 0.0, 0.0, 1.0)

    magnets = []
    my_particles = []
    # num_magnets = random.randint(2, 20)
    sum_x, sum_y = 0, 0
    sums = 0

    print("Number of Magnets: " + str(num_magnets))

    for m in range(num_magnets):
        pole = 1
        if random.uniform(0, 1) < 0.5:
            pole = -pole

        magnets.append(magnet(
                random.randint(100, width-100),
                random.randint(100, height-100),
                pole
        ))

    # start_num = 360
    # a = (math.pi*2)/start_num # 1 degree in radians
    #
    # for x in range(100, width-100, (width-200)//2):
    #     for y in range(100, height-100, (height-200)//2):
    #         for i in range(start_num):
    #             xx = x + (math.sin(a*i)*random.randint(100,250)) + ((width-200)//2)
    #             yy = y + (math.cos(a*i)*random.randint(100,250)) + ((height-200)//2)
    #             vx = random.uniform(-1, 1)*0.5
    #             vy = random.uniform(-1, 1)*0.5
    #             my_particles.append(Particle(xx, yy, vx, vy))

    size = 500

    for x in range(size//2, width - size//2, 25):
        for y in range(size//2, height - size//2, 25):
            xx = x
            yy = y
            vx = 0
            vy = 0
            my_particles.append(Particle(xx, yy, vx, vy, (1 - 123/255, 1 - 67/255, 1 - 151/255), (1 - 220/255, 1 - 36/255, 1 - 48/255)))

    for p in my_particles:
        for t in range(total_steps):
            for m in magnets:
                sums = p.calculate_force(m.x, m.y, m.p)
                sum_x = sum_x + sums[0]
                sum_y = sum_y + sums[1]

            sum_x = sum_x / len(magnets)
            sum_y = sum_y / len(magnets)

            p.reset_force()
            p.set_force(sum_x, sum_y)
            p.update()
            p.edges()
            if t % 8 == 0:
                p.draw(t)
                p.set_last_pos()

    for m in magnets:
        m.draw()


def main():
    for i in range(1, 10):
        setup(width, height, "" + str(i))
        draw(i)
        export()


if __name__ == '__main__':
    main()
