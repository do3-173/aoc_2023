def is_valid_char(c):
    return c not in ".\n0123456789"


def check_possible(row, start_idx, end_idx, input_text):
    for idx_row, idx_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        for i in range(start_idx, end_idx + 1):
            r, c = row + idx_row, i + idx_col
            if (
                0 <= r < len(input_text)
                and 0 <= c < len(input_text[r])
                and is_valid_char(input_text[r][c])
            ):
                return True

    for idx_row, idx_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        r, c = row + idx_row, (start_idx if idx_col == -1 else end_idx) + idx_col
        if (
            0 <= r < len(input_text)
            and 0 <= c < len(input_text[r])
            and is_valid_char(input_text[r][c])
        ):
            return True

    return False
    
def find_location_numbers(input_text, check=False):
    nums = []
    for row_idx, line in enumerate(input_text):
        i = 0
        while i < len(line):
            if line[i].isdigit():
                start_i = i
                while i < len(line) and line[i].isdigit():
                    i += 1
                if check:
                    if check_possible(row_idx, start_i, i - 1, input_text):
                        nums.append(int(line[start_i:i]))
                else:
                    nums.append((int(line[start_i:i]), (row_idx, start_i, i - 1)))
            else:
                i += 1
    return nums

def solve_part1(input_text, check=True):
    return sum(find_location_numbers(input_text, check=True))

def solve_part2(input_text):
    nums = find_location_numbers(input_text)
    gears = {}
    gear_ratio = []
    for num in nums:
        for i in range(num[1][0] - 1, num[1][0] + 2):
            if i >= 0 and i < len(input_text):
                for j in range(num[1][1] - 1, num[1][2] + 2):
                    if j >= 0 and j < len(input_text[0]):
                        if input_text[i][j] == "*":
                            if not gears.get((i, j)):
                                gears[(i, j)] = []
                            gears[(i, j)].append(num[0])

    for gear in gears:
        if len(gears[gear]) == 2:
            gear_ratio.append(gears[gear][0] * gears[gear][1])

    return sum(gear_ratio)


def main():
    with open("input/day3.txt") as f:
        lines = f.readlines()
    print(solve_part1(lines))
    print(solve_part2(lines))


if __name__ == "__main__":
    main()
