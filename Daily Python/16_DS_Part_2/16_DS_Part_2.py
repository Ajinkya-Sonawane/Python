class Graph:

    def __init__(self,totalNodes):
        self.totalNodes = totalNodes
        self.adjMatrix = []
        self.adjList = []

    def acceptAdjMatrix(self):
        print('The total number of nodes : ',self.totalNodes)
        for row in range(self.totalNodes):
            temp = list(map(int,input('Enter Row ' +str(row)+\
                ' of matrix : ').split(' ')))
            self.adjMatrix.append(temp)
        
    def printAdjMatrix(self):
        if len(self.adjMatrix) == 0:
            print('Please fill the Adjacency Matrix')
            return 
        print('Given Adjacency Matrix :')
        for row in self.adjMatrix:
            print(row)        

    def acceptAdjList(self):
        print('The total number of nodes : ',self.totalNodes)
        print('Nodes : ',list(range(self.totalNodes)))
        for node in range(self.totalNodes):
            temp = list(map(int,input('Enter Adjacent Nodes of Node' +\
                str(node)+' : ').split(' ')))
            self.adjList.append(temp)

    def printAdjList(self):
        if len(self.adjList) == 0:
            print('Please fill the Adjacency List')
            return
        print('\n\nGiven Adjacency List :')
        for i in range(self.totalNodes):
            print(i,end='--> ')
            for j in self.adjList[i]:
                print(j,end=' ')        
            print('')
    
    def BFS(self):
        print('\n\nBreadth First Search Traversal : ',end=' ')
        iterator = 0
        queue = [iterator]
        visited = [0]*self.totalNodes
        visited[iterator] = 1
        while len(queue)>0:
            queue.extend([ node for node in self.adjList[iterator] \
                if visited[node] != 1 and node not in queue])
            print(queue[0],end=' ')
            visited[iterator] = 1
            iterator = queue[0]           
            queue = queue[1:]
        print('')

graph = Graph(5)
graph.acceptAdjMatrix()
graph.printAdjMatrix()
graph.acceptAdjList()
graph.printAdjList()
graph.BFS()


class Node:
  
  def __init__(self,value):
    self.value = value
    self.rightNode = None
    self.leftNode = None
  
class BSTree:

  def __init__(self):
    self.headNode = None

  def insertNode(self,value):
    node = Node(value)
    if self.headNode == None:
      self.headNode = node
      print(value,' inserted successfully')

    else:
      iterator = self.headNode
      while True:
        if value < iterator.value:
          if iterator.leftNode == None:
            iterator.leftNode = node
            break
          else:
            iterator = iterator.leftNode
        else:
          if iterator.rightNode == None:
            iterator.rightNode = node
            break
          else:
            iterator = iterator.rightNode
      print(value,' inserted successfully')

  def printTree(self):
    print('\n\nPreOrder Traversal (Root, Left, Right)')
    self.preOrder(self.headNode)
  
    print('\n\nInOrder Traversal (Left, Root, Right)')
    self.inOrder(self.headNode)
  
    print('\n\nPostOrder Traversal (Left, Right, Root)')
    self.postOrder(self.headNode)
  
  def inOrder(self,node):
    if node == None:
      return
    self.inOrder(node.leftNode)
    print(node.value, end=' ')
    self.inOrder(node.rightNode)

  def preOrder(self,node):
    if node == None:
      return
    print(node.value, end=' ')
    self.preOrder(node.leftNode)
    self.preOrder(node.rightNode)

  def postOrder(self,node):
    if node == None:
      return
    self.postOrder(node.leftNode)
    self.postOrder(node.rightNode)
    print(node.value, end=' ')    

tree = BSTree()
tree.insertNode(5)
tree.insertNode(3)
tree.insertNode(1)
tree.insertNode(4)
tree.insertNode(6)
tree.printTree()