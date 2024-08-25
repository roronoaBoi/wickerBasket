"""
counts coin toss streaks of 6! this was an initial bugged version. leaving for learning exp.
"""
#pylint: disable=line-too-long
# import random

# streaks = 0

# results = ['H','T']

# all_flips = []

# for flips in range(1000):
#     ding = random.choice(results)
#     all_flips.append(ding)

# for i in range(len(all_flips) - 5): # this was - 1, but the problem with that is
# that when you are checking the last values for streaks, you can go beyond the list's end. this can result in errors.
#     if all(all_flips[i] == all_flips[i + j] for j in range(6)): # easy way to check a range in reference to an iteration (the all condition)
#         streaks = streaks + 1

# # this code is bugged due to all_flips being dynamic referring to an iteration, essentially not counting all options
# # v2 in this directory is the fixed version
# print (streaks)
