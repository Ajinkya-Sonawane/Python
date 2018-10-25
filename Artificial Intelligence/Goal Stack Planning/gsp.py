class GSP:
    def __init__(self):
        self.start = []
        self.goal = []
        self.stack = []
        self.actions = ['Stack','UnStack','Pick','Put']
        self.predicate = ['On','OnTable']
        self.prereq = ['Clear','Holding','ArmEmpty']

    def accept(self):
        self.start = input("Enter Start state : ").split("^")
        self.goal = input("Enter Goal state : ").split("^")

    def contains(self,l1,l2,x):
        if x in l2:
            return True
        else:
            return False

    def break_compound(self,l1):
        for i in l1:
            self.stack.append(i)
        
    def process(self):
        self.accept()

        self.stack.append(goal)
        while len(self.stack) != 0:
            #Break compound clause onto stack
            if len(self.stack[-1]) > 1:
                break_compound(self.stack[-1])
                        
            
