import random


followers = [
    "xaatumusic", "etc",
]



commenters = [
    "xaatumusic", "etc",
]

unique_commenters = list(set(commenters))

sharers = [
    "xaatumusic", "etc",
]

unique_sharers = list(set(sharers))

combined_list = unique_commenters + unique_sharers + followers

def pick_random_winner(participants_list):
    return random.choice(participants_list)

winner = pick_random_winner(combined_list)
print("The randomly selected winner is:", winner)
