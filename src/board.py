from const import *
from square import Square
from piece import *
from move import Move

class Board:

    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def calc_moves(self,piece,row,col):
        '''
        Calculate all the possible (valid) moves of a specific piece on a specific position
        '''
        def pawn_moves():
            steps = 1 if piece.moved else 2

            # vertical moves
            start = row + piece.dir
            end = row + (piece.dir*(1+steps))
            for move_row in range(start,end,piece.dir):
                if Square.in_range(move_row):
                    if self.squares[move_row][col].isempty():
                        # create initial and final move squares
                        initial = Square(row,col)
                        final = Square(move_row,col)
                        #create new move
                        move = Move(initial,final)
                        piece.add_move(move)
                    # blocked
                    else: break
                # not in range
                else: break

            # diagonal moves
            move_rows = row + piece.dir
            move_cols = [col-1,col+1]
            for move_col in move_cols:
                if Square.in_range(move_rows,move_col):
                    if self.squares[move_rows][move_col].has_rival_piece(piece.color):
                        # create initial and final move squares
                        initial = Square(row,col)
                        final = Square(move_row,move_col)
                        # create a new move
                        move = Move(initial,final)



        def knight_moves():
            # 8 possible moves
            possible_moves = [
                (row+2,col+1),(row+2,col-1),
                (row-2,col+1),(row-2,col-1),
                (row+1,col+2),(row+1,col-2),
                (row-1,col+2),(row-1,col-2)
            ]

            for possible_move in possible_moves:
                possible_move_row,possible_move_col = possible_move
                if Square.in_range(possible_move_row,possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create squares of the new move
                        initial = Square(row,col)
                        final = Square(possible_move_row,possible_move_col)  # piece = piece
                        # create new move
                        move = Move(initial,final)
                        # append new valid move
                        piece.add_move(move)

        if isinstance(piece,Pawn): pawn_moves()

        elif isinstance(piece,Knight): knight_moves()
        elif isinstance(piece,Bishop): pass
        elif isinstance(piece,Rook): pass
        elif isinstance(piece,Queen): pass
        elif isinstance(piece,King): pass

    def _create(self):

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row,col)
        

    def _add_pieces(self,color):
        row_pawn, row_other = (6,7) if color == 'white' else (1,0)

        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn,col,Pawn(color))

        # Knights
        self.squares[row_other][1] = Square(row_other,1,Knight(color))
        self.squares[row_other][6] = Square(row_other,6,Knight(color))

        # Bishops
        self.squares[row_other][2] = Square(row_other,2,Bishop(color))
        self.squares[row_other][5] = Square(row_other,5,Bishop(color))

        # Rooks
        self.squares[row_other][0] = Square(row_other,0,Rook(color))
        self.squares[row_other][7] = Square(row_other,7,Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_other,3,Queen(color))

        # King
        self.squares[row_other][4] = Square(row_other,4,King(color))