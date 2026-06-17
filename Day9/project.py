'''
Silent Auction
enter name
enter bid
then find out who bid highest with their name and bid amount

'''
from cmath import inf

dict_auction_members = {}

for i in range(0,5):
    name = input("Enter name")
    bid = int(input("Enter bid"))
    dict_auction_members[name] = bid

print(dict_auction_members)

max_bid = -inf
winner = ""
for k,v in dict_auction_members.items():
    if v > max_bid:
        max_bid = v
        winner = k

print(f"The winner is {winner} with bid of ${max_bid}")