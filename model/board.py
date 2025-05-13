import numpy as np

class Board():
    def __init__(self,n):
        self.grid = []
        for i in range(n):
            x = np.random.randint(n)
            while (x+1 in self.grid):
                x = np.random.randint(n)
            self.grid.append(x+1)

    def __repr__(self):
        return f"Board(grid={self.grid})"         
