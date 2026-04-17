import random 

def flip_coin(probability_of_heads=0.5):
    if random.random() < probability_of_heads:
        return "H"
    else:
       return "T"

def roll_die(sides=6):
    return random.randint(1, sides)

def run_coin_simulation(number_of_trials, probability_of_heads=0.5):
    results = []
    for i in range(number_of_trials):
        outcome = flip_coin(probability_of_heads)
        results.append(outcome)
    return results

def run_dice_simulation(number_of_trials, sides=6):
    results = []
    for i in range(number_of_trials):
        roll = roll_die(sides)
        results.append(roll)
    return results
    