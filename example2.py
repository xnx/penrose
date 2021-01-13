# example2.py
import math
import webbrowser
from penrose import PenroseP3, BtileS

# A "sun", with randomly-coloured tiles and including arc paths|

scale = 100
# Configuration of the tiling
config = {'draw-arcs': True, 'normal-arcs': False, 'tile-opacity': 0.6,
          'base-stroke-width': 0.1, 'random-tile-colours': True, 'draw-tiles': True,
          'Aarc-colour': '#000', 'Carc-colour': '#000', 'proportion': 0.4}
tiling = PenroseP3(scale, ngen=5, config=config)

# Create the initial tiles, a triangle
theta = math.pi / 5
#  alpha = math.cos(theta)
rot = math.cos(theta) + 1j*math.sin(theta)
A1 = scale + 0.j
B = 0 + 0j
C1 = C2 = A1 * rot
A2 = A3 = C1 * rot
C3 = C4 = A3 * rot
A4 = A5 = C4 * rot
C5 = -A1
tiling.set_initial_tiles([BtileS(A1, B, C1), BtileS(A2, B, C2),
                          BtileS(A3, B, C3), BtileS(A4, B, C4),
                          BtileS(A5, B, C5)])
tiling.make_tiling()
tiling.write_svg('pictures/example2.svg')
webbrowser.open('C:/Users/flynn/PycharmProjects/penrose/pictures/example2.svg')

