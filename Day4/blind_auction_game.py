
print("------------- Bidding Program -------------")

is_game_started = True
user_bid_dictionary = {}
names_list = []
amount_list = []
highest_bid = 0
winner = ""
def ask_user():
    name = input("What is your name?\n")
    bid_amount = float(input("How much money do you want to bid?\n"))
    user_bid_dictionary[name] = bid_amount
    is_more = input("Is there any other people wants to bid around you?\n").lower()

    if is_more == "no":
        global is_game_started
        global highest_bid
        global winner
        is_game_started = False
        for key in user_bid_dictionary:
            if (user_bid_dictionary[key]) > highest_bid:
                highest_bid = (user_bid_dictionary[key])
                winner = key
        print(f"The winner is {winner} with a bid amount of {highest_bid}")
    elif is_more == "yes":
        print("\n" * 60)
    else:
        is_game_started = False

while is_game_started:
    ask_user()