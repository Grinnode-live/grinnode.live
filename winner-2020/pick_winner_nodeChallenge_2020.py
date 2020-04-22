#!/usr/bin/env python3

# made in group therapy  togther with @energyburn and @phyro
# thank you. 

import requests
import random
import datetime


NUM_GRAND_PRIZES = 20
NUM_LUCKY_LOSERS = 10

x = datetime.datetime.now()


# Query the API for list of peers
response = requests.get("https://grinnode.live:8080/peers")

# Extract list of peers from request data
peers = response.json()["result"]

# Extract the first 20 grand prize winners
tickets = list(range(NUM_GRAND_PRIZES))
print("\n\nGRAND PRIZE WINNERS:")
print(x)

for i in range(NUM_GRAND_PRIZES):
    print("Peer ", tickets[i])
    print(peers[i])

# Select lucky losers from the remaining peers
peers = peers[NUM_GRAND_PRIZES:] # Exclude grand prize winners
tickets = [random.randrange(len(peers)) for i in range(NUM_LUCKY_LOSERS)]
print("\n\nLUCKY LOSERS:")
print(x)

for i in range(NUM_LUCKY_LOSERS):
    print("Peer ", tickets[i])
    print(peers[i])
