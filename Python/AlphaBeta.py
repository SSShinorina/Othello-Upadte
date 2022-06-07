from OthelloAlgorithm import OthelloAlgorithm
from CountingEvaluator import CountingEvaluator
from OthelloAction import OthelloAction


class AlphaBeta(OthelloAlgorithm):
    DefaultDepth=7
    # """
    # This is where you implement the alpha-beta algorithm. 
	# See OthelloAlgorithm for details
	
    # Author:
    # """ 
    def __init__(self, othello_evaluator=CountingEvaluator(), depth=DefaultDepth):
        self.evaluator = othello_evaluator 
        self.search_depth = depth 
        self.purned = 0

    def set_evaluator(self, othello_evaluator, ):
        self.evaluator = othello_evaluator # change to your own evaluator

    def set_search_depth(self, depth):
        self.search_depth = depth # use iterative deepening search to decide depth

    def evaluate(self, branch, depth, alpha, beta):
        i = 0

        for child in branch:
            if type(child) is list:
                (nalpha, nbeta) = self.evaluate(child, depth + 1, alpha, beta)
                if depth % 2 == 1:
                    beta = nalpha if nalpha < beta else beta
                else:
                    alpha = nbeta if nbeta > alpha else alpha

                branch[i] = alpha if depth % 2 == 0 else beta
                i += 1

            else:

                if depth % 2 == 0 and alpha < child:
                    alpha = child

                if depth % 2 == 1 and beta > child:
                    beta = child

                if alpha > beta:
                    self.pruned += 1
                    break

        return (alpha, beta)
        