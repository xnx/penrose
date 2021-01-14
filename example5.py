# example1.py
import math
import webbrowser
from penrose import PenroseP3, BtileL, psi

# A simple example starting with a BL tile

scale = 100
# Configuration of the tiling
config = {'draw-arcs': True,
          'Aarc-colour': '#f44',
          'Carc-colour': '#44f',
          'tile-opacity': 0.6}
tiling = PenroseP3(scale, ngen=7, config=config)

theta = 2*math.pi / 5
rot = math.cos(theta) + 1j*math.sin(theta)
A = -scale/2 + 0j
B = scale/2 * rot
C = scale/2 / psi + 0j
tiling.set_initial_tiles([BtileL(A, B, C)])
tiling.make_tiling()

tiling.write_svg('pictures/example5.svg')
webbrowser.open('C:/Users/flynn/PycharmProjects/penrose/pictures/example5.svg')
