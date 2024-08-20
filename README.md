# campus-cruisers
ECE 470 Group Project

This project-based course was an introduction to Artificial Intellgence, requiring the implementation of a Genetic Algorithm; a repeating process which mimics natural selection in the pursuit of an optimal solution.

Campus Cruisers implements a Genetic Algorithm to find the shortest path between two points on campus. Taking in a vast network of nodes and arc lengths which represent every possible walking path on campus, the algorithm aims to quickly generate an initial population of solutions through fast yet unoptimal methods. Each iteration selects the highest performing solutions to generate new solutions from, replacing the parents from the prior generation. The end goal is to reach the most optimal shortest path, and ask the question: was it worth it? Was the extra time spent optimizing better than simply using an optimal search algorithm? Or re shortest-path problems not the best problem domain for a Genetic Algorithm?

## Design Specifications
- dataType.py
  - Contains the custom data objects we will be using.
  - Solution class
    - Data: a list of Nodes, optionally a fitness value
    - Methods: tbd
  - Node class
    - Data: id and coord
    - Methods: get_neighbours(Node), tbd
  - Lookup_table class
    - Data: nxn matrix of arc lengths between nodes
    - Methods: get_node(id), tbd
- fitness.py
  - Methods: get_fitness(Solution), check_termination(generation)
- combine_solns.py
  - Methods: select_mutation(Solution), mutate(Solution, Node_curr, Node_mut), select_crossover(Solution), crossover(Solution, Node_cross_point)

