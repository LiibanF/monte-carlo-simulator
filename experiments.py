import simulator
import statistics

def run_convergence_experiment(trial_sizes, sides=6):
    results = []
    for trials in trial_sizes:
        dice_results = simulator.run_dice_simulation(trials, sides)
        print(dice_results[:10])
        mean = statistics.calculate_mean(dice_results)
        variance = statistics.calculate_variance(dice_results)
        std_dev = statistics.calculate_standard_deviation(dice_results)
        
        results.append({
            "trials": trials,
            "mean": mean,
            "variance": variance,
            "std_dev": std_dev
        })

    return results   