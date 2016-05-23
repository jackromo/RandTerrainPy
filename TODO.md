# Todo List

## General

* Tests for TerrainGenerator, DiamondSquareGenerator and Terrain2D/3D
* Optimize all methods to use GPU parallelism when iterating over all points

## Future Features

* Demo applications
    * Handwritten lines (variance in line from noise function)
    * Cloud generator
    * Island generator
        * Voronoi diagram for all sections of island / sea
        * Different 'biomes' for each 
            * Sea, shore, valley, mountain, etc.
    * Continuous procedural terrain generation (generated on the fly)
        * Use DiamondSquare on square regions, copy over adjacent region's edge to influence next area's generation
        * Land, trees, water, clouds
        * Biomes
    * Bubble textures
