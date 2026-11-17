from phased.models import Antenna, Point2D


class Receiver:
    def __init__(self, x: float, y: float):
        self.position = Point2D(x, y)

    def distance_to(self, antenna: Antenna):
        return antenna.position.distance_to(self.position)
