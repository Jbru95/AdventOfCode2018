'''
DAG -> kinda breadth first search
'''

class DAG:

    def __init__(self):
        self.node_dict = {}
        self.startingNodes = []
        self.letterStack = []
        self.availableWorkers = 5
        #self.availableWorkers = 2
        self.availableLetters = []
        self.workingNodes = []

    def __repr__(self):
        
        for elem in self.node_dict.values():
            print(elem)
        print("Base Nodes: ")
        for elem in self.startingNodes: 
            print(elem)
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
        self.startingNodes.append(self.node_dict[startingLetter])

    def alphabetic_order_traversal(self):

        for node in self.startingNodes:
            self.letterStack.append(node.letter)

        traversal_string = ""

        while len(self.letterStack) > 0:
            lowest_letter = self.pop_lowest_letter_with_completed_prereqs(traversal_string)
            traversal_string += lowest_letter
            #self.letterStack.extend(self.node_dict[lowest_letter].pointer_array)
            for node in self.node_dict[lowest_letter].pointer_array:
                if node.letter not in self.letterStack and node.letter not in traversal_string:
                    self.letterStack.append(node.letter)

        return traversal_string

    def pop_lowest_letter_with_completed_prereqs(self, traversal_string):
        if len(self.letterStack) > 0:
            lowest_letter = 'a'
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


    def time_traversal(self):
        traversal_string = ""

        for node in self.startingNodes:
            self.letterStack.append(node.letter)
            self.update_available_letters(traversal_string)

        total_seconds = 0

        while len(self.letterStack) > 0:
            print_str = ""
            for elem in self.workingNodes:
                print_str += elem.letter

            print(total_seconds, self.availableLetters, self.availableWorkers, print_str, " ", traversal_string)
            

            while( self.availableWorkers > 0 and len(self.availableLetters) > 0):
                
                    self.availableWorkers -= 1
                    self.workingNodes.append(self.node_dict[self.pop_lowest_available_letter()])
                    

            for workingNode in self.workingNodes:
                if workingNode.timeToFinish == 0:
                    traversal_string += workingNode.letter

                    for node in workingNode.pointer_array:
                        if node.letter not in self.letterStack and node.letter not in traversal_string:
                            self.letterStack.append(node.letter)
                    
                    self.letterStack.pop(self.letterStack.index(workingNode.letter))
                    self.workingNodes.pop(self.workingNodes.index(workingNode))
                    self.availableWorkers += 1

                else: 
                    workingNode.timeToFinish -= 1

            self.update_available_letters(traversal_string)
            while( self.availableWorkers > 0 and len(self.availableLetters) > 0):
                
                    self.availableWorkers -= 1
                    self.workingNodes.append(self.node_dict[self.pop_lowest_available_letter()])
            total_seconds += 1


        print(traversal_string)
        return total_seconds

    
    def update_available_letters(self, traversal_string):
        for letter in self.letterStack:
            prereqs_finished = True

            for node in self.node_dict[letter].points_from_array:
                if node.letter not in traversal_string:
                    prereqs_finished = False
            
            if prereqs_finished == True and letter not in self.availableLetters and letter not in traversal_string and self.node_dict[letter] not in self.workingNodes:
                self.availableLetters.append(letter)

    def pop_lowest_available_letter(self):
        lowest_letter = 'a'
        for letter in self.availableLetters:
            if letter < lowest_letter:
                lowest_letter = letter
        
        return self.availableLetters.pop(self.availableLetters.index(lowest_letter))







class Node:
    
    def __init__(self, letter):
        self.letter = letter
        self.pointer_array = []
        self.points_from_array = []
        #self.timeToFinish = ord(letter) - 65
        self.timeToFinish = ord(letter) - 4

    def point_to(self, node):
        self.pointer_array.append(node)
        node.points_from_array.append(self)

    def __repr__(self):
        ret_str = self.letter + " points to -> "
        for node in self.pointer_array:
            ret_str += node.letter + ", "
        
        ret_str += ", has pointers from ->"
        for node in self.points_from_array:
            ret_str += node.letter + ", "

        ret_str += ". Time to Finish: " + str(self.timeToFinish)

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

dag.setStartNode("G") #TGKP could all start the DAG, the letter stack should start with these 4
dag.setStartNode("T")
dag.setStartNode("K")
dag.setStartNode("P")
#dag.setStartNode("C")

print(dag)

#traversal_order = dag.alphabetic_order_traversal()
#print(traversal_order)

time_traversal_seconds = dag.time_traversal()

print(time_traversal_seconds)
#guessed 939 and 938 and 937 and 936 and 935
