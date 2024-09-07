from const import *
import numpy as np

class Board:

    def __init__(self):
        self.squares = []

    def _create(self):
        self.squares = np.zeros((8,8))
        

    def _add_pieces(self,color):
        pass

