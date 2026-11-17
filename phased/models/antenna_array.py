import numpy as np
from typing import Iterable, Iterator, List

from phased._typing import FloatArray
from phased.models import Antenna, Point2D


class AntennaArray:
    def __init__(self, antennas: Iterable[Antenna] = ()):
        self.antennas: List[Antenna] = list(antennas)

    def add(self, antenna: Antenna) -> None:
        self.antennas.append(antenna)

    def remove(self, antenna: Antenna) -> None:
        self.antennas.remove(antenna)

    def __iter__(self) -> Iterator[Antenna]:
        return iter(self.antennas)

    def __len__(self) -> int:
        return len(self.antennas)

    def electric_field_at(self, point: Point2D) -> float:
        sum = 0.0
        for antenna in self:
            sum += float(antenna.electric_field_at(point))

        return sum

    def electric_field_grid(self, x: FloatArray, y: FloatArray) -> FloatArray:
        point = Point2D(x, y)
        total = np.zeros_like(x, dtype=float)
        for antenna in self:
            total += antenna.electric_field_at(point)
        return total

    def focus_at(self, target: Point2D):
        reference = self.antennas[0]
        reference.initial_phase = 0.0
        reference_phase = reference.phase_at(target)

        for a in self:
            a.initial_phase = 0.0
            travel_phase = a.phase_at(target)
            a.initial_phase = float(reference_phase) - float(travel_phase)
