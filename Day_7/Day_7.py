'''
DAG -> kinda breadth first search
'''

class DAG:

    def __init__(self):
        self.node_dict = {}
        self.startingNode = None

    def __repr__(self):
        
        for elem in self.node_dict.values():
            print(elem)
        print("Base Node: " + self.startingNode.letter)
        return "end"

    def addNodetoDAG(self, nodeLetter, pointsToNodeLetter = None):
        if nodeLetter not in self.node_dict:
            newNode = Node(nodeLetter)
            self.node_dict[nodeLetter] = newNode

        if pointsToNodeLetter != None:
            if pointsToNodeLetter not in self.node_dict:
                newNode2 = Node(pointsToNodeLetter)
                self.node_dict[pointsToNodeLetter] = newNode2
            
            self.node_dict[nodeLetter].point_to(self.node_dict[pointsToNodeLetter])

    def setStartNode(self, startingLetter):
        self.startingNode = self.node_dict[startingLetter]


class Node:
    
    def __init__(self, letter):
        self.letter = letter
        self.pointer_array = []

    def point_to(self, node):
        self.pointer_array.append(node)

    def __repr__(self):
        ret_str = self.letter + " points to -> "
        for node in self.pointer_array:
            ret_str += node.letter + ", "

        return ret_str
        


dag = DAG()

fp = open('input.txt', 'r')

for line in fp.readlines():
    line_ary = line.split()

    end_node_letter = line_ary[1]
    start_node_letter = line_ary[7]

    dag.addNodetoDAG(start_node_letter, end_node_letter)
    print(end_node_letter, start_node_letter)


letter_set = set()
for Node in dag.node_dict.values():
    for Node2 in Node.pointer_array:
        letter_set.add(Node2.letter)

#print(letter_set) #Z starts the DAG

dag.setStartNode("Z")

print(dag)
