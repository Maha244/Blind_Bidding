# from replit import clear
import os
clearConsole = lambda: print('\n' * 150)
from art import logo
print(logo)


bids = {}
end_program = False

# bidding_record = {"Maha": 123, "James": 321} == bids
def find_highest_bidder(bidding_record):
    largest_bid = 0
    winner = ""
    for name in bidding_record:
        bid_amount = bidding_record[name]
        if bid_amount > largest_bid:
            largest_bid = bid_amount
            winner = name
    print(f"The winner is {winner} with a bid of ${largest_bid}")

while  not end_program :
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    bids[user_name] = user_bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "yes":
        clearConsole()
    elif should_continue == "no":
        end_program = True
        find_highest_bidder(bids)
