# RandTerrainPy

This is a random terrain generator for Python. 

(If you're interested in contributing, then email me at sharrackor@gmail.com.)

## License

This project is licensed under the [MIT license (MIT)](LICENSE).

## Requirements

This software requires matplotlib (>=1.5), and numpy (>=1.6).

## Installation

This program can be installed by downloading the software and entering

```bash
python setup.py
```

within the main directory.

## Features

* 3d Terrain class
    * Grid of heights between 0 and 1
    * Addition and subtraction of Terrains, multiplication with scalar
    * Basic string representation
    * 2d and 3d graphical representations
        * Uses matplotlib for 3d, top-down greyscale for 2d
    * Saving and loading terrains (uses .terr format)
    * Voronoi diagram version of terrain
        * Regions defined by closest positions on 2d grid to points
        * Input set of points to make regions around
        * Can alter heights of all points in a region
        * Uniform randomly generated center points
        * Lloyd relaxation
        * Linear interpolation of heights of points to feature points within participant regions, predefined coefficients
            * Height of point += sum(coefficients[i]*distances_to_closest_feature_points[i] for i in range(len(coefficients)))
            * Can choose to add on heights from feature points or not
    * Terrain erosion
        * Thermal erosion
* Terrain generators
    * Diamond square algorithm
        * Takes noise color function (from frequency to amplitude)
        * Red, pink, white, blue, and violet preset noises
    * Perlin noise
        * Choice of grid size and size of grid squares
        * Choice of linear or cubic smoothing
    * Random Voronoi diagram (see above)