"""Container for all exceptions."""


class Error(Exception):
    """Base error for all custom errors."""
    pass


class InvalidDimensionsError(Error):
    """Exception raised when two Terrains of differing dimensions are combined."""
    pass


class HeightOutOfBoundsError(Error):
    """Error raised when height value passed to Terrain not within 0 and 1."""
    pass
