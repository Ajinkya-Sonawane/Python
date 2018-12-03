#Author : Ajinkya Sonawane

def accept():
    temp = []
    for i in range(0,3):
        inp = input().split(' ')
        temp.append(inp)

    return temp

def f(start,goal,level):
    return h(start,goal) + (level+1)

def h(start,goal):
   count = 0
   for i in range(0,len(goal)):
       for j in range(0,len(goal)):
           if goal[i][j] != start[i][j] and goal[i][j] != '_' :
               count += 1
   return count

def copy(puz):
    temp = []
    for i in range(0,len(puz)):
        x = []
        for j in range(0,len(puz)):
            x.append(puz[i][j])
        temp.append(x)

    return temp


def shuffle(puz,x1,y1,x2,y2):
    puz = copy(puz)
    if x2 >= len(puz) or x2 < 0 or y2 >= len(puz) or y2 < 0:
        return None

    temp = puz[x1][y1]
    puz[x1][y1] = puz[x2][y2]
    puz[x2][y2] = temp

    return puz


def find(puz,char):
    for i in range(0,len(puz)):
        for j in range(0,len(puz)):
            if puz[i][j] == char:
                return i,j

def generate_child(puz):
    x,y = find(puz,'_')
    positions = [[x+1,y],
                 [x-1,y],
                 [x,y+1],
                 [x,y-1]]
    children = []

    for pos in positions:
        child = shuffle(puz,x,y,pos[0],pos[1])
        if child != None:
            children.append(child)

    return children


def present(ol,cl,child):
    for i in ol:
        if h(i['puz'],child) == 0:
            return True
    for i in cl:
        if h(i['puz'],child) == 0:
            return True

    return False

print('Enter the start configuration')
start = accept()
print('Enter the goal configuration')
goal = accept()

open_list = []
close_list = []

"""
f(n) = h(n) + g(n)
"""

open_list.append(
    {
        'id':0,
        'puz':start,
        'f':f(start,goal,-1),
        'g':0,
        'prev':None
    })
id = 0
while True:
    cur_node = open_list[0]
    if h(cur_node['puz'],goal) == 0:
        break
    
    children = generate_child(cur_node['puz'])

    for child in children:
        if not present(open_list,close_list,child):
            id += 1
            open_list.append({
                'id':id,
                'puz':child,
                'f':f(child,goal,cur_node['g']),
                'g':cur_node['g']+1,
                'prev':cur_node['id']
                })
            
    close_list.append(cur_node)
    del open_list[0]

    open_list.sort(key=lambda x:x['f'],reverse=False)

stack = []
stack.append(open_list[0])
close_list.reverse()
cur_id = open_list[0]['prev']
for i in close_list:
    if i['id'] == cur_id:
        stack.append(i)
        cur_id = i['prev']
