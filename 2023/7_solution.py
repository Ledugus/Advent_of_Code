def step_1(filename):
    total_wins = 0
    f = open(filename)
    list_of_hands = []
    for line in f:
        hand, bid = line.strip().split()
        list_of_hands.append((hand, int(bid)))
    # list_of_types = [get_type(hand[0]) for hand in list_of_hands]
    hands_sorted_values = sorted(list_of_hands,
                                 key=lambda hand: ordering(hand[0]), reverse=True)
    hands_sorted = sorted(
        hands_sorted_values, key=lambda hand: get_type(hand[0]), reverse=True)
    return sum([(len(hands_sorted)-index) * hand[1] for index, hand in enumerate(hands_sorted)])


card_values = ["A", 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def ordering(hand: str):
    return sum([13**(len(hand)-index) * (len(card_values)-card_values.index(char)) for index, char in enumerate(hand)])


types: dict[tuple[int, ...], int] = {(5,): 6, (4, 1): 5, (3, 2): 4, (3, 1, 1): 3,
                                     (2, 2, 1): 2, (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 0}


def get_type(hand):
    num_j = 0
    counts = {}
    for char in hand:
        if char == 'J':
            num_j += 1
        else:
            counts[char] = counts.get(char, 0) + 1
    if not counts:
        counts = {"": 0}
    max_key = max(counts.keys(), key=(lambda key: counts[key]))
    counts[max_key] += num_j

    sequence = tuple(sorted(counts.values(), reverse=True))
    print(hand, sequence)
    return types[sequence]


print(step_1("7_input.txt"))
