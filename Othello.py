from OthelloPosition import OthelloPosition
from AlphaBeta import AlphaBeta
import time
import sys


def Othello(position, time_limit):
    global depth, othello, AlphaBeta         
    othello = OthelloPosition(position)         

    AlphaBeta = AlphaBeta()              
    if position == '':                           
        othello.initialize()

    play = True                                

    while play is True:
        listmv = []                          
        moves = othello.get_moves()               

        for i in moves:
            listmv.append(i.print_move())                
        if len(listmv) == 0:                             
            print("pass")
            play = False

        else:
            if othello.to_move() == 'B':        
           
                if len(listmv) > 1:                         

                    check = True                             
                    choice = AlphaBeta.set_search_depth(7)       

                finalmove = listmv[choice]                           

                print('({},{})'.format(finalmove[0], finalmove[1]))      
              

            else:  
                if len(listmv) > 1:                         

                    check = True                             
                    choice = AlphaBeta.set_search_depth(7)       

                finalmove = listmv[choice]                           

                print('({},{})'.format((finalmove[0], finalmove[1]),0))                                     
                othello.make_move(finalmove)  
                                
 

if __name__ == "__main__":                       
    Othello(sys.argv[1], float(sys.argv[2]) )      