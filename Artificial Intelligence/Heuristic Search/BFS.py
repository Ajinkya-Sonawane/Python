from Graph import Graph,Node

class BFS:
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
                #Expand the current node and push it's children in open list                
                for i in self.graph.generate_child(self.in_open,self.nodes,cur.val):
                    self.open.append(i)
                    self.in_open[i.val] = 1   #Mark the child nodes as present in open list     
                del self.open[0]    #Remove the current node from open list

                """ Sort the open list to get the best node at the first position
                    here the hueristic value is used to find the best node
                    h(x) = x.h """                
                self.open.sort(key = lambda x:x.h,reverse=False)

            #Print the path to the goal node
            self.graph.print_path(self.closed)
        except Exception as msg:
            print(msg)
                    

a = BFS()
a.process()
