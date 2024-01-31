import mesa


class Cell(mesa.Agent):
    DEAD = 0
    ALIVE = 1

    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
        self.state = self.DEAD
        self.next_state = self.DEAD

    def step(self):
        live_neighbors = self._get_live_neighbor_count()
        self.next_state = self.state
        if self.is_alive():
            if live_neighbors < 2 or live_neighbors > 3:
                self.next_state = self.DEAD
        else:
            if live_neighbors == 3:
                self.next_state = self.ALIVE

    def _get_live_neighbor_count(self):
        live_neighbors = 0
        for neighbor in self.model.grid.iter_neighbors(self.pos, True):
            if neighbor.is_alive():
                live_neighbors += 1
        return live_neighbors

    def is_alive(self):
        return self.state == self.ALIVE

    def advance(self):
        self.state = self.next_state
