import sys
from functools import lru_cache


@lru_cache
def dfs(start, end):
    total = 0
    for path in paths[start]:
        if path == end:
            total += 1
        elif path == 'out':
            break
        else:
            total += dfs(path, end)
    return total


def solution_10_1():
    return dfs('you', 'out')


def solution_10_2():
    return dfs('svr', 'fft') * dfs('fft', 'dac') * dfs('dac', 'out') \
        + dfs('svr', 'dac') * dfs('dac', 'fft') * dfs('fft', 'out')


if __name__ == "__main__":
    paths = {}
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start, *end = line.split(':')
            paths[start] = end[0].strip().split()

    print(solution_10_1())
    print(solution_10_2())
    