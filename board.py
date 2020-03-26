import enum


global col, size, pos 

col = 6
size = 36
pos = 10

class PIECE(enum.IntEnum):
    BLACK = 0
    WHITE = 1
    SPACE = 9
    UNKNOW = -1

class WIN_STATE(enum.IntEnum):
    BLACK_WIN = 0
    WHITE_WIN = 1
    DRAW = 2

class EXEC_STATE(enum.IntEnum):
    SUCCESS = 1
    FAIL = -1

class DIRECTION(enum.IntEnum):
    LEFT = -1
    RIGHT = 1
    UP = -2
    DOWN = 2

class ACTION(enum.IntEnum):
    MOVE = 0
    EAT = 1

class pair:

    def __init__(self, prev_ = -1 , next_ = -1):
        self.prev = prev_
        self.next = next_

    def __eq__(self, other):
        return self.prev == other.prev and self.next == other.next

    def __ne__(self, other):
        return not ( __eq__(self, other) )


direction_map = {
     1 :  [ 6, DIRECTION.RIGHT],  2 : [12, DIRECTION.RIGHT], 3 : [17, DIRECTION.LEFT ], 4 : [11, DIRECTION.LEFT ],
     6 :  [ 1, DIRECTION.DOWN ], 12 : [ 2, DIRECTION.DOWN ], 18 : [32, DIRECTION.UP   ], 24 : [31, DIRECTION.UP   ],
    31 :  [24, DIRECTION.RIGHT], 32 : [18, DIRECTION.RIGHT], 33 : [23, DIRECTION.LEFT ], 34 : [29, DIRECTION.LEFT ],
    29 :  [34, DIRECTION.UP   ], 23 : [33, DIRECTION.UP   ], 17 : [3, DIRECTION.DOWN ], 11 : [ 4, DIRECTION.DOWN ]
}

corner_pos = [0, 5, 30, 35]


class board:
    # state equals every point on the board
    # step == 0 means white's turn to play, otherwise


    def __init__(self, state = None, step = 0):
        self.step = step
        self.state = state[:] if state is not None else [-1] * 36

        ### to be deleted
        for i in range(size):
            self.state[i] = PIECE.SPACE.value
        # self.state[10] = PIECE.BLACK.value
        # self.state[1] = PIECE.WHITE.value
        # self.state[29] = PIECE.WHITE.value
        # self.state[4] = PIECE.WHITE.value
        # self.state[24] = PIECE.WHITE.value
        # self.state[15] = PIECE.WHITE.value
        self.state[16] = PIECE.BLACK.value
        # self.state[17] = PIECE.WHITE.value



        # for i in range(col):
        #     for j in range(col):
        #         if ( i <= 1):
        #             self.state [i*col+j] = PIECE.BLACK.value
        #         if ( i <= 3 and i > 1): 
        #             self.state [i*col+j] = PIECE.SPACE.value
        #         elif ( i <= 5 and i > 3):
        #             self.state [i*col+j] = PIECE.WHITE.value
        return

    def __getitem__(self, pos):
        return self.state[pos]
    
    def __setitem__(self, pos, tile):
        self.state[pos] = tile
        return

    def compare_piece(self):
        w , b = self.count_piece()
        if (w == b ):
            return WIN_STATE.DRAW
        return WIN_STATE.BLACK_WIN if w > b else WIN_STATE.WHITE_WIN

    def take_turn(self):
        return PIECE.WHITE if self.step % 2 else PIECE.BLACK

    def count_piece(self):
        w = 0
        b = 0
        for i in range(size):
            if ( self.state[i] == PIECE.BLACK ):
                b += 1
            elif( self.state[i] == PIECE.WHITE ):
                w += 1
        return w , b
        
    def move_single_step(self, position, direction):
        # global pos
        if( direction == DIRECTION.LEFT ):
            return -1 if  position % 6 == 0 else (position - 1)

        elif( direction == DIRECTION.RIGHT ):
            return -1 if  position % 6 == 5 else (position + 1)

        elif( direction == DIRECTION.UP ):
            return -1 if  position >= 0 and position <= 5 else (position - col)

        elif( direction == DIRECTION.DOWN ):
            return -1 if  position >= 30 and position <= 35 else (position + col)    

        else :
            return -1    
    #     pos = {
    #         DIRECTION.LEFT:      position - 1,
    #         DIRECTION.RIGHT:      position + 1,
    #         DIRECTION.UP:           position - col,
    #         DIRECTION.DOWN:      position + col
    #     }[direction]

    # find piece to eat, this piece is going to eat another piece
    def eat(self, piece, position, direction, step_count, pass_ring):
        temp_pos = position

        while(temp_pos != -1):

            step_count += 1
            temp_pos = self.move_single_step(position, direction)
            position = temp_pos if temp_pos != -1 else position 
            # print('while pos: ', position, temp_pos)

            # step_count >= 24 
            if( step_count >= 25 or (self.state[position] == piece and temp_pos != -1) ):
                # print('step_count : ',self.state[position], piece.value )
                return EXEC_STATE.FAIL, -1

            if( self.state[position] !=  (piece) and self.state[position] != PIECE.SPACE and self.state[position] != PIECE.UNKNOW):

                if(pass_ring):
                    return EXEC_STATE.SUCCESS, position

                else:
                    step_count = 0 # may be removed
                    return EXEC_STATE.FAIL, -1
        try:
            new_pos = direction_map[position][0]
            new_dir = direction_map[position][1]
            # print('try pos: ', new_pos)
            if( self.state[new_pos] !=  (piece) and self.state[new_pos] != PIECE.SPACE and self.state[new_pos] != PIECE.UNKNOW):
                return EXEC_STATE.SUCCESS, new_pos
            else:
                return self.eat(piece, new_pos, new_dir, step_count, True)

        except KeyError:
            # print('error')
            step_count = 0
            return EXEC_STATE.FAIL, -1

    # eatable record the starting position to eat other piece
    def check_eat(self, position, piece):
        temp_pos = position
        step_count = 0
        eatable = []
        for p in corner_pos:
            if p == position: 
                return []

        self.state[position] = PIECE.SPACE

        for direction in DIRECTION:
            state, new_pos = self.eat(piece, position, direction, step_count, False )
            if( state != EXEC_STATE.FAIL):
                eatable.append(new_pos)
                print('check_eat pos: ', new_pos, ' step_count: ', step_count, 'dir: ', direction)
                step_count = 0

        self.state[position] = piece

        return eatable

    # movable record where the piece can go
    def check_move(self, position, piece):
        dirs = [-7, -6, -5, -1, 1, 5, 6, 7]
        no_move = 0
        moveable = []

        if( position % 6 == 0):
            dirs[0] = dirs[3] = dirs[5] = no_move

        if( position >= 0 and position <= 5):
            dirs[0] = dirs[1] = dirs[2] = no_move

        if( (position + 1) % 6 == 0):
            dirs[2] = dirs[4] = dirs[7] = no_move

        if (position >= 30 and position <= 35):
            dirs[5] = dirs[6] = dirs[7] = no_move

        for dir_pos in dirs:
            if( dir_pos == 0 ):
                continue
            if( self.state[position + dir_pos] == PIECE.SPACE):
                moveable.append( position + dir_pos )

        return moveable

    def find_next_move(self, piece):
        next_move = []
        for position in range(size):
            if(self.state[position] == piece):
                eat_list = self.check_eat(position, piece)
                move_list = self.check_move(position, piece)
                for new_pos in eat_list:
                    next_move.append( pair(position,new_pos ) )
                for new_pos in move_list:
                    next_move.append( pair(position,new_pos ) )
        return next_move

        #     if( len(move) != 0 ): 
        #         for new_pos in move:
        #             next_move.append( pair(position,new_pos) )
        # return next_move
    def check_remaining_piece(self, piece):
        for position in range(size):
            if( self.state[position] == piece ):
                return EXEC_STATE.SUCCESS
        return EXEC_STATE.FAIL 

    def move(prev_pos, next_pos, piece):
        global step 

        if( next_pos > size or next_pos < 0):
            return EXEC_STATE.FAIL
        self.state[next_pos] = piece
        self.state[prev_pos] = PIECE.SPACE
        step += 1
        return EXEC_STATE.SUCCESS


test = board()
print('test.state : ', test.state)
print('test.test.compare_PIECE() : ', test.compare_piece())
print('test.test.take_turn() : ', test.take_turn())

# pos = test.move_single_step( pos,DIRECTION.RIGHT)
# print(pos)
# print(test.eat(PIECE.BLACK, pos, DIRECTION.RIGHT, 0, False))
# pos = test.move_single_step( pos,DIRECTION.UP)
# search_move(pos, DIRECTION.RIGHT, 0, False)

print(test.check_eat(pos, test.state[pos]))
print(test.check_move(pos,  test.state[pos]))

# temp = test.find_next_move(PIECE.BLACK)
# for i in range(len(temp)):
#     print('first: ', temp[i].prev, 'second: ', temp[i].next)
print(test.check_remaining_piece(PIECE.WHITE))