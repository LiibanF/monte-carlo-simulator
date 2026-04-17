import simulator
import statistics
import experiments
import visualisation

print("Monte Carlo Simulator")
print("1. Coin Simulation")
print("2. Dice Simulation")

choice = input("Choose an option (1 or 2): ")


if choice == "1":

    trials = int(input("Number of trials: "))
    bias = float(input("Probability of heads (0–1): "))

    results = simulator.run_coin_simulation(trials, bias)

    freq = statistics.count_frequencies(results)
    probabilities = statistics.calculate_probabilities(freq, len(results))

    print("\n--- Coin Simulation Results ---")
    print("Frequencies:", freq)
    print("Probabilities:", probabilities)


elif choice == "2":

    trials = int(input("Number of trials: "))
    sides = int(input("Number of sides on dice: "))

    results = simulator.run_dice_simulation(trials, sides)

    freq = statistics.count_frequencies(results)
    probabilities = statistics.calculate_probabilities(freq, len(results))

    mean = statistics.calculate_mean(results)
    variance = statistics.calculate_variance(results)
    std_dev = statistics.calculate_standard_deviation(results)

    visualisation.plot_histogram(results)

    print("\n--- Dice Simulation Results ---")
    print("Frequencies:", freq)
    print("Probabilities:", probabilities)
    print("Mean:", mean)
    print("Variance:", variance)
    print("Standard Deviation:", std_dev)


    # Monte Carlo convergence experiment
    trial_sizes = [5, 10, 20, 50, 100, 200, 500, 1000]

    convergence_results = experiments.run_convergence_experiment(trial_sizes, sides)

    print("\n--- Convergence Experiment ---")
    for res in convergence_results:
        print(
            f"Trials: {res['trials']}, "
            f"Mean: {res['mean']:.3f}, "
            f"Variance: {res['variance']:.3f}, "
            f"Std Dev: {res['std_dev']:.3f}"
        )

    # Plot convergence
    visualisation.plot_convergence(convergence_results)


else:
    print("Invalid choice. Please restart and choose 1 or 2.")


"""
print(statistics.calculate_mean([1, 2, 3, 4, 5, 6])) #Debug
test_data = simulator.run_dice_simulation(10)
print(test_data)
"""