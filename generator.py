from random import sample


# pattern for a baseline valid solution
def pattern(r, c, base, side):
    return (base * (r % base) + r // base + c) % side


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s):
    return sample(s, len(s))


def gen(base=3):
    side = base * base
    rbase = range(base)
    rows = [g * base + r for g in shuffle(rbase) for r in shuffle(rbase)]
    cols = [g * base + c for g in shuffle(rbase) for c in shuffle(rbase)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    board = [[nums[pattern(r, c, base, side)] for c in cols] for r in rows]

    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0

    numSize = len(str(side))
    return board
