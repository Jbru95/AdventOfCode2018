class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
 
 
class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None
 
    def get_node(self, index):
        current = self.first
        for i in range(index):
            current = current.next
            #if current == self.first:
            #    return None
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        self.insert_after(ref_node.prev, new_node)
 
    def insert_at_end(self, new_node):

        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)
 
    def insert_at_beg(self, new_node):
        self.insert_at_end(new_node)
        self.first = new_node
 
    def remove(self, node):
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next
 
    def display(self):
        if self.first is None:
            return
        current = self.first
        while True:
            print(current.data, end = ' ')
            current = current.next
            if current == self.first:
                break
 
fp = open('test_input.txt', 'r')
inp_list = fp.read().strip().split()
fp.close()

player_num = int(inp_list[0])
last_marble_value = int(inp_list[6])

marble_circle = CircularDoublyLinkedList()
marble_circle.insert_at_beg(Node(0))

player_score_array = []
current_marble_index = 0
current_marble = marble_circle.first
node1 = Node(1)
marble_circle.insert_after(marble_circle.get_node(0), node1)
current_marble = node1


for i in range(player_num):
    player_score_array.append(0)

#print(player_score_array)

for i in range(2, last_marble_value + 1):
    if (i % 23 != 0):
        marble_circle.insert_after(current_marble.next, Node(i))
        #print(current_marble_index + 2)
        current_marble = current_marble.next.next
        #print(marble_circle)

    else: 
        #print("current index: ", current_marble_index)
        current_marble = current_marble.prev.prev.prev.prev.prev.prev.prev
        player_score_array[(i%player_num)] += current_marble.data
        player_score_array[(i%player_num)] += i

        temp_marb = current_marble.next
        marble_circle.remove(current_marble)
        current_marble = temp_marb

        #current_marble_index = current_marble_index - 7 current_marble
        


player_score_array.sort()
print(player_score_array)

#PART 2 VERY VERY VERY SLOW, NEED 0(1) INSERTION, DOUBLY LINKED LIST WOULD BE IDEAL

