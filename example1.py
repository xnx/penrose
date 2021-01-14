# example1.py
import math
import webbrowser
from penrose import PenroseP3, BtileL, psi

# A simple example starting with a BL tile

scale = 100
# Configuration of the tiling
config = {'draw-arcs': True,
          'normal-arcs': False,
          'Aarc-colour': '#000',
          'Carc-colour': '#000',
          'draw-tiles': False,
          'proportion': 0.5}
tiling = PenroseP3(scale, ngen=4, config=config)

# Create the initial tiles, a triangle
theta = 2*math.pi / 5
rot = math.cos(theta) + 1j*math.sin(theta)
A = -scale/2 + 0j
B = scale/2 * rot
C = scale/2 / psi + 0j
tiling.set_initial_tiles([BtileL(A, B, C)])
# Make the tiles up to ngen generations
tiling.make_tiling()

# Write and open in a browser the svg file
tiling.write_svg('pictures/example1.svg')
webbrowser.open('C:/Users/flynn/PycharmProjects/penrose/pictures/example1.svg')
