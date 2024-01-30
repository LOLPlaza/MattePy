import sympy as sp
import pyglet as pg
import random as rnd
from pyglet import shapes
from pyglet.window import key

window = pg.window.Window(1000, 400)

color1 = (250, 0, 0)
color2 = (0, 250, 0)
color3 = (0, 0, 250)
color4 = (250, 250, 250)

circles = []
lines = []

for i in range(10):
    circles.append(shapes.Circle(rnd.uniform(100, 800), rnd.uniform(100, 300), rnd.uniform(10, 75), color1))
    lines.append(shapes.Line(rnd.uniform(100, 800), rnd.uniform(100, 300), rnd.uniform(10, 75), 1, color2))

#solution = 0

for i in range(10):
    if circles[i] in circles[i-1]:
        circles[i].color = color3
        circles[i-1].color = color3
    if circles[i] in lines[i]:
        circles[i].color = color4

# @window.event #runs the below function every time an event happens in the window?
#def on_draw():
#    if solution == 0: drawA()
#    else: drawB()

def draw10():
    for index in range(10):
        lines[index].draw()

draw10()

pg.app.run()
