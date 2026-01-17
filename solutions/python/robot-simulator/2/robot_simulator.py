EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'

class Robot:

    LEFT_TURNS = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}
    RIGHT_TURNS = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}

    MOVEMENTS = {NORTH:(0,1), WEST:(-1,0), EAST:(1,0), SOUTH:(0,-1)}

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x = x_pos
        self.y = y_pos
        
    def turn_left(self):
        self.direction = self.LEFT_TURNS[self.direction]
            
    def turn_right(self):
        self.direction = self.RIGHT_TURNS[self.direction]
                
    def advance(self):
        cx,cy = self.MOVEMENTS[self.direction]
        self.x += cx
        self.y += cy

    # CHANGE THIS: execute → move
    def move(self, instructions):
        for movement in instructions:
            if movement == 'L':
                self.turn_left()
            elif movement == 'R':
                self.turn_right()
            elif movement == 'A':
                self.advance()

    @property
    def coordinates(self):
        return (self.x, self.y)