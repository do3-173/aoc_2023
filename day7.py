from collections import Counter

# Step 1: Rank the cards and hands
def card_ranking_creation():
    card_values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    card_ranking = {card: idx for idx, card in enumerate(card_values)}
    return card_ranking

def hand_type(hand):
    counts = Counter(hand)
    values = list(counts.values())
    if 5 in values:
        return 7  # Five of a kind
    elif 4 in values:
        return 6  # Four of a kind
    elif 3 in values and 2 in values:
        return 5  # Full house
    elif 3 in values:
        return 4  # Three of a kind
    elif values.count(2) == 2:
        return 3  # Two pair
    elif 2 in values:
        return 2  # One pair
    else:
        return 1  # High card


def compare_hands(hand1, hand2, card_ranking):
    type1, type2 = hand_type(hand1), hand_type(hand2)
    if type1 != type2:
        return type1 - type2

    count1 = Counter(hand1)
    count2 = Counter(hand2)

    # Sort the hands by frequency and then by card rank
    sorted_hand1 = sorted(hand1, key=lambda x: (count1[x], card_ranking[x]), reverse=True)
    sorted_hand2 = sorted(hand2, key=lambda x: (count2[x], card_ranking[x]), reverse=True)

    # Compare the sorted hands card by card
    for c1, c2 in zip(sorted_hand1, sorted_hand2):
        if card_ranking[c1] != card_ranking[c2]:
            return card_ranking[c1] - card_ranking[c2]
    return 0

def sorted_hand(hand, card_ranking):
    # Sorts the hand by frequency of cards and then by card rank
    count = Counter(hand)
    return sorted(hand, key=lambda x: (count[x], card_ranking[x]), reverse=True)

def sort_hands(hands, card_ranking):
    return sorted(hands, key=lambda x: (hand_type(x[0]), [card_ranking[c] for c in sorted_hand(x[0], card_ranking)]), reverse=True)

# Step 3: Calculate winnings
def total_winnings(hands):
    card_ranking = card_ranking_creation()
    sorted_hands = sort_hands(hands, card_ranking)
    print(sorted_hands)
    winnings = sum(bid * (idx + 1) for idx, (_, bid) in enumerate(sorted_hands))
    return winnings

# Example input
hands = [("32T3K", 765), ("T55J5", 684), ("KK677", 28), ("KTJJT", 220), ("QQQJA", 483)]
print(total_winnings(hands))
