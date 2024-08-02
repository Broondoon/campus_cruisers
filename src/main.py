"""
main.py

The nerve centre of the genetic algorithm. Calls other files.

"""
import util # A group of imports bundled together via an __init__.py file
import resources as res
import util.data_types as dt # data_types is somewhat special, as everyone else relies on them

POPULATION_SIZE = 12 # Must be a multiple of TOURNAMENT_SIZE
TOURNAMENT_SIZE = 3
MUTATION_ODDS = 40
START_NODE = dt.topography.get_node_by_name("ECS")
END_NODE = dt.topography.get_node_by_name("DTB")

# If you're familliar with C, this is basically the main() function.
if __name__ == "__main__":
    
    # Population & Encoding
    # curr_generation = util.debug_init_pop(POPULATION_SIZE)
    curr_generation = res.random_depth_first_search(START_NODE, END_NODE)

    print("Current generation:", curr_generation)

    # print("STR TEST:")
    # print(curr_generation[0])

    term_cond = False
    while not term_cond:
        # Selection
        # chosen_parents = util.select_parents(curr_generation, TOURNAMENT_SIZE)
        # chosen_pairs = util.mix_n_mingle(chosen_parents)

        # Crossover
        # crossover_point_node = util.select_crossover()



        # # Mutation
        # for child in children:
        #     old_id, new_id = util.select_mutation(child)
        #     child.mutate(old_id, new_id)

        # # Terminating Condition
        # util.add_to_history()

        
        term_cond = True

    

