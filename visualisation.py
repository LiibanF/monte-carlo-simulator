import matplotlib.pyplot as plt # type: ignore

def plot_convergence(results):
    plt.figure()
    
    trials = []
    means = []
    for res in results:
        trials.append(res["trials"])
        means.append(res["mean"])

    plt.plot(trials, means)
    plt.xlabel("Number of Trials")
    plt.ylabel("mean")
    plt.title("Monte Carlo Convergence (Dice Mean)")
    plt.show() 


def plot_histogram(data):
    plt.figure
    plt.hist(data, bins=10)
    plt.xlabel("Dice Value")
    plt.ylabel("Frequency")
    plt.title("Dice Roll Distribution")
    plt.show