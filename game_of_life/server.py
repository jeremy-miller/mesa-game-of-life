import mesa

from game_of_life.model import GameOfLife

GRID_WIDTH = 50
GRID_HEIGHT = 50
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500


def portrayal(cell):
    return {
        "x": cell.pos[0],
        "y": cell.pos[1],
        "Shape": "rect",
        "w": 1,
        "h": 1,
        "Color": "black" if cell.is_alive() else "white",
        "Filled": True,
        "Layer": 0,
    }


canvas = mesa.visualization.CanvasGrid(
    portrayal, GRID_WIDTH, GRID_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT
)

model_params = {"width": GRID_WIDTH, "height": GRID_HEIGHT}

server = mesa.visualization.ModularServer(
    GameOfLife, [canvas], "Game of Life", model_params
)
