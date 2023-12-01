def solve_part1(input_text):
    return sum(
        int(
            "".join(filter(str.isdigit, line))[0]
            + "".join(filter(str.isdigit, line))[-1]
        )
        for line in input_text
    )


def solve_part2(input_text):
    # eightwothree will become eight8eightwo2twothree3three
    # having this all values will be taken into consideration (instead of being 8wo3 or eigh23)
    modified_text = []
    for line in input_text:
        line = (
            line.replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine"))
        modified_text.append(line)
    return solve_part1(modified_text)


def main():
    with open("input/day1.txt") as f:
        lines = f.readlines()
    print(solve_part1(lines))
    print(solve_part2(lines))


if __name__ == "__main__":
    main()
