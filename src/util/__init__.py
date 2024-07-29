"""
__init__.py

Runs automatically when the /util library is imported.

Allows the bundling of files within the /util into a library, which is a nice way to package and access those files and thier methods. 
"""

# TODO: uncomment when we have methods/classes to import
# from util.population_init import class_to_import
# from util.node import class_to_import
# from util.node import class_to_import
# from util.straightline_distance import class_to_import

from .fitness import fitness_check, check_terminate, add_to_history
# import fitness as fit
from .combine_solns import select_mutation, mutate
from .data_types import Solution, Node
from .parent_selection import select_parents
from .population_init import init_pop
# from straightline_distance import 