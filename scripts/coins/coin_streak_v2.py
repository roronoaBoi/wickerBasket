"""
fixed streak counter (coin_streak_bugged), counts streaks of 6 in 10,000 coin tosses
"""
# pylint: disable=invalid-name
import random

num_flips = 10000

# Generate 1000 coin flips at once
all_flips = [random.choice(['H', 'T']) for _ in range(num_flips)]

streaks = 0

# Check for streaks of 6 in the sequence
for i in range(len(all_flips) - 5):  # len(all_flips) - 5 to avoid out of range error
    if all_flips[i:i + 6] == ['H'] * 6 or all_flips[i:i + 6] == ['T'] * 6:
        streaks += 1

print('Streak Stats:')
print(str(streaks) + ' at ' + str((streaks/num_flips) * 100) + '% of ' + str(num_flips) + ' flips!')
