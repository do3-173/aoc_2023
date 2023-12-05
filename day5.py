def solver(seeds, input_text):
    seeds = list(map(int, input_text[0].split()[1:]))
    stages = []
    current_stage = []
    for line in input_text:
        if 'map:' in line:
            if current_stage:
                stages.append(current_stage)
                current_stage = []
        else:
            parts = line.split()
            if len(parts) == 3:
                current_stage.append(tuple(map(int, parts)))
    stages.append(current_stage)

    def map_through_stage(number, stage):
        for dest_start, src_start, length in stage:
            if src_start <= number < src_start + length:
                return dest_start + (number - src_start)
        return number

    for stage in stages:
        seeds = [map_through_stage(seed, stage) for seed in seeds]

    return min(seeds)

def solve_part1(input_text):
    seeds = list(map(int, input_text[0].split()[1:]))
    return solver(seeds, input_text)

def solve_part2(input_text):
    return 0


def main():
    with open("input/day5.txt") as f:
        lines = f.readlines()
    print(solve_part1(lines))
    print(solve_part2(lines))


if __name__ == "__main__":
    main()
