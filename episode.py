from board import board
from board import pair
import time
import io

class episode:
	def __init__(self):
		self.clear()
		return

	def clear(self):
		self.ep_state = self.initial_state()
		self.winner = "N/A"
		self.win_piece = -1
		self.ep_time = 0
		self.ep_moves = []
		self.ep_open = "N/A", 0 # flag, time usage
		self.ep_close = "N/A", 0 # flag, time usage
		return

	def initial_state(self):
		return board()

	def state(self):
		return self.ep_state

	def open_episode(self, tag = ''):
		self.ep_open = tag, self.millisec()  # flag, time usage
		return

	def close_episode(self, ep_winner, ep_board, tag = ''):
    	#### not yet written
    	# self.winner = ep_winner.name()  
    	# self.win_piece = b.count_piece(ep_winner.get_piece())
		self.ep_close = tag, self.millisec()  # flag, time usage
		return
	def record_action(self, move):
		if(move.prev == -1 or move.next == -1):
			return False
		usage = self.millisec() - self.ep_time
		record = move, usage # action, reward, time usage
		self.ep_moves += [record]
		return True

	def millisec(self):
		return int(round(time.time() * 1000))

ep = episode()
ep.clear()
print(ep.record_action( pair(0,6)))
