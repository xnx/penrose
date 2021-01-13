"""
Using base from example2.py to create a gif
"""

import math
import webbrowser
from penrose import PenroseP3, BtileS

# A simple example starting with a BS tile

scale = 100
theta = math.pi / 5
# Configuration of the tiling
config = {'normal-arcs': False, 'draw-arcs': True, 'reflect-x': False,
          'draw-tiles': True, 'Aarc-colour': '#000', 'Carc-colour': '#000',
          'rotate': theta/2}
tiling = PenroseP3(scale, ngen=0, config=config)

rot = math.cos(theta) + 1j*math.sin(-theta)
A = scale + 0j
B = 0 + 0j
C = A * rot

for i in range(6):
    tiling.ngen = i
    tiling.set_initial_tiles([BtileS(A - A, B - A, C - A)])
    tiling.make_tiling()

    tiling.write_svg('pictures/sequence_2_{}.svg'.format(i))
    webbrowser.open('C:/Users/flynn/PycharmProjects/penrose/pictures/sequence_2_{}.svg'.format(i))
