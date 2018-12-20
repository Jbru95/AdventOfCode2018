'''
DAG -> kinda breadth first search
'''

class DAG:

    def __init__(self):
        self.nodes = []
        


class Node:
    
    def __init__(self, letter):
        self.letter = letter
        self.pointer_array = []

    def point_to(self, node):
        self.pointer_array.append(node)


