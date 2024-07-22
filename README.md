# campus-cruisers
ECE 470 Group Project



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

