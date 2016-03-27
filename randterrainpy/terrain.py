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
        self.height_map = [[0 for _ in self.width]] * self.length

    def __getitem__(self, item):
        """Get an item at x-y coordinates.

        Args:
            item (tuple): 2-tuple of x and y coordinates.

        Returns:
            float: Height of terrain at coordinates, between 0 and 1.

        """
        return self.height_map[item[1]][item[0]]

    def __setitem__(self, key, value):
        """Set the height of an item.

        Args:
            key (tuple): 2-tuple of x and y coordinates.
            value (float): New height of map at x and y coordinates, between 0 and 1.

        """
        self.height_map[key[1]][key[0]] = value
