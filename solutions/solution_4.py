import sys


def valid_tp(x, y, data):
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    curr_rolls = 0
    print(len(data), len(data[0]))
    for offset_1, offset_2 in offsets:
        if x + offset_1 in range(len(data)) and y + offset_2 in range(len(data[0])) \
            and data[x + offset_1][y + offset_2] == "@":
            print('found roll', y, x, offset_1, offset_2)
            curr_rolls += 1
    if curr_rolls < 4:
        print("less than 4")
        return True
    return False


def solution_4_1(data):
    total_rolls = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            print(x,y)
            if data[x][y] == "@" and valid_tp(x, y, data):
                total_rolls += 1
    return total_rolls


def solution_4_2(data):
    curr_rolls = 1
    total_rolls = 0
    while curr_rolls > 0:
        curr_rolls = 0
        for y in range(len(data)):
            for x in range(len(data[0])):
                if data[x][y] == "@" and valid_tp(x, y, data):
                    data[x][y] = "."
                    total_rolls += 1
                    curr_rolls += 1
    return total_rolls

if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as file:
        for line in file: 
            data.append(list(line.strip()))
    print(solution_4_1(data))
    print(solution_4_2(data))
    print('')