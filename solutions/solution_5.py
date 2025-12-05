import sys


def solution_4_1(fresh_ids: list, current_ids: list):
    total_fresh = 0
    for id in current_ids:
        for start, end in fresh_ids:
            if id >= start and id <= end:
                total_fresh += 1
                break
    return total_fresh


def solution_4_2(fresh_ids: list):
    total_ids = 0
    fresh_ids = sorted(fresh_ids)
    for i in range(1, len(fresh_ids)):
        min1, min2, max1, max2 = fresh_ids[i - 1][0], fresh_ids[i][0], fresh_ids[i - 1][1], fresh_ids[i][1]
        if max1 >= min2:
            fresh_ids[i] = (min(min1, min2), max(max1, max2))
            fresh_ids[i - 1] = None
    for j in fresh_ids:
        if j:
            total_ids += j[1] - j[0] + 1 

    return total_ids


if __name__ == "__main__":
    fresh_ids = []
    current_ids = []
    break_found = False
    with open(sys.argv[1], 'r') as file:
        for line in file:    
            #print(line)
            line = line.strip()
            if break_found:
                current_ids.append(int(line))
            else:
                if line == "":
                    break_found = True
                    continue
                ids = line.split('-')
                fresh_ids.append((int(ids[0]), int(ids[1])))
    print(solution_4_1(fresh_ids, current_ids))
    print(solution_4_2(fresh_ids))