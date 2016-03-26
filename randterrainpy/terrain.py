"""This module is for the Terrain class, used for storing randomly generated terrain."""


class Terrain(object):
    """Container for a randomly generated area of terrain.

    Attributes:
        width (int): Width of generated terrain.
        length (int): Length of generated terrain.
        height_map (list): Map of heights of terrain. Values range from 0 to 1.

    """

    def __init__(self, width, length):
        """Initializer for Terrain.

        Args:
            width (int): Width of terrain.
            length (int): Height of terrain.

        """
        self.width = width
        self.length = length
        self.height_map = [0 for _ in self.width] * self.length
