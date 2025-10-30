from deck import *
from game_logic import *
from main import *

def ask_player_action() -> str:
    c = True
    while c:
       choice = input("enter H or S: ")
       if type(choice) == str and len(choice) == 1:
           if choice == "h" or choice == "s":
              c = False
              b = choice.upper()
              return b



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    booli = True
    while booli:
       a = ask_player_action()
       if a == "H":
           z = player["hand"].append(deck.pop())
           sum = calculate_hand_value(player[z])
           if sum > 21:
               print("you lost")
               booli = False
       if a == "S":
           x = dealer_play(deck, dealer)

run_full_game(shuffle_by_suit(build_standard_deck()),player,dealer)