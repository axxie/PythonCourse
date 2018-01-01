import os
import pygame
import pygame.draw
from math import cos, sin, pi


class Line(object):
    def __init__(self, x1, y1, x2, y2, is_down, width, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.is_down = is_down
        self.width = width
        self.color = color


class Turtle(object):
    all = []

    def __init__(self):
        self.angle = 0
        self.x = 0
        self.y = 0
        self.is_down = True
        self.lines = []
        self.cur_width = 1
        self.cur_color = (255, 255, 255)
        Turtle.all.append(self)

    def fw(self, px):
        new_x = self.x + px * cos(self.angle)
        new_y = self.y - px * sin(self.angle)
        self._update(new_x, new_y)

    def left(self, angle):
        self.angle += angle * pi / 180

    def right(self, angle):
        self.angle -= angle * pi / 180

    def up(self):
        self.is_down = False

    def down(self):
        self.is_down = True

    def width(self, w):
        self.cur_width = w

    def color(self, c):
        self.cur_color = c

    def circle(self, radius, extent=None):
        if extent is None:
            extent = 360.0
        frac = abs(extent) / 360.0
        steps = 1 + int(max(11 + abs(radius), 5) * frac)
        w = 1.0 * extent / steps
        w2 = 0.5 * w
        l = 2.0 * radius * sin(w2 * pi / 180.0)
        if radius < 0:
            l, w, w2 = -l, -w, -w2

        self.left(w2)
        for i in range(steps):
            self.fw(l)
            self.left(w)
        self.right(w2)

    def _update(self, new_x, new_y):
        self.lines.append(Line(self.x, self.y, new_x, new_y, self.is_down, self.cur_width, self.cur_color))
        self.x = new_x
        self.y = new_y


default = Turtle()


def fw(px):
    default.fw(px)


def left(angle):
    default.left(angle)


def right(angle):
    default.right(angle)


def up():
    default.up()


def down():
    default.down()


def width(w):
    default.width(w)


def color(c):
    default.color(c)


def circle(radius, extent):
    default.circle(radius, extent)


def main():
    screenshot_path = os.environ.get("SCREENSHOT_PATH", None)
    pygame.init()

    if screenshot_path:
        size = 400, 300
    else:
        size = 800, 600

    width, height = size

    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    try:
        while 1:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                screen.fill((0, 0, 0))
                for t in Turtle.all:
                    (x, y) = size = event.dict["size"]
                    x /= 2
                    y /= 2

                    for line in t.lines:
                        if line.is_down:
                            pygame.draw.line(screen, line.color, (x + line.x1, y + line.y1),
                                             (x + line.x2, y + line.y2), line.width)
                pygame.display.flip()
                if screenshot_path:
                    pygame.image.save(screen, screenshot_path)
                    pygame.quit()
                    return
    finally:
        pygame.quit()
