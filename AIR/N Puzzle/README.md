# N Puzzle Problem using A* Algorithm

1. <b>What is N Puzzle Problem ?</b> <br>
    * N-Puzzle or sliding puzzle is a popular puzzle that consists of N tiles where N can be 8, 15, 24 and so on. The puzzle is divided into v(N+1) rows and v(N+1) columns eg. 15-Puzzle will have 4 rows and 4 columns, an 8-Puzzle will have 3 rows and 3 columns and so on. The puzzle consists of one empty space where the tiles can be moved and thus the puzzle is solved when a particular goal pattern is formed like the following is one of the variant goal pattern.
    <img src="npuzzle.png">

2. <b>What is A* Algorithm ?</b> <br>
    * A* is a computer algorithm that is widely used in pathfinding and graph traversal, the process of plotting an efficiently traversable path between multiple points, called nodes. Noted for its performance and accuracy, it enjoys widespread use.
    * It is one of the basic and the most common algorithm which you’ll see widely across the internet. It is widely used for pathfinding and various other problems which have admissible heuristics and can be converted to a graph form. 
    ### Working <br>
    * The key feature of the A* algorithm is that it keeps a track of each visited node which helps in ignoring the nodes that are already visited, saving a huge amount of time.It also has a list that holds all the nodes that are left to be explored and from this list it chooses the most optimal node thus saving time not exploring unnecessary or less optimal nodes.
    * So we use two lists namely ‘open list‘ and ‘closed list‘ the open list contains all the nodes that are being generated and are not existing in the closed list and each node explored after it’s neighboring nodes are discovered is put in the closed list and the neighbors are put in the open list this is how the nodes expand. Each node has a pointer to it’s parent so that at any given point it can retrace the path to the parent. Initially the open list holds the start(Initial) node. The next node chosen from the open list is based on it’s f score, the node with the least f score is picked up and explored.
    
    ##### What is f-score ?
    * f score is nothing but the sum of the cost to reach that node and the heuristic value of that node.<br>
    For any give node the f score is defined as : f(x)=h(x)+g(x) <br>
    where g(x)  is the cost of that node, h(x) is the calculated heuristic of that node and x is the current node.
    
    ##### What is g-score ?
    * g score is defined as the sum of g score of the parent node and the cost to travel to that node from it’s parent.
        <br>g(x)=g(x.parent)+cost(x.parent,x)
    
    ##### What is h-score ?
    * Heuristic score is different for each question as explained above heuristic needs to be admissible for each type of problem.
    * In our problem the h-score is the count of the misplaced elements in the current state that differ from the goal state.<br>
<hr>
<img src="puzzle1.png"><br>
<img src="puzzle2.png">
