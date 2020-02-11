from appJar import gui
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

with gui() as app:
    x = range(10)
    y = range(10)
    fig = app.addPlotFig("p1")
    ax = fig.subplots()
    # Using set_dashes() to modify dashing of an existing line
    line1, = ax.plot(x, y, label='Using set_dashes()')
    # line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

    # Using plot(..., dashes=...) to set the dashing when creating a line
    line2, = ax.plot(x, y, label='Using the dashes parameter')

    ax.legend()
    plt.show()
# x = np.linspace(0, 10, 500)
# y = np.sin(x)
#
# fig, ax = plt.subplots()
#
# # Using set_dashes() to modify dashing of an existing line
# line1, = ax.plot(x, y, label='Using set_dashes()')
# line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break
#
# # Using plot(..., dashes=...) to set the dashing when creating a line
# line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label='Using the dashes parameter')
#
# ax.legend()
# plt.show()