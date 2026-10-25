class Distance:

    def __init__(self, distance: int | float) -> None:
        self.km = distance

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object | int) -> Distance:
        if isinstance(other, Distance):
            other = other.km
        return Distance(self.km + other)

    def __iadd__(self, other: object | int) -> Distance:
        if isinstance(other, Distance):
            other = other.km
        self.km += other
        return self

    def __mul__(self, other: int) -> Distance | None:
        if not isinstance(other, Distance):
            return Distance(self.km * other)
        return None

    def __truediv__(self, other: int) -> Distance | None:
        if not isinstance(other, Distance):
            return Distance(round((self.km / other), 2))
        return None

    def __lt__(self, other: object | int) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km < other

    def __gt__(self, other: object | int) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km > other

    def __eq__(self, other: object | int) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km == other

    def __le__(self, other: object | int) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km <= other

    def __ge__(self, other: object | int) -> bool:
        if isinstance(other, Distance):
            other = other.km
        return self.km >= other
