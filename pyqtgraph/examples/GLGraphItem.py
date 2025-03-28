"""
Demonstrates use of GLGraphItem
"""

import sys

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import pyqtgraph.opengl as gl

if 'darwin' in sys.platform:
    fmt = QtGui.QSurfaceFormat()
    fmt.setRenderableType(fmt.RenderableType.OpenGL)
    fmt.setProfile(fmt.OpenGLContextProfile.CoreProfile)
    fmt.setVersion(4, 1)
    QtGui.QSurfaceFormat.setDefaultFormat(fmt)

app = pg.mkQApp("GLGraphItem Example")
w = gl.GLViewWidget()
w.setCameraPosition(distance=5)
w.show()

edges = np.array([
    [0, 2],
    [0, 3],
    [1, 2],
    [1, 3],
    [2, 3]
])

nodes = np.array(
    [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]
)

edgeColor=pg.glColor("w")

gi = gl.GLGraphItem(
    edges=edges,
    nodePositions=nodes,
    edgeWidth=1.,
    nodeSize=0.1,
    pxMode=False
)

w.addItem(gi)

if __name__ == "__main__":
    pg.exec()
