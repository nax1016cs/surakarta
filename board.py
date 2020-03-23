import enum

class piece(enum.IntEnum):
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
	global col, size

	col = 6
	size = 36

	def __init__(self, state = None, step = 0):
		self.state = state[:] if state is not None else [-1] * 36
		for i in range(col):
			for j in range(col):
				if (i <= 1):
					self.state [i*col+j] = piece.BLACK.value;
				if (i <= 3 and i > 1): 
					self.state [i*col+j] = piece.SPACE.value;
				elif (i <= 5 and i > 3):
					self.state [i*col+j] = piece.WHITE.value;
		return

	def __getitem__(self, pos):
		return self.state[pos]
    
	def __setitem__(self, pos, tile):
		self.state[pos] = tile
		return

test = board()
print(test.state)
