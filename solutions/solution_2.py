import sys

def solution_2_1(data: list[list]):
    total = 0
    for start, end in data:
        for value in range(int(start), int(end) + 1):
            
            text_val = str(value)
            half_len = len(text_val)//2
            if len(text_val) % 2 != 0:
                continue
            for i in range(0, half_len):
                if text_val[i] != text_val[i + half_len]:
                    break
            else:
                total += value
                print("found match", value)
    return total

def is_valid_id(value: int):
    text_val = str(value)
    for i in range(2, len(text_val) + 1):
        if len(text_val) % i == 0 and text_val[:len(text_val)//i] * i == text_val:
            return False
    return True


def solution_2_2(data: list[list]):
    total = 0
    for start, end in data:
        for value in range(int(start), int(end) + 1):
            if not is_valid_id(value):
                total += value
                print("found match", value)
    return total


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        data = file.readline()
    data = [d.split("-") for d in data.split(",")]

    print(solution_2_1(data))
    print(solution_2_2(data))
    print(data)