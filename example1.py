# example1.py
import math
from penrose import PenroseP3, BtileL, psi

# A simple example starting with a BL tile

scale = 100
tiling = PenroseP3(scale, ngen=5)

theta = 2*math.pi / 5
rot = math.cos(theta) + 1j*math.sin(theta)
A = -scale/2 + 0j
B = scale/2 * rot
C = scale/2 / psi + 0j
tiling.set_initial_tiles([BtileL(A, B, C)])
tiling.make_tiling()

tiling.write_svg('example1.svg')
