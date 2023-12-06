from math import prod


def parse_race(input_lines, part2=False):
    times, distances = [], []
    for line in input_lines:
        words = line.split()
        values = [int(word) for word in words[1:]]

        if "Time" in words[0]:
            if part2:
                times = int("".join(map(str, values)))
            else:
                times.extend(values)
        else:
            if part2:
                distances = int("".join(map(str, values)))
            else:
                distances.extend(values)

    return (times, distances) if part2 else (times, distances)


def calculate_duration(time, distance):
    start_time = next((a for a in range(time) if (time - a) * a > distance), 0)
    end_time = next((a for a in range(time, 0, -1) if (time - a) * a > distance), time)
    return end_time - start_time + 1


def solve_part1(input_lines):
    times, distances = parse_race(input_lines)
    return prod(calculate_duration(t, d) for t, d in zip(times, distances))


def solve_part2(input_lines):
    time, distance = parse_race(input_lines, part2=True)
    return calculate_duration(time, distance)


def main():
    with open("input/day6.txt") as file:
        lines = file.readlines()
    print(solve_part1(lines))
    print(solve_part2(lines))


if __name__ == "__main__":
    main()
