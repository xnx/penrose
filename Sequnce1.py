"""
Using base from example1.py to create a gif
"""

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
          'draw-tiles': True}
tiling = PenroseP3(scale, ngen=0, config=config)

theta = 2*math.pi / 5
rot = math.cos(theta) + 1j*math.sin(theta)
A = -scale/2 + 0j
B = scale/2 * rot
C = scale/2 / psi + 0j

for i in range(6):
    tiling.ngen = i
    tiling.set_initial_tiles([BtileL(A, B, C)])
    tiling.make_tiling()

    tiling.write_svg('pictures/sequence_1_{}.svg'.format(i))
    webbrowser.open('C:/Users/flynn/PycharmProjects/penrose/pictures/sequence_1_{}.svg'.format(i))
