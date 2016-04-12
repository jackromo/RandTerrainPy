"""This module is for the Terrain class, used for storing randomly generated terrain."""

import copy
from exceptions import *
from terraindisplay import *


class Terrain(object):
    """Container for a randomly generated area of terrain."""

    def __init__(self, width, length):
        """Initializer for Terrain.

        Args:
            width (int): Width of terrain.
            length (int): Height of terrain.

        """
        self._width = width
        self._length = length
        self._height_map = [[0 for _ in range(self.width)] for _ in range(self.length)]
        """List[list[float]]: Map of heights of all points in terrain grid."""

    @property
    def width(self):
        """int: Width of terrain."""
        return self._width

    @property
    def length(self):
        """int: Height of terrain."""
        return self._length

    def __getitem__(self, item):
        """Get an item at x-y coordinates.

        Indices out of range are taken modulo (length or width).

        Args:
            item (tuple): 2-tuple of x and y coordinates.

        Returns:
            float: Height of terrain at coordinates, between 0 and 1.

        """
        return self._height_map[item[1] % self.length][item[0] % self.width]

    def __setitem__(self, key, value):
        """Set the height of an item, bounded within 0 and 1.

        Args:
            key (tuple): 2-tuple of x and y coordinates.
            value (float): New height of map at x and y coordinates.

        Raises:
            HeightOutOfBoundsError: Value is not between 0 and 1, when rounded to 3 decimal places.

        """
        if not 0 <= round(value, 3) <= 1:
            raise HeightOutOfBoundsError()
        self._height_map[key[1] % self.length][key[0] % self.width] = round(value, 3)

    def __eq__(self, other):
        """Test equality, element by element.

        Returns:
            bool: True if all heights in first are equal to other and same dimensions, False otherwise.

        """
        if not isinstance(other, Terrain):
            return False
        elif not (other.width == self.width and other.length == self.length):
            return False
        else:
            return all(self[x, y] == other[x, y] for x in range(self.width) for y in range(self.length))

    def __add__(self, other):
        """Add two terrains, height by height. Maximum value of element is 1.

        Args:
            other (Terrain): Other terrain to add self to. Must have same dimensions as self.

        Returns:
            Terrain: Terrain of heights of self and other added together.

        Raises:
            InvalidDimensionsError: Other and self have different widths and lengths.

        """
        if other.length != self.length or other.width != self.width:
            raise InvalidDimensionsError()
        result = Terrain(self.width, self.length)
        for i in range(self.width):
            for j in range(self.length):
                val = self[i, j] + other[i, j]
                result[i, j] = 1 if val > 1 else val
        return result

    def __sub__(self, other):
        """Subtract two terrains, height by height. Minimum value of element is 0.

        Args:
            other (Terrain): Other terrain to subtract self from. Must have same dimensions as self.

        Returns:
            Terrain: Terrain of heights of self subtracted from other.

        Raises:
            InvalidDimensionsError: Other and self have different widths and lengths.

        """
        if other.length != self.length or other.width != self.width:
            raise InvalidDimensionsError()
        result = Terrain(self.width, self.length)
        for i in range(self.width):
            for j in range(self.length):
                val = self[i, j] - other[i, j]
                result[i, j] = 0 if val < 0 else val
        return result

    def __mul__(self, other):
        """Multiply self with scalar; scales all values down by scalar, bounded by 0 and 1.

        Args:
            other (float): Scalar to scale self by.

        Returns:
            Terrain: Terrain of heights of self multiplied by other.

        """
        result = Terrain(self.width, self.length)
        for i in range(self.width):
            for j in range(self.length):
                val = self[i, j] * other
                result[i, j] = val if 0 < val < 1 else (0 if val < 0 else 1)
        return result

    def __str__(self):
        """Return string representation of self.

        Returns:
            str: String of float's, to 1 decimal place, in a 2D grid of heights.

        """
        result = ""
        for x in range(self.length):
            result += "\t".join("{0:.1f}".format(abs(i)) for i in self._height_map[x]) + "\n"
        return result

    def display_2d(self):
        """Display a 2D top-down image of terrain as a grid of greyscale squares.

        Each square corresponds to a height value, being on a scale from white if 1 to black if 0.

        """
        Terrain2D.display_terrain(self)

    def display_3d(self):
        """Display a 3D image of terrain as a surface mesh.

        Notes:
            Uses matplotlib internally; is guaranteed to be somewhat slow, so intended for testing only.

        """
        Terrain3D(self).display_terrain()


class VoronoiTerrain(Terrain):
    """A Terrain where a set of regions are defined of positions closest to certain points.

    The diagram takes a preset group of points,
    and makes each position on the grid aware of which point it is closest to.

    """

    def __init__(self, width, length, points):
        """

        Args:
            width (int): Width of terrain.
            length (int): Length of terrain.
            points (list[tuple(int, int)]): List of seed points to define regions in diagram around.

        """
        super(Terrain, self).__init__(width, length)
        self._points = points
        """List[tuple(int, int)]: List of all points to define regions around."""
        self._region_map = [[0 for _ in range(self.width)] for _ in range(self.length)]
        """List[list[int]]: 2-dimensional list of indices of which point each position is closest to."""
        self._init_regions()

    def _init_regions(self):
        """Initialize region map."""
        for x in range(self.width):
            for y in range(self.length):
                min_dist = self.width**2 + self.length**2
                closest_pnt_index = 0
                for pnt in self._points:
                    dist_squared = (pnt[0] - x)**2 + (pnt[1] - y)**2
                    if dist_squared < min_dist:
                        min_dist = dist_squared
                        closest_pnt_index = self._points.index(pnt)
                self._region_map[y][x] = closest_pnt_index

    @property
    def points(self):
        """List[tuple(int, int)]: List of all points to define regions around."""
        return copy.deepcopy(self._points)  # list is mutable, don't allow user to alter it

    def get_closest_point(self, x, y):
        """Get the index of the closest point to a position.

        Args:
            x (int): X coordinate of position.
            y (int): Y coordinate of position.

        Returns:
            tuple(int, int): X-Y coordinates of closest point in Voronoi diagram to position.

        """
        return self._region_map[y][x]

    def add_point(self, x, y):
        """Add a point to make region around.

        Args:
            x (int): X coordinate of point.
            y (int): Y coordinate of point.

        """
        self._points.append((x, y))
        self._init_regions()

    def get_region(self, point_x, point_y):
        """Get all positions within the region defined around a point.

        Args:
            point_x (int): X coordinate of point to get region around.
            point_y (int): Y coordinate of point to get region around.

        Returns:
            list[tuple(int, int)]: List of 2-tuples, representing x-y coordinates of positions in region.

        """
        return [(x, y) for x in range(self.width) for y in range(self.length)
                if self.get_closest_point(x, y) == (point_x, point_y)]

    def set_region_height(self, point_x, point_y, height):
        """Set uniform height of all positions within the region defined around a point.

        Args:
            point_x (int): X coordinate of point to set region around.
            point_y (int): Y coordinate of point to set region around.
            height (float): Uniform height to set all points in region to. Between 0 and 1.

        """
        for x, y in self.get_region(point_x, point_y):
            self[x, y] = height
