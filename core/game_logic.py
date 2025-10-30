
def calculate_hand_value(hand: list[dict],) -> int:
    sum_of_cards = 0
    for i in range(len(hand)):
        if hand[i]["rank"] == "J" or hand[i]["rank"] == "Q" or hand[i]["rank"] == "k":
           sum_of_cards += 10

        elif hand[i]["rank"] == "A":
           sum_of_cards += 1

        else:
           a = int(hand[i]["rank"])
           sum_of_cards += a
    return sum_of_cards


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for i in range(2):
        player["hand"].append(deck.pop())
        dealer["hand"].append(deck.pop())
    print(calculate_hand_value(player["hand"]))
    print(calculate_hand_value(dealer["hand"]))


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    # dealer["hand"] +=
    while dealer["hand"] >= 17:
        if dealer["hand"] > 21:
            return False
        else:
            return True


