class Tree:
    def __init__(self, input_list):
        self.node_dict = {}
        self.input_list = input_list
        self.input_index = 0
        self.height = 0
        self.root_node = None
        self.meta_data_total = 0
        self.fill_tree_from_input()

    def __repr__(self): 
        ret_str = "Tree: "
        ret_str += str(self.root_node)
        return ret_str

    def fill_tree_from_input(self):
        self.add_node(None, 0)

    def add_node(self, parent_node, start_index):
        add_node = Node(self.input_list[start_index], self.input_list[start_index + 1])
        start_index += 2

        if add_node.child_node_num == 0: #add node has no children, just add meta data and increment pointer index
            for i in range(add_node.meta_data_num):
                add_node.add_meta_data(self.input_list[start_index + i])
                #self.meta_data_total += int(self.input_list[start_index + i])
            start_index += add_node.meta_data_num

        else: #add node has children, add these nodes recursively calling add_node
            for i in range(add_node.child_node_num):
                start_index = self.add_node(add_node, start_index)
            
            for i in range(add_node.meta_data_num):
                add_node.add_meta_data(self.input_list[start_index + i])
                #self.meta_data_total += int(self.input_list[start_index + i])
            start_index += add_node.meta_data_num

        if (parent_node is not None):
            parent_node.children.append(add_node)
        else:
            self.root_node = add_node
        #print(add_node)

        return start_index

    def calculate_meta_data_total(self):
        self.add_meta_data(None)

    def add_meta_data(self, current_node):

        if current_node == None:
            current_node = self.root_node

        for num in current_node.meta_data:
            self.meta_data_total += int(num)

        for child_node in current_node.children:
            self.add_meta_data(child_node)




class Node:
    def __init__(self, childNum, metaNum):
        self.child_node_num = int(childNum)
        self.meta_data_num = int(metaNum)
        self.meta_data = []
        self.children = []
    
    def add_meta_data(self, meta_data): #adds meta data number(strs) to be added as meta data of this node, takes indiv strs or a list of strs
        if isinstance(meta_data, str):
            self.meta_data.append(meta_data)
        elif isinstance(meta_data, list):
            self.meta_data.extend(meta_data)

    def add_children(self, child_node): #adds Nodes to be children of this node, takes either individual nodes or a list of Nodes
        if isinstance(child_node, Node):
            self.children.append(child_node)
        elif isinstance(child_node, list):
            self.children.extend(child_node)

    def __str__(self):
        ret_str = "Meta Data: "
        for elem in self.meta_data:
            ret_str += str(elem) + ", "
        ret_str += " Children:[ "
        for child_node in self.children:
            ret_str += child_node.__str__()
        ret_str += "]"
        return ret_str


fp = open('input.txt', 'r')
for line in fp.readlines():
    node_tree = Tree(line.strip().split(' '))
fp.close()


print(node_tree.input_list)

print(node_tree)

node_tree.calculate_meta_data_total()

print(node_tree.meta_data_total)





