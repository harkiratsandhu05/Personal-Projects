class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if len(self.__items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.__items.pop(0)

    def peek(self):
        if len(self.__items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.__items[0]

    def isEmpty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

    def __str__(self):
        str_exp = ""
        for item in self.__items:
            str_exp += (str(item) + " ")
        return str_exp

    def __repr__(self):
        return str(self)

def createMaze1():
    maze = []
    maze.append(["#","#","#","#","#","O","#"])
    maze.append(["#"," "," "," ","#"," ","#"])
    maze.append(["#"," ","#"," ","#"," ","#"])
    maze.append(["#"," ","#"," "," "," ","#"])
    maze.append(["#"," ","#","#","#"," ","#"])
    maze.append(["#"," "," "," ","#"," ","#"])
    maze.append(["#","#","#","X","#","#","#"])
    return maze

def createMaze2():
    maze = []
    maze.append(["#","#","#","#","#","O","#"])
    maze.append(["#"," "," "," ","#"," ","#"])
    maze.append(["#"," ","#","#","#"," ","#"])
    maze.append(["#"," ","#"," "," "," ","#"])
    maze.append(["#"," ","#"," ","#","#","#"])
    maze.append(["#"," "," "," ","#"," ","#"])
    maze.append(["#","#","#","X","#","#","#"])
    return maze

def printMaze(maze, path=""):
    start = 0
    
    for x in range(len(maze[0])):
        if maze[0][x] == "O":
            start = x
 
    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j in range(len(maze)):
        for i in range(len(maze[j])):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(maze[j][i] + " ", end="")
        print()
    print('\n')
def valid(maze, moves):
    start = 0
    for x in range(len(maze[0])):
        if maze[0][x] == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True

def findEnd(maze, moves):
    start = 0
    for x in range(len(maze[0])):
        if maze[0][x] == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True

    return False
def main():
    nums = Queue()
    nums.enqueue("")
    add = ""
    maze = createMaze1()
    
    while not findEnd(maze, add):
        add = nums.dequeue()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(maze, put):
                nums.enqueue(put)
                
    maze = createMaze1()
    
    while not findEnd(maze, add):
        add = nums.dequeue()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(maze, put):
                nums.enqueue(put)    
    
main()