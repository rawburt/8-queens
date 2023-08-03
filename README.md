# 8-Queens

This program solves the [Eight Queens Puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) using a [genetic algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm).

## Program Requirements

* Python 3.11+

Python libraries:

* matplotlib

The required Python libraries can be installed using `pip3`:

```sh
pip3 install -r requirements.txt
```

## Program Usage

From the project directory, run the `main.py` file to run the simulation:

```sh
python3 main.py
```

The following command-line options are available:

```sh
usage: main.py [-h] [-p POPULATION_SIZE] [-i ITERATIONS] [-m MUTATION_PCT] [-s SEED] [-g]

Find solutions to 8 Queen puzzle using a genetic algorithm.

options:
  -h, --help            show this help message and exit
  -p POPULATION_SIZE, --population-size POPULATION_SIZE
                        initial population size (default: 10)
  -i ITERATIONS, --iterations ITERATIONS
                        number of generational iterations (default: 50)
  -m MUTATION_PCT, --mutation-percent MUTATION_PCT
                        percent change of mutation (0-100) (default: 50)
  -s SEED, --seed SEED  seed the random number generator (default: system time)
  -g, --graph           generate generational fitness graph
```

# References

* "An Introduction to Genetic Algorithms" by Melanie Mitchell
