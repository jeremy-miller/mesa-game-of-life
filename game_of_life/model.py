import mesa

from game_of_life.cell import Cell


class GameOfLife(mesa.Model):
    description = "Conway's Game of Life"

    INITIAL_LIVING_RATE = 0.1  # 10%

    # "seed" used by mesa.Model automatically
    def __init__(self, width=50, height=50, seed=42):
        super().__init__()
        self.schedule = mesa.time.SimultaneousActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, torus=True)
        self._initialize_grid()

    def _initialize_grid(self):
        for _content, pos in self.grid.coord_iter():
            cell = Cell(self.next_id(), self, pos)
            if self.random.random() <= self.INITIAL_LIVING_RATE:
                cell.state = Cell.ALIVE
            self.grid.place_agent(cell, pos)
            self.schedule.add(cell)

    def step(self):
        self.schedule.step()
