import numpy as np

sample = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 """

# Parse the input into drawn numbers and board arrays
def parse_input(input):
    
    # Separate boards from numbers drawn
    boards = input.split('\n')[2:]
    nums = [int(a) for a in input.split("\n")[0].split(',')]
    
    nboards = int(len(boards)/6)
    print(f"Parsing {nboards} bingo boards")

    # Get 5 lines every 6 lines (skips blank line between boards)
    boards = [boards[i:i+5] for i in range(0, len(boards), 6)]
    boardarr = []

    # Construct boards as lists of ints
    for board in boards:
        b = []
        for line in board:
            # Remove empty character caused by single-digit numbers
            b.append([int(a) for a in line.split(' ') if a != ''])
        boardarr.append(np.asarray(b))

    return nums, boardarr    


# Check if board is a winner
def check_board(board, n):
    for row in board:
        if not False in row.mask:
            # print(board)
            return np.sum(board) * n

    for row in board.T:
        if  not False in row.mask:
            # print(board)
            return np.sum(board) * n
    
    return None


# Loop through all the drawn numbers against all boards
def play_bingo(input, find_last=False):
    nums, boards = parse_input(input)

    for i,n in enumerate(nums):

        newboards = []
        for board in boards:
            b = np.ma.masked_equal(board, n)

            # If this is not the first round, and there's been at 
            # least one number masked from board, check for win
            if i>0 and np.ma.is_masked(b):
                
                # Check board for win
                ans = check_board(b, n)

                # If winning board, don't add to newboards
                if ans is not None:
                    # print(f"Bingo!! Answer: {ans}")
                    
                    if find_last:
                        last_win = ans
                    else:
                        return ans
                else:
                    newboards.append(b)
            else:
                newboards.append(b)

        boards = newboards
    if find_last:
        return last_win


assert play_bingo(sample) == 4512
assert play_bingo(sample, find_last=True) == 1924

with open('./input04.txt') as inf:
    input = inf.read()
    print("Part 1: ", play_bingo(input))
    print("Part 2: ", play_bingo(input, find_last=True))
