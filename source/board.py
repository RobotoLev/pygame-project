class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[random.randint(1, 2) for _ in range(height)] for _ in range(width)]

        self.left = 10
        self.top = 10
        self.cell_size = 30

        self.cross_now = True

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                  self.cell_size, self.cell_size), 1)
                if self.board[x][y] == 1:
                    pygame.draw.circle(screen, pygame.Color("red"),
                                       (self.left + x * self.cell_size + self.cell_size // 2,
                                        self.top + y * self.cell_size + self.cell_size // 2),
                                       self.cell_size // 2 - 3)
                elif self.board[x][y] == 2:
                    pygame.draw.circle(screen, pygame.Color("blue"),
                                       (self.left + x * self.cell_size + self.cell_size // 2,
                                        self.top + y * self.cell_size + self.cell_size // 2),
                                       self.cell_size // 2 - 3)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size

        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y

    def on_click(self, cell_coords):
        x, y = cell_coords

        now = self.board[x][y]
        for i in range(self.width):
            self.board[i][y] = now
        for i in range(self.height):
            self.board[x][i] = now

        self.render()

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is None:
            return
        self.on_click(cell)
        self.render()