from board import board
from board import PIECE
from board import pair
from agent import agent
import time
import io

class ep_data:

    def __init__(self, move, time):
        self.move = move
        self.time = time

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
        self.winner = ep_winner.get_name()  
        w, b = ep_board.count_piece()
        self.win_piece = b if (ep_winner.get_piece() == PIECE.BLACK) else w
        self.ep_close = tag, self.millisec()  # flag, time usage
        return

    def record_action(self, move):
        if(move.prev == -1 or move.next == -1):
            return False
        usage = self.millisec() - self.ep_time
        record = ep_data(move, usage) # action, reward, time usage
        self.ep_moves += [record]
        return True

        # get ep_moves.move ---> self.moves[0][0].prev self.moves[0][0].next

    def millisec(self):
        return int(round(time.time() * 1000))

    def get_step(self, player = 'x'):
        total_step = len(self.ep_moves)

        if(player == 'p'):
            return (total_step//2 + int(total_step % 2 == 1 ) )

        elif(player == 'e'):
            return total_step //2

        else:
            return total_step

    def get_time(self, player = 'x'):
        player_time = 0
        envir_time = 0

        for i in range(0, len(self.ep_moves), 2):
            player_time += self.ep_moves[i].time

        for i in range(1, len(self.ep_moves), 2):
            envir_time += self.ep_moves[i].time

        if(player == 'p'):
            return player_time

        elif(player == 'e'):
            return envir_time


        return self.ep_close[1] - self.ep_open[1]

    def take_turns(self, player, envir):
        self.ep_time = self.millisec()
        if(envir.get_piece() == PIECE.BLACK):
            return envir if ( (self.get_step() + 1) % 2 ) else player
        else:
            return player if ( (self.get_step() + 1) % 2 ) else envir

    def get_winner(self, player, envir):
        return envir if ( self.take_turns(player, envir) == player ) else player

if __name__ == '__main__':
    ep = episode()
    ep.clear()
    ep.open_episode()
    player = agent(PIECE.BLACK)
    ep.close_episode(player, ep.ep_state)
    print(ep.ep_time)
    print(ep.ep_close)
    a = 0
    a += 1 if(1==0) else 0
    print(a)