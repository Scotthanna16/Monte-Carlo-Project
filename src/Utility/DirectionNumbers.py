import numpy as np

import os


# Load .env file into environment


class DirectionNumbers:
    def __init__(
        self,
        file_path: str = "Monte-Carlo-Project/src/data/direction_number.txt",
        max_bits: int = 30,
    ):
        self.max_bits = max_bits
        self.data = self._load(file_path)
        self.v = self._compute_direction_numbers()

    def _load(self, file_path: str):
        data = []
        with open(file_path, "r") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    parts = line.split()
                    j = int(parts[0])
                    s = int(parts[1])
                    a = int(parts[2])
                    m = [int(x) for x in parts[3:]]
                    data.append((j, s, a, m))
        return data

    def _compute_direction_numbers(self):
        """Compute v[j][k] for all dimensions j and bit positions k."""
        v = {}
        for j, s, a, m in self.data:
            v[j] = np.zeros(self.max_bits + 1, dtype=np.uint32)
            if j == 1:
                for k in range(1, self.max_bits + 1):
                    v[j][k] = 1 << (32 - k)
            else:
                # extract coefficients of a (binary form)
                a_bits = [(a >> i) & 1 for i in range(s - 1, -1, -1)]
                for k in range(1, s + 1):
                    v[j][k] = m[k - 1] << (32 - k)
                for k in range(s + 1, self.max_bits + 1):
                    v[j][k] = v[j][k - s]
                    for l in range(1, s + 1):
                        if a_bits[l - 1]:
                            v[j][k] ^= v[j][k - l] >> l
        return v

    def get_dim(self, j):
        return self.v[j]

    def get_dim_direction(self, j):
        return self.v[j] / 2**32

    def get_bit(self, j, k):
        """Return direction number for dimension j and bit k."""
        return self.v[j][k]

    def get_direction(self, j, k):
        return self.v[j][k] / 2**32
