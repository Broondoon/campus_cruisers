import sys
sys.path.append("..")
from src.util import parent_selection
from src.util import population_init

POPULATION_SIZE = 12 # Must be a multiple of TOURNAMENT_SIZE
TOURNAMENT_SIZE = 3

generation = population_init.debug_init_pop(POPULATION_SIZE)
chosen_parents = parent_selection.select_parents(generation, TOURNAMENT_SIZE)

print(chosen_parents)

