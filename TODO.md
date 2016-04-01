# Todo List

## General

* Tests for TerrainGenerator and DiamondSquareGenerator
* Exception for Terrain setter value out of range (0, 1)

## Future Features

* Terrain class for random height map
    * Saving and loading terrains
    * Voronoi diagrams (subclass of Terrain)
        * Input set of points to make regions around
            * Lloyd relaxation
        * Can alter heights of all points in a region
        * Can alter height of center point and corner points
            * Linear interpolation of heights of points to corner / center, within participant regions
* Noise generation
    * Perlin noise
    * Random Voronoi diagram generator
        * Random seed points for regions, give mean / std.dev
        * Random feature points w/ random or preset heights
            * If random, can decide on an interval, mean and std.dev
* Demo applications
    * Handwritten lines (variance in line from noise function)
    * Cloud generator
    * Island generator
        * Voronoi diagram for all sections of island / sea
        * Different 'biomes' for each 
            * Sea, shore, valley, mountain, etc.
    * Continuous procedural terrain generation (generated on the fly)
