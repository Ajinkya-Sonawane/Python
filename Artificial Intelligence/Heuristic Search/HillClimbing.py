from Graph import Graph,Node

class HC:
    def __init__(self):
        """ Accept the grpah using the Graph Module and initialize the required lists """
        self.graph = Graph()
        self.graph.accept()
        """ list of nodes """
        self.nodes = [Node(i) for i in range(0,self.graph.total_nodes)]
        self.open = []      #To keep track of expanded nodes
        self.closed = []    #To keep track of visited nodes
        self.in_open = [0]*self.graph.total_nodes #To keep track of nodes already present in open list
    
    def process(self):
        try:
            start,goal = map(int,input("Enter start and goal nodes : ").split(" "))
            if start < 0 or start >= self.graph.total_nodes or goal < 0 or goal >= self.graph.total_nodes:
                raise Exception("Invalid start or goal node")

            self.open.append(self.nodes[start]) #Push start node in open list
            self.in_open[start] = 1     #Mark start node as already in open list
            while True:
                cur = self.open[0]  #Take the first node in open list which is usually the best node
                self.closed.append(cur) #Push this node in closed list
                if cur.val == goal: #If it is the goal node then stop 
                    break
                #Expand the current node                
                children = self.graph.generate_child(self.in_open,self.nodes,cur.val)

                #Find the best child based on the heuristic value 
                children.sort(key = lambda x:x.h,reverse=False)

                #Store the best child
                best_child = children[0]

                #Put the best child in open list
                self.open.append(best_child)

                #Mark that the child is in open list
                self.in_open[best_child.val] = 1

                #Delete the current node from open list
                del self.open[0]

            #Print the path to the goal node
            self.graph.print_path(self.closed)
        except Exception as msg:
            print(msg)
                    

a = HC()
a.process()
