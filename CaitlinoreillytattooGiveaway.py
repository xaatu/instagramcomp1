import random

# ADD LIST OF FOLLOWERS IN THE STYLE SHOWN BELOW
followers = [
    "xaatumusic", "etc",
]


# SAME FOR COMMENTERS
commenters = [
    "xaatumusic", "etc",
]

unique_commenters = list(set(commenters))

# SAME FOR SHARERS
sharers = [
    "xaatumusic", "etc",
]

unique_sharers = list(set(sharers))

combined_list = unique_commenters + unique_sharers + followers

def pick_random_winner(participants_list):
    return random.choice(participants_list)

winner = pick_random_winner(combined_list)
print("The randomly selected winner is:", winner)
