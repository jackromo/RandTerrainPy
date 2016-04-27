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


class OutOfRegionError(Error):
    """Error raised when stating a point outside a VoronoiTerrain's region is within said region."""
    pass


class InvalidCoefficientCountError(Error):
    """Error raised when giving an invalid number of coefficients to add_feature_point_factors()."""
    pass


class InvalidFileFormatError(Error):
    """Error raised when .terr file is not of valid format."""
    pass
