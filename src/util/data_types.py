"""
dataType.py

Contains the definition for the node() object class.

We could also update this file to have any/all custom objects/classes.

"""
import numpy as np

class Node:
    name = None
    id = None
    xy = None

    soln_parent = None

    def __init__(self, name, id, coordinate, parent = None):
        self.name = name
        self.id = id
        self.xy = coordinate

        self.soln_parent = parent

    def __str__(self) -> str:
        return "(" + self.name + " " + str(self.id) + ")" 
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:        
        if self.id == value.id:
            return True
        
        return False

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    # Returns a list of node objects
    def get_neighbours(self):
        # Defining empty list and adding values to it
        neighbour_list = []
        row_num = self.id

        for index, cell in enumerate(topography.lookup_table.data[row_num]):
            if cell is not None:
                neighbour_list.append(topography.get_node_by_id(index))

        return neighbour_list
    
    def set_parent(self, parent):
        self.soln_parent = parent

class Solution: 
    nodes = []
    fitness = None

    def __init__(self, nodes, fitness = None):
        self.nodes = nodes

        if fitness == None:
            self.fitness = self.fitness_check()

    def __str__(self) -> str:
        return "<Solution: " + ", ".join(str(node) for node in self.nodes) + ">\n"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        if len(self.nodes) != len(value.nodes):
            return False
        
        for i in range(len(self.nodes)):
            if self.nodes[i] != value.nodes[i]:
                return False
        
        return True

    # Takes a solution object and evaluates its fitness.
    # Input: solution object of potential solution, the lookup_table
    # Output: the total distance from start to end of the path
    def fitness_check(self):
        # variables used in calculation
        running_sum = 0
        prev = None
        # loop through nodes in solution
        for node in self.nodes:
            # add distance from the previous node
            if prev:
                running_sum += topography.lookup_table.data[prev.id][node.id]
            # set the previous node to the current node
            prev = node
        # prepare answer
        total_distance = running_sum

        # return the calculated finess
        return total_distance
    
    # Update the fitness val by doing a fitness check
    def refresh_fitness(self):
        self.fitness = self.fitness_check()

    # Get the fitness, and if it's None, generate it.
    def get_fitness(self):
        if self.fitness is None:
            self.refresh_fitness()
        
        return self.fitness

    def mutate(self, new_id, old_id):
        # Make a list from an old list
        # But grab a new node instead of one from the old list if the id matches 
        # Otherwise, populate with old nods
        self.nodes = [topography.get_node_by_id(new_id) if node.id == old_id else node for node in self.nodes]
        self.refresh_fitness()

    # Input: self, another solution, indecies for crossing over, any extra nodes, and the case
    # Output: two child Solutions
    def crossover(self, partner_soln, index_a, index_b, extra_node_list, case):
        if case == "same":
            # includes start point of from here, ie list[startpoint:]
            # does Not include end point of until here, ie list[:endpoint]
            # becuase they are the same
            new_a_nodes = self.nodes[:index_a] + partner_soln.nodes[index_b:]
            new_b_nodes = partner_soln.nodes[:index_b] + self.nodes[index_a:]
        elif case == "first_cousin":
            # includes both because they are different
            new_a_nodes = self.nodes[:index_a+1] + partner_soln.nodes[index_b:]
            new_b_nodes = partner_soln.nodes[:index_b+1] + self.nodes[index_a:]
        else:
            # therefore case == "second_cousins"
            new_a_nodes = self.nodes[:index_a+1] + extra_node_list + partner_soln.nodes[index_b:]
            new_b_nodes = partner_soln.nodes[:index_b+1] + extra_node_list + self.nodes[index_a:]

        child_a = Solution(new_a_nodes)
        child_b = Solution(new_b_nodes)

        return (child_a, child_b)

class Lookup_Table:
    data = None

    def __init__(self):
        self.createDistTable()

    # Creates and populates a lookup table with our data.
    def createDistTable(self):

        n = 63 # Added +1 to avoid argument-out-of-range issue on line 115

        # Creates a matrix of nxn filled with "None"
        arr = [[None for _ in range(n)] for _ in range(n)]

        arr[0][35] = arr[35][0] = 48.34
        arr[0][55] = arr[55][0] = 53.83
        arr[2][3] = arr[3][2] = 10.72
        arr[3][4] = arr[4][3] = 81.52
        arr[3][49] = arr[49][3] = 87.76
        arr[4][5] = arr[5][4] = 68.59
        arr[5][6] = arr[6][5] = 31.58
        arr[6][7] = arr[7][6] = 38.67
        arr[7][8] = arr[8][7] = 86.80
        arr[6][46] = arr[46][6] = 84.19
        arr[7][44] = arr[44][7] = 36.51
        arr[8][9] = arr[9][8] = 17.42
        arr[8][11] = arr[11][8] = 21.36
        arr[9][10] = arr[10][9] = 18.1
        arr[9][45] = arr[45][9] = 37.59
        arr[10][11] = arr[11][10] = 20.7
        arr[10][12] = arr[12][10] = 12.81
        arr[12][13] = arr[13][12] = 21.1
        arr[13][14] = arr[14][13] = 29.56
        arr[13][17] = arr[17][13] = 28.77
        arr[15][14] = arr[14][15] = 21.88
        arr[14][17] = arr[17][14] = 13.76
        arr[15][16] = arr[16][15] = 19.37
        arr[15][18] = arr[18][15] = 18.5
        arr[16][1] = arr[1][16] = 62.65
        arr[16][24] = arr[24][16] = 44.8
        arr[17][18] = arr[18][17] = 18.89
        arr[19][1] = arr[1][19] = 53.15
        arr[19][20] = arr[20][19] = 34.53
        arr[20][21] = arr[21][20] = 55.97
        arr[21][22] = arr[22][21] = 38.73
        arr[21][25] = arr[25][21] = 12.92
        arr[21][26] = arr[26][21] = 12.41
        arr[22][19] = arr[19][22] = 23.32
        arr[22][23] = arr[23][22] = 24.59
        arr[23][24] = arr[24][23] = 22.91
        arr[23][25] = arr[25][23] = 17.25
        arr[24][25] = arr[25][24] = 33.58 
        arr[25][27] = arr[27][25] = 28.78
        arr[26][27] = arr[27][26] = 15.36
        arr[27][28] = arr[28][27] = 33.81
        arr[27][29] = arr[29][27] = 37.86
        arr[27][31] = arr[31][27] = 81.23
        arr[28][29] = arr[29][28] = 21.67
        arr[28][34] = arr[34][28] = 45.14
        arr[29][30] = arr[30][29] = 21.33
        arr[30][31] = arr[31][30] = 39.19
        arr[30][32] = arr[32][30] = 38.62
        arr[31][32] = arr[32][31] = 40.4
        arr[32][33] = arr[33][32] = 34.53
        arr[33][34] = arr[34][33] = 84.08

        arr[34][35] = arr[35][34] = 19.82
        arr[34][45] = arr[45][34] = 47.48
        arr[34][43] = arr[43][34] = 108.24
        arr[35][36] = arr[36][35] = 56.92
        arr[35][38] = arr[38][35] = 59.39
        arr[36][37] = arr[37][36] = 47.63
        arr[36][38] = arr[38][36] = 48.54
        arr[37][39] = arr[39][37] = 48.36
        arr[37][50] = arr[50][37] = 41.68
        arr[38][39] = arr[39][38] = 51
        arr[38][42] = arr[42][38] = 85.57
        arr[39][40] = arr[40][39] = 10.84
        arr[40][41] = arr[41][40] = 28.76
        arr[41][42] = arr[42][41] = 34.74
        arr[41][47] = arr[47][41] = 26.85
        arr[41][48] = arr[48][41] = 56.55
        arr[42][43] = arr[43][42] = 34.72
        arr[43][44] = arr[44][43] = 44.48
        arr[44][45] = arr[45][44] = 107.5
        arr[43][46] = arr[46][43] = 21.44
        arr[46][47] = arr[47][46] = 42.57
        arr[47][48] = arr[48][47] = 70.58
        arr[48][49] = arr[49][48] = 80.8
        arr[50][51] = arr[51][50] = 35.61
        arr[51][52] = arr[52][51] = 71.84
        arr[51][53] = arr[53][51] = 116.43
        arr[53][54] = arr[54][53] = 71.52
        arr[54][55] = arr[55][54] = 22.64
        arr[54][57] = arr[57][54] = 22.08
        arr[55][56] = arr[56][55] = 36.26
        arr[56][57] = arr[57][56] = 20.96
        arr[56][58] = arr[58][56] = 23.17
        arr[58][59] = arr[59][58] = 36.25
        arr[59][60] = arr[60][59] = 31.6
        arr[59][61] = arr[61][59] = 21.31
        arr[60][62] = arr[62][60] = 36.67
        arr[61][62] = arr[62][61] = 15.23

        self.data = arr

class Graph:
    all_nodes = []
    lookup_table = None

    def __init__(self):
        # Populate nodes
        self.defineNodes()

        # Populate arcs
        self.lookup_table = Lookup_Table()

    # Given the id of a node, return the Node object
    def get_node_by_id(self, id)  -> Node:
        for index, node in enumerate(self.all_nodes):
            if node.get_id() == id:
                return self.all_nodes[index]
            
    def get_node_by_name(self, name) -> Node:
        for index, node in enumerate(self.all_nodes):
            if node.get_name() == name:
                return self.all_nodes[index]

    ### SO! You might be wondering why I have brought defineNodes() into an object
    # It was mainly because I wanted a convenient grouping between the lookup table andd
    #   our data on the nodes and their positions. This should make our life easier.
    # Conceptually, a graph contains both nodes and arcs. So this is bringing them together.
    def defineNodes(self):
        self.all_nodes.append(Node("CLE", 0, (48.46385902698279, -123.31022982698542)))
        self.all_nodes.append(Node("DTB", 1, (48.465078386216554, -123.31387649906908)))
        self.all_nodes.append(Node("ECS", 2, (48.46113617040822, -123.31144840329222)))
        self.all_nodes.append(Node("A", 3, (48.46137123703085, -123.31186238839109)))
        self.all_nodes.append(Node("B", 4, (48.46144238255688, -123.31297282285963)))
        self.all_nodes.append(Node("C", 5, (48.46203288657421, -123.31309620446726)))
        self.all_nodes.append(Node("D", 6, (48.46231795765519, -123.31314127534513)))
        self.all_nodes.append(Node("E", 7, (48.462662522603, -123.31321083409442)))
        self.all_nodes.append(Node("F", 8, (48.46342610204105, -123.31340018103346)))
        self.all_nodes.append(Node("G", 9, (48.46358150936804, -123.31345705671202)))
        self.all_nodes.append(Node("H", 10, (48.46357605432841, -123.31369001219407)))
        self.all_nodes.append(Node("I", 11, (48.46338572867817, -123.31368937765774)))
        self.all_nodes.append(Node("J", 12, (48.463692981969224, -123.31369478087726)))
        self.all_nodes.append(Node("K", 13, (48.46388032081692, -123.31373454713497)))
        self.all_nodes.append(Node("L", 14, (48.46415135200406, -123.31375764767687)))
        self.all_nodes.append(Node("M", 15, (48.46434007846103, -123.3137951796987)))
        self.all_nodes.append(Node("N", 16, (48.46452050859181, -123.31380143503718)))
        self.all_nodes.append(Node("O", 17, (48.46409494297565, -123.31392991258758)))
        self.all_nodes.append(Node("P", 18, (48.46425459828522, -123.31401192394024)))
        self.all_nodes.append(Node("Q", 19, (48.465043410178254, -123.31316249107589)))
        self.all_nodes.append(Node("R", 20, (48.46506586485167, -123.31268500347667)))
        self.all_nodes.append(Node("S", 21, (48.46463024241453, -123.31258679680732)))
        self.all_nodes.append(Node("T", 22, (48.46488847266101, -123.31293221336846)))
        self.all_nodes.append(Node("U", 23, (48.46466593363721, -123.31290932401616)))
        self.all_nodes.append(Node("V", 24, (48.464576424708596, -123.31319310804354)))
        self.all_nodes.append(Node("W", 25, (48.464563639242705, -123.31274859056202)))
        self.all_nodes.append(Node("X", 26, (48.46457441303656, -123.31243265661517)))
        self.all_nodes.append(Node("Y", 27, (48.4644391418955, -123.31239654987678)))
        self.all_nodes.append(Node("Z", 28, (48.46413511942271, -123.31233815143615)))
        self.all_nodes.append(Node("AA", 29, (48.46422774284721, -123.31197756936676)))
        self.all_nodes.append(Node("AB", 30, (48.46423205090937, -123.31169170250094)))
        self.all_nodes.append(Node("AC", 31, (48.464492687988674, -123.31129213858618)))
        self.all_nodes.append(Node("AD", 32, (48.46412865731801, -123.31123691430398)))
        self.all_nodes.append(Node("AE", 33, (48.46382278337691, -123.31114920516384)))
        self.all_nodes.append(Node("AF", 34, (48.46372154300355, -123.31229592111427)))
        self.all_nodes.append(Node("AG", 35, (48.463836849996845, -123.31088451782277)))
        self.all_nodes.append(Node("AH", 36, (48.46334867504509, -123.31012884636613)))
        self.all_nodes.append(Node("AI", 37, (48.46292716358054, -123.31003749311604)))
        self.all_nodes.append(Node("AJ", 38, (48.46330324283998, -123.31078354465832)))
        self.all_nodes.append(Node("AK", 39, (48.4628438704791, -123.31067696586706)))
        self.all_nodes.append(Node("AL", 40, (48.46281105800872, -123.3108178021276)))
        self.all_nodes.append(Node("AM", 41, (48.462793389746636, -123.31120985982585)))
        self.all_nodes.append(Node("AN", 42, (48.46278393628378, -123.31165050880267)))
        self.all_nodes.append(Node("AO", 43, (48.46275083181234, -123.3121365664517)))
        self.all_nodes.append(Node("AP", 44, (48.46272275869386, -123.31272464719247)))
        self.all_nodes.append(Node("AQ", 45, (48.46366275140987, -123.31295712882488)))
        self.all_nodes.append(Node("AR", 46, (48.462567810094974, -123.31210582935589)))
        self.all_nodes.append(Node("AS", 47, (48.46269810095332, -123.31154444355855)))
        self.all_nodes.append(Node("AT", 48, (48.462325840470754, -123.3107725380872)))
        self.all_nodes.append(Node("AU", 49, (48.46150632099027, -123.3106693138996)))
        self.all_nodes.append(Node("AV", 50, (48.46301805525083, -123.30946674285744)))
        self.all_nodes.append(Node("AW", 51, (48.46308858471603, -123.30900938287407)))
        self.all_nodes.append(Node("AX", 52, (48.463162640549, -123.30805211779263)))
        self.all_nodes.append(Node("AY", 53, (48.46389261369236, -123.30823293453025)))
        self.all_nodes.append(Node("AZ", 54, (48.463870761236706, -123.30917892832963)))
        self.all_nodes.append(Node("BA", 55, (48.463848635842865, -123.30949257803245)))
        self.all_nodes.append(Node("BB", 56, (48.46418642357976, -123.3095243371507)))
        self.all_nodes.append(Node("BC", 57, (48.46415501347602, -123.30925591044864)))
        self.all_nodes.append(Node("BD", 58, (48.46438079469843, -123.30956096408622)))
        self.all_nodes.append(Node("BE", 59, (48.46462181947507, -123.30923451194397)))
        self.all_nodes.append(Node("BF", 60, (48.46486004224007, -123.30898709747622)))
        self.all_nodes.append(Node("BG", 61, (48.46467021176951, -123.30950944335464)))
        self.all_nodes.append(Node("BH", 62, (48.46480296576786, -123.3095157545876)))

# This l'il guy is alllll of our data, in one convenient package!
topography = Graph()

""" Debug code """

# print("Row 3 of topography:", topography.lookup_table.data[3])

# test_node = Node("I", 11, (48.46338572867817, -123.31368937765774))
# print("" + str(test_node.get_neighbours()))

# print(topography.get_node_by_id(11).name, "= I?")

# dtb = topography.get_node_by_name("DTB")
# ecs = topography.get_node_by_name("ECS")

# ecs.get_neighbours()
# print("")
# print(topography.lookup_table.data[2])

# print(ecs.get_neighbours())
