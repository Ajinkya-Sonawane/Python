#Implementing basic data structures in Python - LinkedList
class Node:
  
  def __init__(self,value):
    self.value = value
    self.nextNode = None

class LinkedList:

  def __init__(self):
    self.headNode = None
    self.lastNode = None

  def insertNode(self,value):
    node = Node(value)
    if self.headNode == None:
      self.headNode = node
      self.lastNode = node
    else:
      self.lastNode.nextNode = node
      self.lastNode = node

  def insertNodeAfter(self,value,refValue):
    node = Node(value)
    if self.headNode == None:
      self.headNode = node
      self.lastNode = node
    else:
      iterator = self.headNode
      while iterator.value != refValue:
        iterator = iterator.nextNode
      node.nextNode = iterator.nextNode
      iterator.nextNode = node

  def traverseList(self):
    iterator = self.headNode
    while iterator != None:
      print(iterator.value)
      iterator = iterator.nextNode

  def deleteNode(self,value):
    iterator = self.headNode
    while iterator.nextNode.value != value:
      iterator = iterator.nextNode
    temp = iterator.nextNode
    iterator.nextNode = temp.nextNode
    del(temp)
    print(value,' deleted successfully')

ll = LinkedList()
ll.insertNode(1)
ll.insertNode(2)
ll.insertNode(3)
ll.traverseList()
ll.deleteNode(2)
ll.traverseList()
ll.insertNodeAfter(2,1)
ll.traverseList()








#Implementing basic data structures in Python - Stack
class Stack:

  def __init__(self):
    self.top = -1
    self.data = []

  def push(self,value):
    print(value,' pushed successfully' )    
    self.data.append(value)
    self.top +=1 
  
  def pop(self):
    if self.top == -1:
        print('Stack is empty')        
        return 
    print(self.data[self.top],' popped successfully')
    del self.data[self.top]
    self.top -= 1

  def printStack(self):
    print('Stack : ',self.data)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(2)
stack.printStack()
stack.pop()
stack.printStack()



class Queue:

    def __init__(self):
        self.front = -1
        self.end =  -1
        self.data = []
    
    def enqueue(self,value):
        print(value,' enqueued successfully')
        self.front = 0
        self.end += 1
        self.data.insert(self.front,value)
    
    def dequeue(self):
        if self.end == -1:
            print('Queue is empty')        
            return
        print(self.data[-1],' dequeued successfully')
        del self.data[self.end] 
        self.end -= 1

    def printQueue(self):
        print('Queue : ',self.data)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.printQueue()
queue.dequeue()
queue.printQueue()
