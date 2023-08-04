from random import randrange, seed, shuffle
from time import time
from argparse import ArgumentParser
from matplotlib import pyplot


def random_gene():
    return randrange(0, 8)


def random_locus():
    return randrange(0, 8)


def random_chromosome():
    return [random_gene() for _ in range(8)]


# mutate at a random locus
def mutate(c):
    locus = random_locus()
    c[locus] = random_gene()
    return c


# crossover at a random locus
def crossover(c1, c2):
    locus = random_locus()
    child = c1[0:locus] + c2[locus:]
    return child


# generate the initial population
def initial_population(size):
    return [random_chromosome() for _ in range(size)]


# calculate the fitness of a chromosome (lower number is better)
def fitness(c):
    fit = 0
    for g in c:
        fit += c.count(g) - 1
    for i in range(8):
        g = c[i]
        for j in range(i + 1, 8):
            if g + (j - i) == c[j]:
                fit += 1
            if g - (j - i) == c[j]:
                fit += 1
        for j in range(i - 1, -1, -1):
            if g + (j - i) == c[j]:
                fit += 1
            if g - (j - i) == c[j]:
                fit += 1
    return fit


def random_parents(parents):
    psize = len(parents)
    p1 = randrange(0, psize)
    p2 = randrange(0, psize)
    while p2 == p1:
        p2 = randrange(0, psize)
    return (parents[p1][1], parents[p2][1])


# construct the next generation of population
def generational_step(population, mutation_pct):
    psize = len(population)
    # generate children
    children = []
    while len(children) < psize:
        # selection of two parents to crossover
        parents = population[0 : randrange(1, psize // 2)]
        # random shuffle of possible parents
        shuffle(parents)
        # two parents are required
        if len(parents) < 2:
            continue
        p1, p2 = random_parents(parents)
        child = crossover(p1, p2)
        if randrange(0, 100) < mutation_pct:
            child = mutate(child)
        children.append(child)
    return children


def average_fitness(population):
    l = len(population)
    p = [c[0] for c in population]
    return sum(p) // l


def print_population(population):
    fit_stats = {}
    for p in population:
        print("Fit ", p[0], " Queens ", p[1])
        if p[0] in fit_stats:
            fit_stats[p[0]] += 1
        else:
            fit_stats[p[0]] = 1
    print()
    print("Summary:")
    for key in fit_stats:
        print("Fit: ", key, " - Count: ", fit_stats[key])
    print()


def run(population_size, num_iterations, mutation_pct):
    population = initial_population(population_size)
    population = [(fitness(c), c) for c in population]
    population.sort()
    print("=========================== Initial Population:")
    print_population(population)
    max_fit = []
    max_fit.append(population[0][0])
    avg_fit = []
    avg_fit.append(average_fitness(population))
    for _ in range(num_iterations):
        population = generational_step(population, mutation_pct)
        population = [(fitness(c), c) for c in population]
        population.sort()
        max_fit.append(population[0][0])
        avg_fit.append(average_fitness(population))
    print("=========================== Final Population:")
    print_population(population)
    results = {"max_fit": max_fit, "avg_fit": avg_fit}
    return results


parser = ArgumentParser(
    prog="main.py",
    description="Find solutions to 8 Queen puzzle using a genetic algorithm.",
)
parser.add_argument(
    "-p",
    "--population-size",
    dest="population_size",
    help="initial population size (default: 10)",
    default=10,
)
parser.add_argument(
    "-i",
    "--iterations",
    dest="iterations",
    help="number of generational iterations (default: 50)",
    default=50,
)
parser.add_argument(
    "-m",
    "--mutation-percent",
    dest="mutation_pct",
    help="percent change of mutation (0-100) (default: 50)",
    default=50,
)
parser.add_argument(
    "-s",
    "--seed",
    dest="seed",
    help="seed the random number generator (default: system time)",
)
parser.add_argument(
    "-g", "--graph", help="generate generational fitness graph", action="store_true"
)

args = parser.parse_args()

rand_seed = int(time())

if args.seed:
    rand_seed = args.seed

seed(rand_seed)

print("Population Size: ", str(args.population_size))
print("Iterations: ", str(args.iterations))
print("Mutation %: ", args.mutation_pct)
print("Seed: ", str(rand_seed))
print()

results = run(int(args.population_size), int(args.iterations), int(args.mutation_pct))

if args.graph:
    print()
    print("Saving graph.")
    fig = pyplot.figure()
    pyplot.plot(results["avg_fit"], label="Average")
    pyplot.plot(results["max_fit"], label="Best")
    pyplot.xlabel("Generation")
    pyplot.ylabel("Fit")
    pyplot.grid()
    pyplot.tight_layout()
    pyplot.legend()
    pyplot.savefig(
        "fitplot-P"
        + str(args.population_size)
        + "-I"
        + str(args.iterations)
        + "-M"
        + str(args.mutation_pct)
        + ".png"
    )
