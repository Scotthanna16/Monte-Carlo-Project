from DirectionNumbers import DirectionNumbers

# sobol_sequence_generator.py
import numpy as np


class SobolSequenceGenerator:
    def __init__(
        self, DirectionNumbers: DirectionNumbers, dimension: int, n_points: int
    ):
        self.dn = DirectionNumbers
        self.dimension = dimension
        self.n_points = n_points
        self.scale = 1.0 / 2**32  # convert 32-bit int to [0,1)
        self.x = np.zeros(dimension, dtype=np.uint32)  # current XOR state
        self.points = np.zeros((n_points, dimension), dtype=np.float64)

    def _rightmost_zero_bit(self, i: int) -> int:
        """
        Return position (1-indexed) of the rightmost zero bit of (i-1).
        """
        c = 1
        while i & 1:
            i >>= 1
            c += 1
        return c

    def generate(self):
        """
        Generate the Sobol sequence points for the specified dimension and count.
        """
        for i in range(1, self.n_points + 1):
            k = self._rightmost_zero_bit(i - 1)
            for j in range(1, self.dimension + 1):
                self.x[j - 1] ^= self.dn.get_bit(j, k)
                self.points[i - 1, j - 1] = self.x[j - 1] * self.scale
        return self.points


dn = DirectionNumbers()

# Create Sobol generator for 3D, 16 points
sobol = SobolSequenceGenerator(dn, dimension=3, n_points=16)
points = sobol.generate()
print(points)
