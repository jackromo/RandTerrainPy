# RandTerrainPy

This is a random terrain generator for Python. It's a work in progress, but if you're interested in contributing then email me at sharrackor@gmail.com.

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
    * Voronoi diagram version of terrain (UNFINISHED)
        * Regions defined by closest positions on 2d grid to points
* Terrain generators
    * Diamond square algorithm
        * Takes noise color function (from frequency to amplitude)
        * Red, pink, white, blue, and violet preset noises