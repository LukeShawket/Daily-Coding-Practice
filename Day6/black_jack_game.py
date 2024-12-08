"""BLACK JACK GAME"""
import random
from plistlib import dumps

print("\n\n------------- Welcome to Black Jack -------------\n\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
player_cards = []
game_loop_start = True
show_dealers = True

def shuffle():
    """Returns a random card from cards"""
    card = random.choice(cards)
    return card

# Game starts
for _ in range(2):
    new_player_card = shuffle()
    new_dealer_card = shuffle()
    player_cards.append(new_player_card)
    dealer_cards.append(new_dealer_card)
print(f"Dealer's first car is {dealer_cards[0]}, second card is unknown.\n")
print(f"Your cards {player_cards}, Your total points is {sum(player_cards)}.\n\n")

while game_loop_start:
    player_choice = input("Your next move: (Please type Hit or Stand)\n").lower()
    if player_choice == "hit":
        new_player_card = shuffle()
        player_cards.append(new_player_card)
        print(f"Your cards {player_cards}, Your total points is {sum(player_cards)}.\n\n")
        if sum(player_cards) > 21:
            print("Dealer Wins!")
            game_loop_start = False
    while player_choice == "stand":
        if show_dealers:
            print(f"Dealer's cards are {dealer_cards}, dealer's total point is {sum(dealer_cards)}")
            show_dealers = False
        if sum(dealer_cards) < 17:
            new_dealer_card = shuffle()
            dealer_cards.append(new_dealer_card)
            print(f"Dealer's cards are {dealer_cards}, dealer's total point is {sum(dealer_cards)}")
        elif sum(dealer_cards) > 21:
            print("You Win!")
            game_loop_start = False
            player_choice = ""
        elif 21 <= sum(dealer_cards) >= 17:
            if sum(dealer_cards) > sum(player_cards):
                print("Dealer Wins!")
                game_loop_start = False
                player_choice = ""
            elif sum(dealer_cards) == sum(player_cards):
                print("Game Draw!")
                game_loop_start = False
                player_choice = ""
            else:
                print("You Win!")
                game_loop_start = False
                player_choice = ""
