"""
main.py

The nerve centre of the genetic algorithm. Calls other files.

"""
import util # A group of imports bundled together via an __init__.py file
import util.data_types as dt # data_types is somewhat special, as everyone else relies on them
from globals import topography # 

# If you're familliar with C, this is basically the main() function.
if __name__ == "__main__":
    
    # Population & Encoding
    initial_solutions = util.init_pop()

    # util.fitness_check()

    term_cond = False
    while not term_cond:

        print("Yes once")
        term_cond = True

    # Fitness Function

    # Selection

    # Crossover

    # Mutation

    # Terminating Condition

