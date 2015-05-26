import math
from penrose import PenroseP3, BtileL, psi

scale = 100
tiling = PenroseP3(scale, ngen=5)

theta = math.pi / 5
rot = math.cos(theta) + 1j*math.sin(theta)
A = 0 + 0j
B = scale * rot
C = scale / psi + 0j
tiling.set_initial_tiles([BtileL(A, B, C)])
tiling.make_tiling()

tiling.write_svg('example1.svg')
