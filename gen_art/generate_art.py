from gen_art.graphics.Graphics import setup, export
from gen_art.graphics.Geometry import background, color, stroke, Line, line_width, Circle, fill, background_gradient, color_hsv
import math
import random
import numpy
import colorsys

# Some variables
height, width = 1000, 1000
total_steps = 1000


class ColourInfo:
    def __init__(self, happy, dance, aggressive, chill, acoustic):
        marker = 100 + (150 * (1 - happy))
        spread = (math.exp(3.2 * dance) - 1) * 360 / 25
        start_hue = marker - spread / 2
        end_hue = marker + spread / 2
        if start_hue < 0:
            end_hue -= start_hue
            start_hue = 0
        elif end_hue > 360:
            start_hue -= (end_hue - 360)
            end_hue = 360

        print("marker: ", marker)
        print("spread: ", spread)

        saturation = 100 - (100 * (chill / 2))
        brightness = 85 - (math.log(20 * acoustic + 1) * 35 / 3)
        print("saturation: ", saturation)
        print("brightness: ", brightness)

        self.background = (0.95, 0.95, 0.95)
        self.start_col = (start_hue / 360, saturation / 100, brightness / 100)
        self.end_col = (end_hue / 360, saturation / 100, brightness / 100)

        if self.is_chill(chill):
            print("was chill")
            self.background = colorsys.hsv_to_rgb(0.5 * math.tanh(4.5 * dance - 2) + 0.5, 0.4, 0.65)
            self.start_col = (1.0, 0.0, 1.0)
            self.end_col = (1.0, 0.0, 1.0)

        if self.is_aggressive(aggressive):
            print("was aggressive")
            self.background = (0.0, 0.0, 0.0)
            self.start_col = (1.0, 1.0, 0.75)
            self.end_col = (1.0 - dance / 2, 1.0, 0.75)

    def is_chill(self, chill):
        return chill > 0.85

    def is_aggressive(self, aggressive):
        return aggressive > 0.85


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

        self.vel_x = self.vel_x * 0.9
        self.vel_y = self.vel_y * 0.9

        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y

    def edges(self):
        # if self.x <= 50 or self.x >= width-50 or self.y <= 50 or self.y >= height-50:
        #     self.draw_stroke = False
        # else:
        #     self.draw_stroke = True
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
            color_hsv(r + gradient_pos[0], g + gradient_pos[1], b + gradient_pos[2])
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


def draw(velocity_scaling, magnet_force, magnet_range, num_particles, separation_coeff, force_jitter, colour_info):
    print(velocity_scaling)
    print(magnet_force)
    print(magnet_range)
    print(num_particles)
    print(separation_coeff)
    print(force_jitter)
    rb, gb, bb = colour_info.background
    background(rb, gb, bb, 1.0)
    color(0.0, 0.0, 0.0, 1.0)

    magnets = []
    my_particles = []
    num_magnets = 2 + magnet_range
    sum_x, sum_y = 0, 0
    sums = 0

    print("Number of Magnets: " + str(num_magnets))

    for m in range(int(num_magnets)):
        pole = 1
        if random.uniform(0, 1) < 0.5:
            pole = -pole

        magnets.append(magnet(
                random.randint(100, width-100),
                random.randint(100, height-100),
                pole
        ))

    x_increment = (width - 350) // int(math.sqrt(num_particles))
    y_increment = (height - 350) // int(math.sqrt(num_particles))
    for x in range(175, width - 175, x_increment):
        for y in range(175, height - 175, y_increment):
            x_change = random.uniform(-1, 1) * separation_coeff * x_increment
            y_change = random.uniform(-1, 1) * separation_coeff * y_increment
            xx = x + x_change
            yy = y + y_change
            vx = random.uniform(-1, 1) * velocity_scaling
            vy = random.uniform(-1, 1) * velocity_scaling
            my_particles.append(Particle(xx, yy, vx, vy, colour_info.start_col, colour_info.end_col))

    for p in my_particles:
        for t in range(total_steps):
            for m in magnets:
                f = magnet_force
                if force_jitter:
                    f = random.uniform(0.5, 2.5) * magnet_force
                sums = p.calculate_force(m.x, m.y, m.p * f)
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


def generate(output_path, happy, dance, aggressive, chill, acoustic):
    setup(width, height, output_path)
    magnet_force = 4
    colour_info = ColourInfo(happy, dance, aggressive, chill, acoustic)
    if 0.5 < aggressive < 0.8:
        magnet_force += aggressive * 10
    draw(0.5 + aggressive, magnet_force, 3 * (happy + dance), 500 + (4000 * (1 - chill)), (chill + dance) * 3, aggressive > 0.8, colour_info)
    export()
