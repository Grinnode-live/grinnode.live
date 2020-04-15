#!/usr/bin/env python3

import requests
import random

# Query the API for list of peers
response = requests.get("https://grinnode.live:8080/peers")

# Convert request data to dictionary of peers
peers = response.json()["result"]

# Create a bag of peers excluding the first 20
lucky_bag = peers[20:]

# Select 10 peers from the bag
lucky_losers = random.sample(lucky_bag, 10) 
for lucky_loser in lucky_losers:
    print("Lucky loser:", lucky_loser)
