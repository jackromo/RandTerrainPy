"""All random generators for Terrain class."""

from terrain import Terrain
import random
import abc


class TerrainGenerator(object):
    """Abstract noise generator that makes a Terrain with heights produced from noise."""

    __metaclass__ = abc.ABCMeta

    def __init__(self, seed=None):
        """
        Args:
            seed (int): Seed of noise generator for random elements.

        """
        self.seed = seed if seed is not None else random.randint(100)

    @abc.abstractmethod
    def __call__(self, width, length):
        """Generate a Terrain with heights corresponding to noise.

        Args:
            width (int): Width of Terrain to generate.
            length (int): Length of Terrain to generate.

        Returns:
            Terrain: New Terrain with heights corresponding to noise.

        """
