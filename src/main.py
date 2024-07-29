"""
main.py

The nerve centre of the genetic algorithm. Calls other files.

"""
import util # A group of imports bundled together via an __init__.py file
import util.data_types as dt # data_types is somewhat special, as everyone else relies on them

TOURNAMENT_SIZE = 3
MUTATION_ODDS = 40

# If you're familliar with C, this is basically the main() function.
if __name__ == "__main__":
    
    # Population & Encoding
    curr_generation = util.init_pop()

    term_cond = False
    while not term_cond:
        # Selection
        chosen_parents = util.select_parents(curr_generation)

        # Crossover
        crossover_point_node = util.select_crossover()

        # Mutation
        for child in children:
            old_id, new_id = util.select_mutation(child)
            child.mutate(old_id, new_id)

        # Terminating Condition
        util.add_to_history()

        
        term_cond = True

    

