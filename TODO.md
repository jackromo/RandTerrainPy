# Todo List

## General

* Tests for TerrainGenerator, DiamondSquareGenerator and Terrain2D/3D

## Future Features

* Terrain class for random height map
    * Saving and loading terrains
    * Voronoi diagrams (subclass of Terrain)
        * Linear interpolation of heights of points to feature points within participant regions, predefined coefficients
            * Height of point += sum(coefficients[i]*distances_to_closest_feature_points[i] for i in range(len(coefficients)))
            * Can choose to add on heights from feature points or not
* Noise generation
    * Perlin noise
    * Random Voronoi diagram generation
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
        * Use DiamondSquare on square regions, copy over adjacent region's edge to influence next area's generation
