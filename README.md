# MazeViz
## Overview
MazeViz is a python package meant to visualize maze generation and solving using pygame.
First, the program will construct a maze using Kruskal's minimum spanning tree algorithm.


<img width="612" alt="Screen Shot 2023-10-20 at 6 28 40 PM" src="https://github.com/Thomas-Edwards/MazeViz/assets/45698475/4ff8dc4d-14c0-4caa-ab35-cf55d4c4e9ad">

Then after placing down starting and ending points, the program will either peform depth-first search,
breadth-first search, or A* to get from the start to the end. Below, we run A* on a 100x100 grid.

<img width="700" alt="Screen Shot 2023-10-19 at 11 25 21 PM" src="https://github.com/Thomas-Edwards/MazeViz/assets/45698475/71b437b0-b553-4afe-9140-a6db32fdaf97">

## Running The Software
Start by downloading the wheel file in the dist/ folder of the repo.
You can then install the package by running

`pip install <wheel_file>`

You can then run MazeViz directly by running

`python3 -m MazeViz`

Note that you can only change the number of rows/columns in the maze by editing the source code directly.
