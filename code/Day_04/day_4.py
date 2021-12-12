import re
from numpy import array, zeros, int32, ones, where
with open("code/Day_4/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()

def parse_boards(lines):
    boards = []
    _next = lines.pop(0)
    while len(lines) > 0:
        if _next == "\n":
            new_board = True
            current_board = []
            while new_board:
                try:
                    _next = lines.pop(0)
                except IndexError:
                    break
                if _next != "\n":
                    current_board.append([int(n) for n in _next.replace("\n", "").strip().split(" ") if re.match("^[0-9]\d*$", n)] )
                else:
                    new_board = False
            boards.append(current_board)

        
    return boards

class BingoBoard:
    def __init__(self, board):
        self.numbers = array(board)
        self.state = zeros(self.numbers.shape, dtype=bool)
        self.win = False

    def play(self, call):
        if not self.win:
            call_match = ones(self.numbers.shape, dtype=int32) * int32(call)
            self.state += ones(self.numbers.shape, dtype=int32) * int32(call) == self.numbers
            self.assert_win()

    def assert_win(self):
        self.win = any([all(self.state[row,:]) for row in range(self.state.shape[0])] + [all(self.state[:,col]) for col in range(self.state.shape[1])])
        #if self.win:
        #    print("I Won")

def part_1():
    calls = [int(n) for n in lines[0].replace("\n", "").split(",")]
    raw_boards = parse_boards(lines[1:])
    bingo_boards = [BingoBoard(b) for b in raw_boards]
    winner = False
    while len(calls) >0:
        call = calls.pop(0)
        [brd.play(call) for brd in bingo_boards]
        states =[brd.win for brd in bingo_boards]
        winner = any(states)
        if winner:
            winner_index = where(states)[0][0]
            winning_board = bingo_boards[winner_index]
            winning_call = call
            rest  = (~winning_board.state).astype(int) * winning_board.numbers
            rest_sum = rest.sum()
            break
    print("The winning call was {} and the sum of the rest numbers is {}".format(winning_call, rest_sum))
    print("The product is {}".format(winning_call * rest_sum))


def part_2():
    calls = [int(n) for n in lines[0].replace("\n", "").split(",")]
    raw_boards = parse_boards(lines[1:])
    bingo_boards = [BingoBoard(b) for b in raw_boards]
    winner = False
    while len(calls) >0:
        call = calls.pop(0)
        [brd.play(call) for brd in bingo_boards]
        states =[int(brd.win) for brd in bingo_boards]
        winners = sum(states)
        num_losers = len(states) - winners
        if num_losers == 1:
            states_bool = array([bool(s) for s in states])
            loser_index = where(~states_bool)[0][0]
            last_board = bingo_boards[loser_index]
        if num_losers == 0:
            winning_call = call
            rest  = (~last_board.state).astype(int) * last_board.numbers
            rest_sum = rest.sum()
            break
    print("The last winning call was {} and the sum of the rest numbers is {}".format(winning_call, rest_sum))
    print("The product is {}".format(winning_call * rest_sum))

if __name__ == "__main__":
    part_1()
    part_2()