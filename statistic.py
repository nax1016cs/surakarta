from board import board
from episode import episode
from agent import agent


class statistic:
	""" container & statistic of episodes """
	
	def __init__(self, total, block = 0):
		"""
		the total episodes to run
		the block size of statistic
		the limit of saving records
		
		note that total >= limit >= block
		"""
		self.total = total
		self.block = block if block else total
		self.data = []
		self.count = 0
		return

	def show(self, tstat = True):
		
		blk = self.block
		print("#Game     #Winner     #left_pieces     #Moves     #player_time     #env_time")
		game_id = 1


		for i in range(len(data)):
			print("\t {} \t {} \t {} \t {} \t {} (ms) \t {} (ms) " .format(game_id, data[i].winner, data[i].win_piece, 
				len(data[i].ep_moves, data[i].time('p'), data[i].time('e') )))
			game_id += 1

		sop, pop, eop = 0, 0, 0
		sdu, pdu, edu = 0, 0, 0
		total = 0
		player_win = 0
		total += blk;



		for i in range(1, blk + 1):
			ep = self.data[-i]

			player_win += 1 if (ep.winer == "player") else 0

			sop += ep.get_step();
			pop += ep.get_step('p');
			eop += ep.get_step('e');
			
			sdu += ep.get_time();
			pdu += ep.get_time('p');
			edu += ep.get_time('e');

		env_win = total - player_win

		print( "In " , count , " games:\n")
		print( "player win: " , player_win , " games";)
 		print( "env win: " , env_win , " games\n";)
		print( "player win rate: " , double(player_win) / total * 100.0 , "%";)
		print( "env win rate: " , double(env_win) / total * 100.0 , "%")
		print( "ops: " , (sop * 1000.0) / sdu , '(' , (pop * 1000.0) / pdu , " | " , 
		(eop * 1000.0) / edu , ')', "(player_op | env_op)" )


		print( "-------------------------------------\n")
		return

	def is_finished(self):
		return count >= total

	def back(self):
		return self.data[-1]

	def open_episode(self, tag = ''):
		count += 1
		self.data += [episode()]
		self.data[-1].open_episode(flag)
		return

	def close_episode(self, ep_winner, ep_board, tag = ''):
		self.data[-1].close_episode(ep_winner, ep_board, tag)
		if self.count % self.block == 0:
			self.show()
		return

