# example3.py
import math
from penrose import PenroseP3, BtileL, psi

# A star with five-fold symmetry

# The Golden ratio
phi = 1 / psi
scale = 100
config = {'draw-arcs': True,
          'Aarc-colour': '#ff5e25',
          'Carc-colour': 'none',
          'Stile-colour': '#090',
          'Ltile-colour': '#9f3'}
tiling = PenroseP3(scale*2, ngen=5, config=config)

theta = 2*math.pi / 5
rot = math.cos(theta) + 1j*math.sin(theta)

B1 = scale
p = B1 * rot
q = p*rot

C5 = -scale * phi
r = C5 / rot
s = r / rot
A = [0]*5
B = [scale, p, p, q, q]
C = [s, s, r, r, C5]

tiling.set_initial_tiles([BtileL(*v) for v in zip(A, B, C)])
tiling.make_tiling()

tiling.write_svg('example3.svg')

