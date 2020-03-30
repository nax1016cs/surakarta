from board import board 
from board import PIECE 
from agent import agent 
from episode import episode
from statistic import statistic
import sys

if __name__ == '__main__':
    print('2048 Demo: ' + " ".join(sys.argv))
    print()
    
    total, block, limit = 5, 0, 0
    
    for para in sys.argv[1:]:
        if "--total=" in para:
            total = int(para[(para.index("=") + 1):])
        elif "--block=" in para:
            block = int(para[(para.index("=") + 1):])
        
    
    stat = statistic(total, block)
    player = agent(PIECE.BLACK)
    envir = agent(PIECE.WHITE)

    while not stat.is_finished():
        b = board()
        stat.open_episode("W:B");
        game = stat.back(); 

        while(1):
            who = game.take_turns(player, envir)
            move = who.take_action(b, who.piece)
            if( move.prev != -1 or move.next != -1 ):
                game.record_action(move)
            else:
                winner = game.get_winner(player, envir)
                stat.close_episode( winner, b, "end" )
                break
            b.print_board()
