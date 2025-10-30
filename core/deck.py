import random

def build_standard_deck() -> list[dict]:
    cards = []
    suite = ['S','H','D','C']
    arr = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for i in range(len(arr)):
        for j in range(len(suite)):
            cardss = {"rank": arr[i],"suite": suite[j]}
            cards.append(cardss)
    return cards



def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:

       for i in range(swaps):
           index_i = random.randint(0, 51)
           index_j = random.randint(0,51)
           if index_i != index_j:
               if deck[index_i]["suite"] == "H":
                   if index_j % 5 == 0:
                       deck[index_j], deck[index_i] = deck[index_i], deck[index_j]

               elif deck[index_i]["suite"] == "C":
                   if index_j % 3 == 0:
                       deck[index_j], deck[index_i] = deck[index_i], deck[index_j]

               elif deck[index_i]["suite"] == "D":
                   if index_j % 2 == 0:
                       deck[index_j], deck[index_i] = deck[index_i], deck[index_j]

               elif deck[index_i]["suite"] == "S":
                   if index_j % 5 == 0:
                    deck[index_j], deck[index_i] = deck[index_i], deck[index_j]
       return deck



















