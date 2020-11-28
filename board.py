import time
from luma.core.render import canvas
from luma.led_matrix.device import ws2812

class Board:
    def __init__(self):
        self.device = ws2812(width=8, height=8)
        self.size = 64
        self.pattern = ["#000000"] * self.size

    def set_pattern(self, pattern):
        if len(pattern) != self.size:
            return
        self.pattern = pattern

    def draw(self):
        with canvas(self.device) as grid:
            for index, colour in enumerate(self.pattern):
                x = index % 8
                y = index // 8
                grid.point((x, y), fill=colour)
            time.sleep(0.05)


if __name__ == "__main__":
    board = Board()

    while True:
        try:
            board.draw()
        except KeyboardInterrupt:
            pass