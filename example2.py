import math
from penrose import PenroseP3, BtileS, BtileL

# A "sun", with randomly-coloured tiles and including arc paths

scale = 100
config={'draw-arcs': True, 'tile-opacity': 0.6,
        'random-tile-colours': True, 'Aarc-colour': '#f44',
        'Carc-colour': '#44f'}
tiling = PenroseP3(scale, ngen=4, config=config)

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
tiling.write_svg('example2.svg')
