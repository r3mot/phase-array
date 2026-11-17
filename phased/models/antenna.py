import numpy as np

from phased._typing import FloatOrArray
from phased.models.point import Point2D


class Antenna:
    """Models a single radio transmitter.

    Given any spot on the map, it calculates how far the wave
    traveled and whether the wave is pushing up or pulling down
    at that exact moment
    """

    def __init__(self, x: float, y: float, frequency: float, phase: float = 0.0):
        self.position = Point2D(x, y)
        self.frequency = frequency
        self.initial_phase = phase
        self.wavelength = 3e8 / self.frequency
        self.wavenumber = (2 * np.pi) / self.wavelength

    def phase_at(self, point: Point2D) -> FloatOrArray:
        distance = self.position.distance_to(point)
        return self.wavenumber * distance + self.initial_phase

    def electric_field_at(self, point: Point2D) -> FloatOrArray:
        return np.cos(self.phase_at(point))

    def set_position(
        self, x: FloatOrArray | None = None, y: FloatOrArray | None = None
    ) -> None:
        self.position.update(x, y)
