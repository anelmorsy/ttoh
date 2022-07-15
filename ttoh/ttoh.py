"""Main module."""

DEBUG = False
NUM_ROWS = 6
NUM_COLS = 3
NUM_DISK = 5

towers = [['|', '|', '|'],
          ['1', '|', '|'],
          ['2', '|', '|'],
          ['3', '|', '|'],
          ['4', '|', '|'],
          ['5', '|', '|']
]

trans_index = [NUM_ROWS - NUM_DISK, NUM_ROWS - 1, NUM_ROWS - 1]

from_index = [NUM_ROWS - NUM_DISK, None, None]
to_index = [None, NUM_ROWS - 1 , NUM_ROWS - 1]

def print_towers():
    for row in towers:
        for cell in row:
            print(cell, end=' ')
        print()

def valid_tower_transition(a, b):
    return from_index[a] is not None and to_index[b] is not None

def valid_disk_transisiton(a, b):
    return from_index[b] is None or towers[from_index[a]][a] < towers[from_index[b]][b]

def move(a, b):
    if DEBUG:
        print(f"tower: {a} -> {b}, index: {from_index[a]} -> {to_index[b]}")

    if not valid_tower_transition(a, b):
        print("tower:fuck you motherfuckker")
        exit(1)
    
    if not valid_disk_transisiton(a, b):
        print("dsik:fuck you motherfucckkkekr")
        exit(1)

    towers[from_index[a]][a], towers[to_index[b]][b] = towers[to_index[b]][b], towers[from_index[a]][a]

    from_index[a] += 1
    to_index[b] -=1

    if to_index[a] is None:
        to_index[a] = NUM_ROWS - NUM_DISK
    else:
        to_index[a] += 1

    if from_index[b] is None:
        from_index[b] = NUM_ROWS - 1
    else:
        from_index[b] -= 1

    if from_index[a] == NUM_ROWS:
        from_index[a] = None
    if to_index[b] == NUM_ROWS - NUM_DISK - 1:
        to_index[b] = None

if DEBUG:
    print_towers()
    for i in range(0, 5):
        move(0, 1)
    print("move(0, 1)")
    print_towers()
    for i in range(0, 5):
        move(1, 0)
    print("move(1, 0)")
    print_towers()
    for i in range(0, 5):
        move(0, 2)
    print("move(0, 2)")
    print_towers()
    for i in range(0, 5):
        move(2, 1)
    print("move(2, 1)")
    print_towers()
    for i in range(0, 5):
        move(1, 2)
    print("move(1, 2)")
    print_towers()
    for i in range(0, 5):
        move(2, 0)
    print("move(2, 0)")
    print_towers()

if not DEBUG:
    while True:
        print_towers()
        in_move = input()
        move(int(in_move[0]) - 1, int(in_move[1]) - 1)

