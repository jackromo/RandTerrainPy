"""All random generators for Terrain class."""

from terrain import Terrain
import random
import abc
import math


class TerrainGenerator(object):
    """Abstract noise generator that makes a Terrain with heights produced from noise."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        """Generate a Terrain with heights corresponding to noise.

        Returns:
            Terrain: New Terrain with heights corresponding to noise.

        """


class DiamondSquareGenerator(TerrainGenerator):
    """Terrain generator that used diamond-square algorithm."""

    def __init__(self, amp_from_freq):
        """

        Args:
            amp_from_freq (function): Function that converts frequency to maximum amplitude.

        """
        self.amp_from_freq = amp_from_freq

    def __call__(self, side_exp):
        """Generate a Terrain with heights corresponding to noise.

        Used diamond-square algorithm, with frequency of noise at each step doubling.
        Colored_noise will use the frequency to generate the offset noise.

        Width and length are equal, and length must be of form 2**n + 1 (n >= 0).

        Args:
            side_exp (int): Exponent of side length. Length of side is 2**side_exp + 1.

        Returns:
            Terrain: New Terrain with heights corresponding to noise.

        """
        side_len = (2 ** side_exp) + 1
        ter = Terrain(side_len, side_len)
        return self._divide(self._initialize_corners(ter, 0.5), side_len-1)

    def _initialize_corners(self, terrain, init_val):
        """Initialize corner values of terrain.

        Args:
            terrain (Terrain): Terrain to initialize edges of.
            init_val (float): Initial value to set all corners to, between 0 and 1.

        Returns:
            Terrain: Terrain with corners set to init_val.

        """
        terrain[0, 0] = init_val
        terrain[0, terrain.length-1] = init_val
        terrain[terrain.width-1, 0] = init_val
        terrain[terrain.width-1, terrain.length-1] = init_val
        return terrain

    def _divide(self, terrain, square_len):
        """Divide terrain into squares and process each square recursively.

        Goes through each square, altering midpoint. After this, go through each diamond, altering edges.
        (Altering constitutes setting the value to an average of adjacent values and adding a noise offset.)
        Once all are done, halve size of each square and do _divide again on half-size squares.
        Once square size goes below 1, finish.

        Args:
            terrain (Terrain): Terrain to manipulate. Must have corners initialized.
            square_len (int): Current length of one side of a square.

        Returns:
            Terrain: New terrain with generated values.

        """
        half = square_len / 2

        if half < 1:
            return terrain
        else:
            # loop through all squares
            for y in range(half, terrain.length, square_len):
                for x in range(half, terrain.width, square_len):
                    terrain = self._update_square(terrain, x, y, square_len)
            # loop through all diamonds
            for y in range(0, terrain.length, half):
                for x in range((y + half) % square_len, terrain.width, square_len):
                    terrain = self._update_diamond(terrain, x, y, square_len)
            return self._divide(terrain, half)

    def _update_square(self, terrain, x, y, square_len):
        """Update the midpoint of a square.

        Midpoint becomes average of square corners plus a random offset determined by noise.

        Args:
            terrain (Terrain): Terrain to update.
            x (int): X coordinate of center of square.
            y (int): Y coordinate of center of square.
            square_len (int): Length of one side of square.

        Returns:
            Terrain: New terrain with updated square center.

        """
        half_len = square_len / 2
        # Impossible to attempt to access neighbours out of terrain bounds
        mean_height = sum([terrain[x - half_len, y - half_len],
                           terrain[x - half_len, y + half_len],
                           terrain[x + half_len, y - half_len],
                           terrain[x + half_len, y + half_len]]) / 4.0
        frequency = terrain.length / square_len
        offset = (random.random() - 0.5) * self.amp_from_freq(frequency)
        if not 0 <= mean_height + offset <= 1:
            if mean_height + offset > 1:
                terrain[x, y] = 1
            else:
                terrain[x, y] = 0
        else:
            terrain[x, y] = mean_height + offset
        return terrain

    def _update_diamond(self, terrain, x, y, diamond_len):
        """Update the midpoint of a diamond.

        Midpoint becomes average of diamond corners plus a random offset determined by noise.

        Args:
            terrain (Terrain): Terrain to update.
            x (int): X coordinate of center of diamond.
            y (int): Y coordinate of center of diamond.
            diamond_len (int): Length of one corner of diamond to other.

        Returns:
            Terrain: New terrain with updated square center.

        """
        half_len = diamond_len / 2
        # If on edge of terrain, only access 3 neighbours to avoid leaving terrain bounds
        neighbours = []
        if x != 0:
            neighbours.append(terrain[x - half_len, y])
        if y != 0:
            neighbours.append(terrain[x, y - half_len])
        if x != terrain.width - 1:
            neighbours.append(terrain[x + half_len, y])
        if y != terrain.length - 1:
            neighbours.append(terrain[x, y + half_len])
        mean_height = sum(neighbours) / float(len(neighbours))
        frequency = terrain.length / diamond_len
        offset = (random.random() - 0.5) * self.amp_from_freq(frequency)
        if not 0 <= mean_height + offset <= 1:
            if mean_height + offset > 1:
                terrain[x, y] = 1
            else:
                terrain[x, y] = 0
        else:
            terrain[x, y] = mean_height + offset
        return terrain


class RedNoiseGenerator(DiamondSquareGenerator):
    """Diamond square terrain generator with red noise (amplitude = 1 / (frequency^2))."""

    def __new__(cls, *args, **kwargs):
        return DiamondSquareGenerator(lambda f: f ** -2)


class PinkNoiseGenerator(DiamondSquareGenerator):
    """Diamond square terrain generator with pink noise (amplitude = 1 / frequency)."""

    def __new__(cls, *args, **kwargs):
        return DiamondSquareGenerator(lambda f: f ** -1)


class WhiteNoiseGenerator(DiamondSquareGenerator):
    """Diamond square terrain generator with white noise (amplitude = 1)."""

    def __new__(cls, *args, **kwargs):
        return DiamondSquareGenerator(lambda f: 1)


class BlueNoiseGenerator(DiamondSquareGenerator):
    """Diamond square terrain generator with blue noise (amplitude = frequency)."""

    def __new__(cls, *args, **kwargs):
        return DiamondSquareGenerator(lambda f: f)


class VioletNoiseGenerator(DiamondSquareGenerator):
    """Diamond square terrain generator with violet noise (amplitude = frequency^2)."""

    def __new__(cls, *args, **kwargs):
        return DiamondSquareGenerator(lambda f: f ** 2)


class PerlinGenerator(TerrainGenerator):
    """Terrain generator that uses Perlin noise algorithm."""

    def __init__(self, square_len, width_in_squares, length_in_squares):
        """

        Args:
            square_len (int): Length of one side of a square in Perlin noise grid. Is > 0.
            width_in_squares (int): Width of generated terrain in grid squares. Is > 0.
            length_in_squares (int): Length of generated terrain in grid squares. Is > 0.

        """
        self._square_len = square_len
        self._width_in_squares = width_in_squares
        self._length_in_squares = length_in_squares
        self._linearly_interpolated = False
        self._init_gradients(1)

    def _init_gradients(self, vec_magnitude):
        """Initialize all gradient vectors to be in random directions with the same magnitude.

        Args:
            vec_magnitude (float): Magnitude of all gradient vectors.

        """
        self._grad_vecs = [[(0, 0) for _ in range(self._width_in_squares+1)] for _ in range(self._length_in_squares+1)]
        """list[list[tuple(float, float)]]: Grid of gradient vectors."""
        for x in range(self._width_in_squares+1):
            for y in range(self._length_in_squares+1):
                x_val = (random.random() - 0.5) * 2 * vec_magnitude
                y_val = math.sqrt(vec_magnitude**2 - x_val**2) * random.choice([1, -1])
                self._grad_vecs[y][x] = (x_val, y_val)

    def __call__(self, linearly_interpolated=False):
        """Generate terrain via Perlin noise.

        Args:
            linearly_interpolated (bool): Whether to linearly interpolate values or use cubic function.

        Returns:
            Terrain: Generated terrain.

        """
        self._linearly_interpolated = bool(linearly_interpolated)
        terr = Terrain(self._square_len * self._width_in_squares,
                       self._square_len * self._length_in_squares)
        for x in range(terr.width):
            for y in range(terr.length):
                terr[x, y] = self._get_noise_at(x, y)
        return terr

    def _get_noise_at(self, x, y):
        """Get perlin noise at a point in terrain.

        Does this by choosing a random gradient vector for each grid corner (done at initialization)
        and taking their dot products with the displacement vectors to each point in the grid.
        The generated values are then interpolated between based on distance to each corner from the desired point.

        Args:
            x (int): X coordinate of requested point.
            y (int): Y coordinate of requested point.

        Returns:
            float: Height of point on terrain, between 0 and 1 inclusive.

        """
        grid_x = x / float(self._square_len)    # X value within grid of gradient vectors
        grid_y = y / float(self._square_len)    # Y value within grid of gradient vectors
        left_x, right_x, upper_y, lower_y = self._get_corners(grid_x, grid_y)
        x_weight = grid_x - left_x
        y_weight = grid_y - upper_y
        # ul = upper left, lr = lower right, etc.
        ul_influence_val = self._get_influence_val(left_x, upper_y, grid_x, grid_y)
        ur_influence_val = self._get_influence_val(right_x, upper_y, grid_x, grid_y)
        ll_influence_val = self._get_influence_val(left_x, lower_y, grid_x, grid_y)
        lr_influence_val = self._get_influence_val(right_x, lower_y, grid_x, grid_y)
        # Interpolate between top two and bottom two influence vals, then interpolate between them using y_weight
        upper_influence_val = self._interpolate_between(ul_influence_val, ur_influence_val, x_weight)
        lower_influence_val = self._interpolate_between(ll_influence_val, lr_influence_val, x_weight)
        interpolated_val = self._interpolate_between(upper_influence_val, lower_influence_val, y_weight)
        # Normalize interpolated_val to be between 0 and 1, return as height
        # Can range from 0.5 to -0.5, add 0.5 to achieve proper result
        height = interpolated_val + 0.5
        # Some margin of error, ensure is still between 0 and 1
        return round(height) if not 0 <= height <= 1 else height

    def _get_corners(self, x, y):
        """Get coordinates of corners around point in gradients grid.

        Args:
            x (float): X coordinate of point in gradient grid.
            y (float): Y coordinate of point in gradient grid.

        Returns:
            tuple(int, int, int, int): Tuple of left x, right x, upper y and lower y.

        """
        left_x = (int(x)-1) if x == self._width_in_squares else int(x)
        right_x = int(x) if x == self._width_in_squares else (int(x) + 1)
        upper_y = (int(y)-1) if y == self._length_in_squares else int(y)
        lower_y = int(y) if y == self._length_in_squares else (int(y) + 1)
        return left_x, right_x, upper_y, lower_y

    def _get_influence_val(self, vec_x, vec_y, x, y):
        """Get influence value from a corner on grid for a point.

        This value is the dot product of the displacement and gradient vectors at that corner.
        Four of these for all four corners surrounding a point will be interpolated between to get the point's height.

        Args:
            vec_x (int): X coordinate of corner to get gradient and displacement vectors from.
            vec_y (int): Y coordinate of corner to get gradient and displacement vectors from.
            x (float): X coordinate of point to get influence value for, normalized to be within gradients grid.
            y (float): Y coordinate of point to get influence value for, normalized to be within gradients grid.

        Returns:
            float: Influence value of corner (vec_x, vec_y) for point (x, y).

        """
        disp_x = x - vec_x
        disp_y = y - vec_y
        grad_x, grad_y = self._grad_vecs[vec_y][vec_x]
        return grad_x*disp_x + grad_y*disp_y

    def _interpolate_between(self, val0, val1, weight):
        """Interpolate between two values given a weight.

        Will be linear if self._linearly_interpolated is True, or via a smooth function otherwise.

        Args:
            val0 (float): First value to interpolate from.
            val1 (float): Second value to interpolate from.
            weight (float): Weighting of interpolation. Is between 0 and 1; 0 means == val0, 1 means == val1.

        Returns:
            float: Result of interpolation between val0 and val1.

        """
        if self._linearly_interpolated:
            return (1 - weight)*val0 + weight*val1
        else:
            return self._smoothen_weight(1 - weight)*val0 + self._smoothen_weight(weight)*val1

    @staticmethod
    def _smoothen_weight(x):
        return 6*(x**5) - 15*(x**4) + 10*(x**3)
