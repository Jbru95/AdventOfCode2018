class Tree:
    def __init__(self, input_list):
        self.node_dict = {}
        self.input_list = input_list
        self.input_index = 0

    def __repr__(self): 

    def fill_tree_from_input():

        node = node(self.input_list[self.input_index], self.input_list[self.input_index])
        self.input_index += 1


        



class Node:
    def __init__(self, childNum, metaNum):
        self.child_node_num = childNum
        self.meta_data_num = metaNum
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



    




fp = open('test_input.txt', 'r')
for line in fp.readlines():
    node_tree = Tree(line.strip().split(' '))
fp.close()


print(node_tree.input_list)





