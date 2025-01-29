# example1.py
import math
from penrose import PenroseP3, BtileL, psi

scale = 100
ngen = 6
width, height = 1200, 900
#width = height = '100%'

config={'tile-opacity': 1, 'stroke-colour': '#fff', 'base-stroke-width': 0.1,
        'Stile-colour': '#66ff66', 'Ltile-colour': '#006600',
        'stroke-colour': 'none',
        'width': width, 'height': height, 'rotate': math.pi/2}
#-50.0 -70.0 110.0 110.0

tiling = PenroseP3(scale, ngen=ngen, config=config)

theta = math.pi / 5
A1 = -scale / psi / 2
C1 = -A1
B1 = scale * math.sin(theta) * 1j

C2 = C1
B2 = B1
CA = A1-C1
rot = math.cos(-theta) + 1j * math.sin(-theta)
CA2 = CA * rot * rot
A2 = C2 + CA2

A3 = A2
C3 = C2

print(A1, B1, C1)
print(A2, B2, C2)

tiling.set_initial_tiles([BtileL(A1, B1, C1), BtileL(A2, B2, C2)])
tiling.make_tiling()

tiling.write_svg('example7.svg')
