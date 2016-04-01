"""Module for displaying Terrain, both in 2D and 3D.

(Not accessible outside of package; use display methods of Terrain instead.)

"""

from Tkinter import Tk, Canvas, Frame, BOTH
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


class Terrain2D(Frame):
    """2D graphical representation of a Terrain object.

    Consists of a 2D top-down image of terrain as a grid of greyscale squares.
    Each square corresponds to a height value, being on a scale from white if 1 to black if 0.

    """

    SQUARE_SIDE = 3
    """Length of one side of colored square."""

    @classmethod
    def display_terrain(cls, terrain):
        """Display a Terrain in 2D.

        Args:
            terrain (Terrain): Terrain to display.

        """
        root = Tk()
        dimensions = "{0}x{1}".format(terrain.width * Terrain2D.SQUARE_SIDE,
                                      terrain.length * Terrain2D.SQUARE_SIDE)
        root.geometry(dimensions)
        app = Terrain2D(root, terrain)
        root.mainloop()

    def __init__(self, parent, terrain):
        """Make self child of a TK parent, then initialize own UI.

        Args:
            parent (TK): Parent to attach self to.
            terrain (Terrain): Terrain to display.

        """
        Frame.__init__(self, parent)
        self.terrain = terrain
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """Initialize UI of window."""
        self.parent.title("Terrain (top-down)")
        self.pack(fill=BOTH, expand=1)
        self.draw_heights()

    def draw_heights(self):
        """Draw grid of height values on window.

        Heights are shown as squares, with greyscale colors becoming brighter for greater heights.

        """
        canvas = Canvas(self)
        for x in range(self.terrain.width):
            for y in range(self.terrain.length):
                x_pos = x * Terrain2D.SQUARE_SIDE
                y_pos = y * Terrain2D.SQUARE_SIDE
                color = int(self.terrain[x, y] * 15)
                hex_color = "#" + "0123456789abcdef"[color] * 3
                canvas.create_rectangle(x_pos, y_pos,
                                        x_pos + Terrain2D.SQUARE_SIDE,
                                        y_pos + Terrain2D.SQUARE_SIDE,
                                        outline=hex_color, fill=hex_color)
        canvas.pack(fill=BOTH, expand=1)


class Terrain3D(object):
    """A 3D representation of a Terrain.

    Consists of a 3D surface mesh, shown at an angle. Can be seen at different angles.
    Uses matplotlib.mplot3d to display rudimentary 3D version of terrain.

    Notes:
        Is somewhat guaranteed to be slow. Not intended for use other than visualizing terrain during development.

    """

    def __init__(self, terrain):
        self.terrain = terrain
        self.x_grid, self.y_grid = np.meshgrid(range(self.terrain.width),
                                               range(self.terrain.length))
        z_vals = np.array([self.terrain[x, y] for x, y in zip(np.ravel(self.x_grid), np.ravel(self.y_grid))])
        self.z_grid = z_vals.reshape(self.x_grid.shape)

    def display_terrain(self):
        """Display 3D surface of terrain."""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x_grid, self.y_grid, self.z_grid)
        ax.set_zlim(0.0, 1.0)
        plt.show()
