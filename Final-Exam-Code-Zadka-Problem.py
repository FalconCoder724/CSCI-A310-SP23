
map3 = """\
....
.XX.
....
"""

map1 = """\
..X.......
..X.......
.XX.......
..........
..........
"""

map4 = """\
..X.
X.X.
.XX.
....
"""

map2 = """\
..........
X..XXXXXX.
..XX.....X
....XXXXXX
..........
"""

data = {} # data dictionary holds the map
graph = {} # graph dictionary represents the neighbors, where you can go from each point
letters = ["a","b","c","d","e","f","g","h",'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Starting Index is at (0,0)
(line, column) = (0,0)

"""
Checks to see if i has reached a new line
if not: assigns (lines, column) to "." or "X" whichever in the map; assigns it to 
creates empty graph for possible paths
assigning column values

if the loop has moved onto a new lineL
the program assigns a new line value, and set's the column back to zero

creating the representation of the map
"""
for i in map3:
    if not i == '\n':
        data[line, column] = i
        graph[line, column] = []
        column += 1
    else:
        line += 1
        width = column
        column = 0

height = line

"""
Creating the paths that you can take
if hit the max of the map or (l,c) not in map or theres an x
it doesn't allow the path to travel there by utilizing the pass function
else it keeps adding to the graph as a path option
Then continues creating the graph which creates the paths.

"""
for line in range(height):
    for column in range (width):
        for dl in [-1, 0,1]:
            for dc in [-1,0,1]:
                (l, c) = (line + dl, column + dc)
                if (l,c) == (line,column) or (l,c) not in data or data[l,c] == 'X':
                    pass
                else:
                    graph[line,column] += [(l,c)] #Store in the list at dat[line,column] if valid
                    
from math import sqrt

#Method to calculate the distance between two points using the pythagoream theoreom

def dist (p1,p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

#calculates the overall path distance
def measure(path):
    d = 0
    #print(path)
    for i in range(len(path)-1):
        d = d + dist(path[i], path[i + 1])
    return d

"""
Helper function used to check for zero
used in measure(solution)
if measure(solution) is 0 then theres no possible path
"""
def help(num):
    if num > 0:
        return num
    else:
        try:
            print("no path found")
            return float('inf')
        except:
            print("no path found")

solution = []

def fun(paths, end, graph):
    global solution
    if (paths == []):
        return paths
    else:
        newPaths = []
        for path in paths: # looking for a path
            if path[-1] == end:
                #Stroes the path length or Changing it
                if solution == [] or measure(solution) > measure(path):
                    solution = path
                    print("Solution: ", path, " cost: ", measure(solution))
                continue
            #If path not solution b/c it is longers tan existing abandon
            if measure(path) >= measure(solution) > 0:
                #Abandon by continuing
                continue
            neighbors = graph[path[-1]]
            for neighbor in neighbors:
                if neighbor not in path:
                    newPaths = newPaths + [path + [neighbor]]
    return fun(newPaths, end, graph)

# The very bottom right of the graph    
target = (height-1, width-1)
answer = fun([[(0,0)]],target, graph)
print("Shortest Path from (0,0) to", str(target) + ":", solution, " cost ", help(measure(solution)))
print(map3)
def show(map):
    for line in range(height):
        for column in range(width):
            if (line, column) in solution:
                print(letters[column], end=' ')
            else:
                print(data[line, column], end= " ")
        print()

print("----------------------")
show(map3)