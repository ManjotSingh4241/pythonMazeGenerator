# Members
# 1.Manjot Singh
# 2.Manak Preet Singh
# 3.Abhi

import random
from a3_partb import minimum_spanning_tree
from a2d import Graph

def generate_maze(number_of_rows, number_of_columns):
    
    boundary = []
    
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            blocks = j + i * number_of_columns
            while True:
                while True:
                    while i == number_of_rows - 1:
                        break
                    while i != number_of_rows - 1:
                        boundary.append((blocks, number_of_columns + blocks))
                        break
                    while j == number_of_columns - 1:
                        break
                    while j != number_of_columns - 1:
                        boundary.append((blocks, blocks + 1))
                        break
                    break
                break
            
    visual = Graph(number_of_columns * number_of_rows)
    
    for k in boundary:
        randm = random.choice(range(1, 51))
        visual.add_edge(k[1], k[0], randm)
        visual.add_edge(k[0], k[1], randm)

    tree_a1 = minimum_spanning_tree(visual)

    mboundary = list(filter(lambda k: (k[1], k[0]) not in tree_a1 and k not in tree_a1, boundary))
    
    return mboundary
