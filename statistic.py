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
        print("#Game\t#Winner\t#left_pieces\t#Moves\t#player_time\t#env_time")
        game_id = 1


        for i in range(len(self.data)):
            print("{}\t{}\t{}\t\t{}\t{}(ms)\t\t{}(ms)" .format(game_id, self.data[i].winner, self.data[i].win_piece, 
                len(self.data[i].ep_moves), self.data[i].get_time('p'), self.data[i].get_time('e') ))
            game_id += 1

        sop, pop, eop = 0, 0, 0
        sdu, pdu, edu = 0, 0, 0
        total = 0
        player_win = 0
        total += blk;



        for i in range(1, blk + 1):
            ep = self.data[-i]

            player_win += 1 if (ep.winner == "player") else 0

            sop += ep.get_step();
            pop += ep.get_step('p');
            eop += ep.get_step('e');
            
            sdu += ep.get_time();
            pdu += ep.get_time('p');
            edu += ep.get_time('e');

        env_win = total - player_win

        print( "In " , self.count , " games:\n")
        print( "player win: " , player_win , " games")
        print( "env win: " , env_win , " games\n")
        print( "player win rate: " , float(player_win) / total * 100.0 , "%")
        print( "env win rate: " , float(env_win) / total * 100.0 , "%")
        print( "ops: " , (sop * 1000.0) / sdu , '(' , (pop * 1000.0) / pdu , " | " , 
        (eop * 1000.0) / edu , ')', "(player_op | env_op)" )


        print( "-------------------------------------\n")
        return

    def is_finished(self):
        return self.count >= self.total

    def back(self):
        return self.data[-1]

    def open_episode(self, tag = ''):
        self.count += 1
        self.data += [episode()]
        self.data[-1].open_episode(tag)
        return

    def close_episode(self, ep_winner, ep_board, tag = ''):
        self.data[-1].close_episode(ep_winner, ep_board, tag)
        if self.count % self.block == 0:
            self.show()
        return

