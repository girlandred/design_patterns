from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Board:
    def __init__(self):
        x = ["A", "B", "C", "D", "E", "F", "G", "H"]
        y = [1, 2, 3, 4, 5, 6, 7, 8]
        squares = []


class Piece(ABC):
    def __init__(self, color, position, number_of_moves, move_rule: MoveRule):
        self.color = color
        self.x = position[0]
        self.y = position[1]
        self.position = position
        self.number_of_moves = number_of_moves
        self.move_rule = move_rule

    @abstractmethod
    def move(self, board, currentSquare, x, y, new_position: List):
        for square in board.squares:
            if square.position == [chr(ord(currentSquare.x) + x), currentSquare.y + y] and square.empty():
                new_position.append(square.position)

    def check_position_range(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Knight(Piece):
    def print_info(self):
        pass

    def __init__(self, color, x, y, number_of_moves, move_rule: MoveRule):
        super().__init__(color, x, y, number_of_moves)

    def move(self, new_position: List, **kwargs):
        pass


class Rook(Piece):
    def __init__(self, color, x, y, number_of_moves, move_rule: MoveRule):
        super().__init__(color, x, y, number_of_moves)

    def move(self, new_position: List, **kwargs):
        pass


class MoveRule(ABC):
    def __init__(self):
        pass

    def get_all_moves(self):
        pass


class KnightMove(MoveRule):
    def __init__(self):
        super().__init__()

    def get_all_moves(self):
        pass


class RookMove(MoveRule):
    def __init__(self):
        super().__init__()

    def get_all_moves(self):
        pass
