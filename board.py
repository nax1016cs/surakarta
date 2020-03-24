import enum


global col, size, pos 

col = 6
size = 36
pos = 15

class PIECE(enum.IntEnum):
	BLACK = 7
	WHITE = 8
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

class action(enum.IntEnum):
	move = 0
	eat = 1

class pair:

	def __init__(self, prev_ = -1 , next_ = -1):
		self.prev = prev_
		self.next = next_

	def __eq__(self, other):
		return self.prev == other.prev and self.next == other.next

	def __ne__(self, other):
		return not ( __eq__(self, other) )

class board:
	# state equals every point on the board
	# step == 0 means white's turn to play, otherwise


	def __init__(self, state = None, step = 0):
		self.step = step
		self.state = state[:] if state is not None else [-1] * 36
		for i in range(col):
			for j in range(col):
				if ( i <= 1):
					self.state [i*col+j] = PIECE.BLACK.value;
				if ( i <= 3 and i > 1): 
					self.state [i*col+j] = PIECE.SPACE.value;
				elif ( i <= 5 and i > 3):
					self.state [i*col+j] = PIECE.WHITE.value;
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
		global pos
		pos =  {
			DIRECTION.LEFT: 	 position - 1,
			DIRECTION.RIGHT: 	 position + 1,
			DIRECTION.UP: 	 	 position - col,
			DIRECTION.DOWN: 	 position + col
		}[direction]
		return

test = board()
print('test.state : ', test.state)
print('test.test.compare_PIECE() : ', test.compare_piece())
print('test.test.take_turn() : ', test.take_turn())
test.move_single_step( pos,DIRECTION.RIGHT)
test.move_single_step( pos,DIRECTION.UP)
test.move_single_step( pos,DIRECTION.LEFT)
print('move_right: ' , pos)
# print('test.test.count_PIECE(PIECE.WHITE_WIN.value) : ', test.count_piece(PIECE.WHITE.value))
