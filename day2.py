def solve_part1(input_text):
    id_array = []
    for line in input_text:
        words_array = line.split()
        id = int(words_array[1][:-1])
        possible = True
        for i in range(2, len(words_array), 2):
            number = int(words_array[i])
            color = words_array[i + 1][0]
            if (
                "r" in color
                and number > 12
                or "g" in color
                and number > 13
                or "b" in color
                and number > 14
            ):
                possible = False
                break
        if possible:
            id_array.append(id)
    return sum(id_array)


def solve_part2(input_text):
    color_array = []
    for line in input_text:
        words_array = line.split()
        color_dict = {"r": [], "g": [], "b": []}
        for i in range(2, len(words_array), 2):
            number = int(words_array[i])
            color = words_array[i + 1][0]
            color_dict[color].append(number)
        color_array.append(
            max(color_dict["r"]) * max(color_dict["b"]) * max(color_dict["g"])
        )
    return sum(color_array)


def main():
    with open("input/day2.txt") as f:
        lines = f.readlines()
    print(solve_part1(lines))
    print(solve_part2(lines))


if __name__ == "__main__":
    main()
