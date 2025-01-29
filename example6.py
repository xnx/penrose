# example6.py
import math
from penrose import PenroseP3, BtileS, BtileL

# A "sun" with colours varying with distance from the centre.

scale = 100

def get_h(e):
    r = abs(e.centre()) / scale
    v = 15-min(int(15*r), 15)
    return hex(v)[2]
def Ltile_colour(e):
    return '#{0}{0}{0}'.format(get_h(e))
def Stile_colour(e):
    return '#{0}{0}{0}'.format(get_h(e))

config={'tile-opacity': 1, 'stroke-colour': '#fff', 'base-stroke-width': 0,
        'Stile-colour': Stile_colour, 'Ltile-colour': Ltile_colour}
tiling = PenroseP3(scale*1.1, ngen=4, config=config)

theta = math.pi / 5
alpha = math.cos(theta)
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
tiling.write_svg('example6.svg')

