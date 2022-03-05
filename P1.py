import queue
from typing import Dict, List

from queue import PriorityQueue
import copy
import heapq

class Node:
    box: List
    man: int
    goal: int
    def __init__(self, box, man, goal):
        self.box = box
        self.man = man
        self.goal = goal
        
    def __eq__(self, other):
        return (self.box == other.box) and (self.man == other.man) and (self.goal == other.goal)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.box < other.box) and (self.man < other.man) and (self.goal < other.goal)

    def __gt__(self, other):
        return (self.box > other.box) and (self.man > other.man) and (self.goal > other.goal)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)

class Queue:
    queue: List
    
    # Constructor
    def __init__(self):
        self.queue = []
    
    # Comparision operations
    def __eq__(self, other):
        return (self.table == other.table)

    def __ne__(self, other):
        return not (self.table == other.table)

    def __lt__(self, other):
        return (self.table < other.table)

    def __gt__(self, other):
        return (self.table > other.table)

    def __le__(self, other):
        return (self.table < other.table) or (self.table == other.table)

    def __ge__(self, other):
        return (self.table > other.table) or (self.table == other.table)
    
    # Appends then Sorts list from least to greatest
    def insert(self, node: Node):
        self.queue.append(node)
        self.queue.sort(key=lambda x:x.man+x.goal)
        
    # Returns and removes first element
    def pop(self):
        return self.queue.pop(0)
    
    # Returns i-th element in list
    # NOTE: does not remove  
    def at(self, i: int):
        return self.queue[i]
    
    # Prints Nodes in a Json like format
    def print_node(self,i: int):
        print("%s: {"%(i))
        print("\tbox: ",end='')
        print(self.queue[i].box)
        print("\tman: %s,\n\tgoal: %s\n}"%(self.queue[i].man,self.queue[i].goal))
    
    # Prints all nodes in queue
    def print_queue(self):
        for i in range(len(self.queue)):
            self.print_node(i)

class HashTable:
    table: Dict
    
    # Constructor
    def __init__(self):
        self.table = {}
    
    # Comparision operations
    def __eq__(self, other):
        return (self.table == other.table)

    def __ne__(self, other):
        return not (self.table == other.table)

    def __lt__(self, other):
        return (self.table < other.table)

    def __gt__(self, other):
        return (self.table > other.table)

    def __le__(self, other):
        return (self.table < other.table) or (self.table == other.table)

    def __ge__(self, other):
        return (self.table > other.table) or (self.table == other.table)
    
    def append_hash(self, node: Node):
        self.table[hash(chr(len(self.table)))] = node
        
    def at(self, i: int):
        return self.table[hash(chr(i))]

q = Queue()

goal = [
    [1,2,3],
    [8,0,4],
    [7,6,5]
]

initial = [
    [2,8,3],
    [6,7,4],
    [1,5,0]
]

# Test Data

# q.insert(Node([
#      [2,8,3],
#      [6,7,4],
#      [1,0,5]
#  ],18,2))

# q.insert(Node([
#      [2,8,3],
#      [6,0,4],
#      [1,7,5]
#  ],14,5))

# q.insert(Node([
#      [2,8,3],
#      [0,6,4],
#      [1,7,5]
#  ],14,7))

# print(q.pop())

# q.print_queue()

# Hash Table Test Data

# ht = HashTable()

# ht.append_hash(q.queue[0])

# ht.append_hash(q.queue[1])

# def insert(node: Node, q: PriorityQueue):
#     total = node.goal + node.man
#     temp1: Node
#     temp2: Node
#     flag = True 
#     i = 0

#     if(q.empty()):
#         q.put(node)
#     elif(q.queue[len(q.queue)-1].man+q.queue[len(q.queue)-1].goal <= total):
#         q.put(node)
#     else:
#         while(i < len(q.queue) and flag):
#             if(total < q.queue[i].goal+q.queue[i].man):
#                 flag = False
#                 temp1 = q.queue[i]
#                 q.queue[i] = node
#                 for j in range(i+1,len(q.queue)):
#                     temp2 = q.queue[j]
#                     q.queue[j] = temp1
#                     temp1 = temp2
#                 q.put(temp1)
#             elif(total == q.queue[i].goal+q.queue[i].man):
#                 for j in range(i+1,len(q.queue)):
#                     if (total != q.queue[j].goal+q.queue[j].man):
#                         flag = False
#                         temp1 = q.queue[j]
#                         q.queue[j] = node
#                         for k in range(j+1,len(q.queue)):
#                             temp2 = q.queue[k]
#                             q.queue[k] = temp1
#                             temp1 = temp2
#                         q.put(temp1)
#                         break

#             i+=1

def print_matrix(l):
    print(f"{l[0]} {l[1]} {l[2]}")
    print(f"{l[3]} {l[4]} {l[5]}")
    print(f"{l[6]} {l[7]} {l[8]}")
    print("-----")
    print("8 | 9")
    print("-----")
    print(" #0")

def f(l, num):
    for i in range(len(l)):
        ex = True
        try:
            temp = l[i].index(num)
        except ValueError:
            ex = False
        
        if(ex == True):
            return [i,temp]

def calculate_manhatten_distance(goal_index, initial_index):
    d = 0
    if(initial_index[0] > goal_index[0]):
        d += initial_index[0] - goal_index[0]
    elif(initial_index[0] < goal_index[0]):
        d += (goal_index[0] - initial_index[0])*3
    
    if(initial_index[1] > goal_index[1]):
        d += (initial_index[1] - goal_index[1])*2
    elif(initial_index[1] < goal_index[1]):
        d += (goal_index[1] - initial_index[1])*2

    return d

def swapPositions(list, pos1, pos2):
    position1a = pos1[0]
    position1b = pos1[1]
    position2a = pos2[0]
    position2b = pos2[1]
    list[position1a][position1b], list[position2a][position2b] = list[position2a][position2b], list[position1a][position1b]
    return list

ht = HashTable()



q.insert(Node(initial,21,0))
k = 0
temp_list = []
while(k < 12):
    cost1 = q.queue[0].goal
    cost2 = q.queue[0].goal
    cost3 = q.queue[0].goal
    initial_Index = f(q.queue[0].box,0)
    goal_Index = f(goal,0)
    if (initial_Index == [2,2]):
        temp_list = copy.deepcopy(q.queue[0].box)
        temp_list2 = copy.deepcopy(q.queue[0].box)
        manDist = 0
        temp_list = copy.deepcopy(swapPositions(temp_list[:],initial_Index,[2,1]))
        cost1 += 2
        ht.append_hash(q.queue[0])
        q.pop()
        for i in range(1, 9):
            temp_Index = f(temp_list,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list,manDist,cost1))

        temp_list2 = copy.deepcopy(swapPositions(temp_list2[:],initial_Index,[1,2]))[:]
        cost2 += 3
        manDist = 0
        for i in range(1, 9):
            temp_Index = f(temp_list2,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list2,manDist,cost2))
    elif (initial_Index == [2,1]):
        temp_list = copy.deepcopy(q.queue[0].box)
        temp_list2 = copy.deepcopy(q.queue[0].box)
        manDist = 0
        temp_list = copy.deepcopy(swapPositions(temp_list[:],initial_Index,[2,0]))
        cost1 += 2
        # ht.append_hash(Node(q.queue[0].box,q.queue[0].man,q.queue[0].goal))
        ht.append_hash(q.queue[0])
        q.pop()
        for i in range(1, 9):
            temp_Index = f(temp_list,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)

        q.insert(Node(temp_list,manDist,cost1))

        manDist = 0
        temp_list2 = copy.deepcopy(swapPositions(temp_list2[:],initial_Index,[1,1]))
        cost2 += 3
        for i in range(1, 9):
            temp_Index = f(temp_list2,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list2,manDist,cost2))
    elif (initial_Index == [1,1]):
        temp_list = copy.deepcopy(q.queue[0].box)
        temp_list2 = copy.deepcopy(q.queue[0].box)
        temp_list3 = copy.deepcopy(q.queue[0].box)
        manDist = 0
        temp_list = copy.deepcopy(swapPositions(temp_list[:],initial_Index,[1,0]))
        cost1 += 2
        ht.append_hash(q.queue[0])
        q.pop()
        for i in range(1, 9):
            temp_Index = f(temp_list,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list,manDist,cost1))

        manDist = 0
        temp_list2 = copy.deepcopy(swapPositions(temp_list2[:],initial_Index,[0,1]))
        cost2 += 3
        for i in range(1, 9):
            temp_Index = f(temp_list2,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list2,manDist,cost2))
        manDist = 0
        temp_list3 = copy.deepcopy(swapPositions(temp_list3[:],initial_Index,[1,2]))
        cost3 += 2
        for i in range(1, 9):
            temp_Index = f(temp_list3,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list3,manDist,cost3))
    elif (initial_Index == [1,0]):
        temp_list = copy.deepcopy(q.queue[0].box)
        temp_list2 = copy.deepcopy(q.queue[0].box)
        temp_list3 = copy.deepcopy(q.queue[0].box)
        manDist = 0
        temp_list = copy.deepcopy(swapPositions(temp_list[:],initial_Index,[0,0]))
        cost1 += 3
        ht.append_hash(q.queue[0])
        q.pop()
        for i in range(1, 9):
            temp_Index = f(temp_list,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list,manDist,cost1))

        manDist = 0
        temp_list2 = copy.deepcopy(swapPositions(temp_list2[:],initial_Index,[1,1]))
        cost2 += 2
        for i in range(1, 9):
            temp_Index = f(temp_list2,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list2,manDist,cost2))

        manDist = 0
        temp_list3 = copy.deepcopy(swapPositions(temp_list3[:],initial_Index,[2,0]))
        cost3 += 1
        for i in range(1, 9):
            temp_Index = f(temp_list3,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list3,manDist,cost3))
    elif (initial_Index == [0,1]):
        temp_list = copy.deepcopy(q.queue[0].box)
        temp_list2 = copy.deepcopy(q.queue[0].box)
        temp_list3 = copy.deepcopy(q.queue[0].box)
        manDist = 0
        temp_list = copy.deepcopy(swapPositions(temp_list[:],initial_Index,[0,0]))
        cost1 += 2
        ht.append_hash(q.queue[0])
        q.pop()
        for i in range(1, 9):
            temp_Index = f(temp_list,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list,manDist,cost1))

        manDist = 0
        temp_list3 = copy.deepcopy(swapPositions(temp_list3[:],initial_Index,[0,2]))
        cost3 += 2
        for i in range(1, 9):
            temp_Index = f(temp_list3,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list3,manDist,cost3))
    elif (initial_Index == [2,0]):
        temp_list = copy.deepcopy(q.queue[0].box)
        temp_list2 = copy.deepcopy(q.queue[0].box)
        temp_list3 = copy.deepcopy(q.queue[0].box)
        manDist = 0
        temp_list = copy.deepcopy(swapPositions(temp_list[:],initial_Index,[2,1]))
        cost1 += 2
        ht.append_hash(q.queue[0])
        q.pop()
        for i in range(1, 9):
            temp_Index = f(temp_list,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list,manDist,cost1))
    elif (initial_Index == [0,0]):
        temp_list = copy.deepcopy(q.queue[0].box)
        temp_list2 = copy.deepcopy(q.queue[0].box)
        temp_list3 = copy.deepcopy(q.queue[0].box)
        manDist = 0
        temp_list = copy.deepcopy(swapPositions(temp_list[:],initial_Index,[1,0]))
        cost1 += 1
        ht.append_hash(q.queue[0])
        q.pop()
        for i in range(1, 9):
            temp_Index = f(temp_list,i)
            goal_Index = f(goal,i)
            manDist += calculate_manhatten_distance(goal_Index, temp_Index)
        q.insert(Node(temp_list,manDist,cost1))
    
        
    k += 1
ht.append_hash(q.queue[0])
q.pop()

for i in range(len(ht.table)):
    print(ht.at(i).box[0])
    print(ht.at(i).box[1])
    print(ht.at(i).box[2])
    print("---------")
    print(ht.at(i).goal,"\t  ",ht.at(i).man)
    print("  #",i+1)
    print()
    print()



