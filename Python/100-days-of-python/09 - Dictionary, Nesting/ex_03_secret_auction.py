import art
print(art.secret_auction)

def getBid():
  name = input("Name: ")
  amount = int(input("Your bid amount: $"))
  return {
    "name" : name,
    "amount" : amount
  }

# MAIN
# --------------------------------------------
bids = []
askForBids = True

while askForBids:
  bids.append(getBid())

  print()
  moreBids = input("More bids y or n? ")
  if moreBids == "n":
    askForBids = False
  else:
    # clear screen
    print()

if len(bids) == 0:
  print("There were not bids")
else:
  winningBid = {}
  maxBid = 0
  print()
  for bid in bids:
    if (maxBid < bid["amount"]):
      maxBid = bid["amount"]
      winningBid = bid
  print(f"Winning bid is by {winningBid['name']}. Amount is {winningBid['amount']}.")
