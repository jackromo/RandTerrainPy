# Todo List

## General

* Tests for TerrainGenerator, DiamondSquareGenerator and Terrain2D/3D

## Future Features

* Noise generation
    * Random Voronoi diagram generation
        * Random seed points for regions, give mean / std.dev
        * Random feature points w/ random or preset heights
            * If random, can decide on an interval, mean and std.dev
    * Erosion algorithms
        * Thermal erosion
        * Hydraulic erosion
* Demo applications
    * Handwritten lines (variance in line from noise function)
    * Cloud generator
    * Island generator
        * Voronoi diagram for all sections of island / sea
        * Different 'biomes' for each 
            * Sea, shore, valley, mountain, etc.
    * Continuous procedural terrain generation (generated on the fly)
        * Use DiamondSquare on square regions, copy over adjacent region's edge to influence next area's generation
