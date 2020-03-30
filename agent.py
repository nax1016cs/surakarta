from board import board
from board import PIECE
from board import pair


class agent:

	def __init__(self, piece):
		self.piece = piece
		self.step_count = 0
		self.count_not_eat = 0
		return

	def __eq__(self, other):
		return self.piece == other.piece

	def open_episode(self, tag = ''):
		return

	def close_episode(self, tag = ''):
		return

	def take_action(self, board):
		return

	def get_name(self):
		return "agent"

	def get_piece(self):
		return self.piece

	def idle_step(self):
		return count_not_eat

	def print_pos(self, move):
		print("piece: ", self.piece)
		# print("from: ", move.prev//6, " ", move.prev % 6 , "to: ", move.next//6, " ", move.next % 6)
		print("from : {} {} to: {} {}" .format(move.prev//6, move.prev % 6, move.next//6, move.next % 6))

	def count_piece(self, board):
		count = 0
		for i in range(36):
			if( board.state[i] == (self.get_piece() ^ 1) ):
				count += 1 
		return count

test = agent(PIECE.BLACK)
test.print_pos(pair(6, 8))