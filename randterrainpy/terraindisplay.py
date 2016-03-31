"""Module for displaying Terrain, both in 2D and 3D.

(Not accessible outside of package; use display methods of Terrain instead.)

"""

from Tkinter import Tk, Frame, BOTH


class Terrain2D(Frame):
    """2D graphical representation of a Terrain object.

    Consists of a 2D top-down image of terrain as a grid of greyscale squares.
    Each square corresponds to a height value, being on a scale from white if 1 to black if 0.

    """

    DIMENSIONS = "250x150"
    """Dimensions of the window for a Terrain2D."""

    @classmethod
    def display_terrain(cls, terrain):
        root = Tk()
        root.geometry(Terrain2D.DIMENSIONS)
        app = Terrain2D(root, terrain)
        root.mainloop()

    def __init__(self, parent, terrain):
        Frame.__init__(self, parent)
        self.terrain = terrain
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Terrain (top-down)")
        self.pack(fill=BOTH, expand=1)
