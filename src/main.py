"""
main.py

The nerve centre of the genetic algorithm. Calls other files.

"""
import util # A group of imports bundled together via an __init__.py file
import resources as res
import util.data_types as dt # data_types is somewhat special, as everyone else relies on them

POPULATION_SIZE = 12 # Must be a multiple of TOURNAMENT_SIZE
TOURNAMENT_SIZE = 3
MUTATION_ODDS = 88 # Must be < 100?
MAX_STAGNATION = 3
MAX_DEV = 77
SAFETY_BREAK = 15
START_NODE = dt.topography.get_node_by_name("ECS")
END_NODE = dt.topography.get_node_by_name("DTB")

def format_print_gen(generation):
    print("Current generation:")

    for i in range(len(generation)):
        print(str(generation[i]) + "\n")

def format_print_gen_fitness(generation):
    print("Current generation fitness:")

    for i in range(len(generation)):
        print(str(generation[i].get_fitness()) + ",", end = " ")

    print("and best fitness is:", min(generation, key = lambda soln: soln.get_fitness()).get_fitness())

def format_print_comparison(best_of_first, best_of_last):
    print("\n================\n")
    print("FINAL COMPARISON")
    print("First Generation:")
    print("    - Fitness:", best_of_first.get_fitness())
    print("    -", best_of_first.nodes)
    print("Last Generation:")
    print("    - Fitness:", best_of_last.get_fitness())
    print("    -", best_of_last.nodes)

# If you're familliar with C, this is basically the main() function.
if __name__ == "__main__":
    
    # Population & Encoding
    curr_generation = res.init_stochastic(START_NODE, END_NODE, POPULATION_SIZE)
    best_of_first_gen = min(curr_generation, key = lambda soln: soln.get_fitness())

    # Initialize our fitness history tracker
    codex_idoneitatem = []

    # This is a l'il debug safety measure to prevent infinite loops
    safety_valve_pressure = 0

    term_cond = False
    while not term_cond:
        # Selection
        chosen_parents = util.select_parents(curr_generation, TOURNAMENT_SIZE)
        chosen_pairs = util.mix_n_mingle(chosen_parents)

        # Remove parents from the generation (incremental version)
        curr_generation = [soln for soln in curr_generation if soln not in chosen_parents]

        # Crossover
        children = []
        for soln_a, soln_b in chosen_pairs:
            child_a, child_b = util.select_crossover(soln_a, soln_b)

            children.append(child_a)
            children.append(child_b)

        # Mutation
        for child in children:
            ids = util.select_mutation(child, MUTATION_ODDS)
            if ids is not None:
                # print("-- mutation occurred --")
                child.mutate(ids[0], ids[1])

        # Add the childs to the current generation
        curr_generation += children[:]

        # Update our fitness history
        codex_idoneitatem = util.add_to_history(curr_generation, codex_idoneitatem)

        print("Algo iter:", safety_valve_pressure)
        format_print_gen_fitness(curr_generation)

        # Terminating Condition
        term_cond = util.check_terminate(codex_idoneitatem, MAX_STAGNATION, MAX_DEV)
        
        print("Should terminate?", term_cond)

        safety_valve_pressure += 1

        if safety_valve_pressure > SAFETY_BREAK:
            print("!!!\n!!!PRESSURE TOO HIGH! EXECUTING EMERGENCY BREAK\n!!!")
            break

    best_of_last_gen = min(curr_generation, key = lambda soln: soln.get_fitness())
    format_print_comparison(best_of_first_gen, best_of_last_gen)