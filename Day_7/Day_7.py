'''
DAG -> kinda breadth first search
'''

class DAG:

    def __init__(self):
        self.node_dict = {}
        self.startingNode = None
        self.letterStack = []

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

    def alphabetic_order_traversal(self):

        self.letterStack.append(self.startingNode.letter)
        traversal_string = ""

        while len(self.letterStack) > 0:
            lowest_letter = self.pop_lowest_letter_with_completed_prereqs(traversal_string)
            traversal_string += lowest_letter
            #self.letterStack.extend(self.node_dict[lowest_letter].pointer_array)
            for node in self.node_dict[lowest_letter].pointer_array:
                if node.letter not in self.letterStack:
                    self.letterStack.append(node.letter)
            print(self.letterStack)
            print(traversal_string)

        return traversal_string

    def pop_lowest_letter_with_completed_prereqs(self, traversal_string):
        if len(self.letterStack) > 0:
            lowest_letter = self.letterStack[0]
        else:
            return None

        for letter in self.letterStack:
            prereqs_finised = True

            for node in self.node_dict[letter].points_from_array:
                if node.letter not in traversal_string:
                    prereqs_finised = False

            if letter < lowest_letter and prereqs_finised == True :
                lowest_letter = letter
        
        return self.letterStack.pop(self.letterStack.index(lowest_letter))

class Node:
    
    def __init__(self, letter):
        self.letter = letter
        self.pointer_array = []
        self.points_from_array = []

    def point_to(self, node):
        self.pointer_array.append(node)
        node.points_from_array.append(self)

    def __repr__(self):
        ret_str = self.letter + " points to -> "
        for node in self.pointer_array:
            ret_str += node.letter + ", "

        return ret_str
        


dag = DAG()

fp = open('input.txt', 'r')

for line in fp.readlines():
    line_ary = line.split()

    start_node_letter = line_ary[1]
    end_node_letter = line_ary[7]

    dag.addNodetoDAG(start_node_letter, end_node_letter)
    print(end_node_letter, start_node_letter)


letter_set = set()
for Node in dag.node_dict.values():
    for Node2 in Node.pointer_array:
        letter_set.add(Node2.letter)

print(letter_set) #Z starts the DAG

dag.setStartNode("G")

print(dag)

traversal_order = dag.alphabetic_order_traversal()

print(traversal_order)

