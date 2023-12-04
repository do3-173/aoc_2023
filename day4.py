def extract_winning_data(game_array):
    winning_numbers = []
    number_of_winning = 0
    is_winning_numbers_section = True

    for item in game_array[2:]:
        if item == "|":
            is_winning_numbers_section = False
        elif is_winning_numbers_section:
            winning_numbers.append(item)
        elif item in winning_numbers:
            number_of_winning += 1

    return winning_numbers, number_of_winning


def solve_part1(input_text):
    winning_score = 0
    for line in input_text:
        game_array = line.split()
        _, number_of_winning = extract_winning_data(game_array)
        winning_score += int(pow(2, number_of_winning - 1))
    return winning_score


def solve_part2(input_text):
    game_dict = {}
    instances_of_cards = {}

    for line in input_text:
        game_array = line.split()
        id = int(game_array[1][:-1])
        _, number_of_winning = extract_winning_data(game_array)
        game_dict[id] = number_of_winning

    for id, win_count in game_dict.items():
        if id not in instances_of_cards:
            instances_of_cards[id] = 1
        for _ in range(instances_of_cards[id]):
            for i in range(win_count):
                next_id = id + 1 + i
                instances_of_cards[next_id] = instances_of_cards.get(next_id, 1) + 1

    return sum(instances_of_cards.values())


def main():
    with open("input/day4.txt") as f:
        lines = f.readlines()
    print(solve_part1(lines))
    print(solve_part2(lines))


if __name__ == "__main__":
    main()
