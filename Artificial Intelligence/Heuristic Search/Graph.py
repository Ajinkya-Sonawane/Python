class Graph:
    def __init__(self):
        self.total_nodes  = 0
        self.adj_mat = []

    def accept(self):
        """ To accept adjacencey matrix from user """
        self.total_nodes = int(input("Enter the total number of nodes : "))
        try:
            print("""\nEnter the adjacency matrix with heuristic values if edge is present,
                else 0 if not present """)
            for i in range(0,self.total_nodes):
                temp = input().split(" ")
                if len(temp) != self.total_nodes:
                    raise Exception("Ivalid number of inputs")
                temp = list(map(int,temp))
                self.adj_mat.append(temp)
        except Exception as msg:
            print(msg)

    def print_matrix(self):
        """ To print the adjecency matrix """
        for i in self.adj_mat:
            for j in i:
                print(j,end=" ")
            print("")

    def generate_child(self,in_open,nodes,cur):
        """ Function to generate child nodes from a given node """
        adj = []
        for i,h in enumerate(self.adj_mat[cur]):
            if h != 0 and in_open[i] !=1:
                nodes[i].prev = cur   #Store the parent
                nodes[i].h = h     #Store the heuristic value or 'h-score'
                adj.append(nodes[i])
        return adj

    def print_path(self,closed):
        """ Function to print the path to the node"""
        closed.reverse()   #reverse the closed list
        stack = []  #To store the nodes
        prev = closed[0].val   #Initialize prev with first value to start the traversal
        for i in closed:
            if prev == i.val:   #If current node is the parent of the prev node then push in stack
                stack += [i.val]
                prev = i.prev   #Store parent of current node in prev
        stack.reverse() #Reverse the stack to print the path
        print("\nPath to goal node : ",end=" ")
        end = " --> "
        for i in stack:
            if i == stack[-1]:
                end=" "
            print(i,end=end)

class Node:
    def __init__(self,val,h=0,prev=None,level=0):
        self.val = val
        self.h = h
        self.prev = prev
        self.level = level
    
