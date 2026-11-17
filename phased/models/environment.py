import numpy as np
from typing import Tuple

Bound = Tuple[int, int]


class Environment:
    def __init__(self, x: Bound, y: Bound, resolution=500):
        self.x_bounds = x
        self.y_bounds = y
        self.resolution = resolution

    def create_grid(self):
        grid_x = np.linspace(*self.x_bounds, self.resolution)
        grid_y = np.linspace(*self.y_bounds, self.resolution)
        return np.meshgrid(grid_x, grid_y)
