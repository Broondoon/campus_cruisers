"""
__init__.py

Runs automatically when the /util library is imported.

Allows the bundling of files within the /util into a library, which is a nice way to package and access those files and thier methods. 
"""

from .fitness import check_terminate, add_to_history
from .combine_solns import select_mutation, select_crossover
from .parent_selection import select_parents, mix_n_mingle
from .population_init import init_pop, debug_init_pop