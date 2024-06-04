from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bid_dict = {}
more_bidders = False

while not more_bidders:
  name = input("Please enter your name:\n")
  bid = int(input("Please enter the bid amount in INR: \n"))
  bid_dict[name] = bid
  ask_for_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  
  if ask_for_bidders == "yes":
    clear()
  
  elif ask_for_bidders == "no":
    more_bidders = False
    for key in bid_dict:
      highest_bid = 0
      if bid_dict[key] > highest_bid:
        highest_bid = bid_dict[key]
        winner = key
    print(f"The winner is {winner} with a bid of ₹{highest_bid}. Congratulations!")
    break

  else:
    print("Please enter either 'yes or 'no'.")
