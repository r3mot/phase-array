from __future__ import annotations
from dataclasses import dataclass
import numpy as np

from phased._typing import FloatOrArray


@dataclass(eq=False)
class Point2D:
    x: FloatOrArray
    y: FloatOrArray

    def update(
        self, x: FloatOrArray | None = None, y: FloatOrArray | None = None
    ) -> None:
        if x is not None:
            self.x = x

        if y is not None:
            self.y = y

    def distance_to(self, other: Point2D) -> FloatOrArray:
        dx = self.x - other.x
        dy = self.y - other.y
        return np.hypot(dx, dy)
