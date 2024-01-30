import pyglet as pg
from random import randint as rnd
from pyglet import shapes

window = pg.window.Window(1000, 400)

color1 = (250, 0, 0)
color2 = (0, 250, 0)
color3 = (0, 0, 250)
color4 = (250, 250, 250)

circles = []
lines = []

batch = pg.graphics.Batch()

for i in range(10):
    circle = shapes.Circle(x=rnd(100, 800),
                           y=rnd(100, 300),
                           radius=rnd(10, 75),
                           color=color1,
                           batch=batch)
    circles.append(circle)

    # classLine(x, y, x2, y2, width=1, color=(255, 255, 255, 255), batch=None, group=None)
    line = shapes.Line(x=rnd(100, 800),
                       y=rnd(100, 300),
                       x2=rnd(100, 800),
                       y2=rnd(100, 300),
                       width=rnd(10, 75),
                       color=color2,
                       batch=batch)
    lines.append(line)

@window.event
def on_draw():
    window.clear()

    batch.draw()


pg.app.run()
