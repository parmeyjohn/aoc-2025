import sys


def solution_7_1(rows: list[str]):
    beam_locations = set()
    split_locations = set()

    for i in range(len(rows[0])):
        if rows[0][i] == 'S':
            beam_locations.add((0, i))
            break
    while beam_locations:
        row, col = beam_locations.pop()
        # print(row, col)
        if row not in range(len(rows)):
            continue
        if rows[row][col] == "^":
            split_locations.add((row,col))
            beam_locations.add((row + 1, col - 1))
            beam_locations.add((row + 1, col + 1))
        else:
            beam_locations.add((row + 1, col))
    return len(split_locations)
        

def solution_7_2(location: tuple[int], rows: list[str]):
    
    row, col = location
    # print(row, col)
    if location in seen:
        return seen[location]
    if row not in range(len(rows)):
        return 1
    if rows[row][col] == "^":
        left, right = solution_7_2((row + 1, col - 1), rows), solution_7_2((row + 1, col + 1), rows)
        seen[(row + 1, col - 1)] = left
        seen[(row + 1, col + 1)] = right
        return left + right
    curr = solution_7_2((row + 1, col), rows)
    seen[(row + 1, col)] = curr
    return curr


if __name__ == "__main__":
    rows = []
    seen = {}

    with open(sys.argv[1], 'r') as file:
        for line in file:
            rows.append(line.strip())
    start = (0, 0)
    for i in range(len(rows[0])):
        if rows[0][i] == 'S':
            start = (0, i)
            break

    print(rows)
    print(solution_7_1(rows))
    print(seen)
    print(solution_7_2(start, rows))