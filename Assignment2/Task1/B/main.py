from collections import deque

def bfs(graph, start, end):
    # perform BFS to find the shortest path from start to end
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.append((neighbor, dist+1))
    # end node is not reachable
    return float('inf')

# define the labyrinth graph
labyrinth = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'G'],
    'F': ['D', 'H'],
    'G': ['E', 'H'],
    'H': ['F', 'G', 'Exit'],
    'Exit': ['H']
}

# define the initial positions and speeds of the wizards
wizards = {
    'Harry': ('A', 2),
    'Ron': ('B', 3),
    'Hermione': ('C', 4)
}

# find the shortest distance from each wizard's initial position to the exit
distances = {}
for wizard, (position, speed) in wizards.items():
    distances[wizard] = bfs(labyrinth, position, 'Exit')

# calculate the time it will take for each wizard to reach the exit
times = {}
for wizard, (position, speed) in wizards.items():
    times[wizard] = distances[wizard] / speed

# predict which wizard will reach the exit first
winner = min(times, key=times.get)
print("The winner is", winner, "with a time of", times[winner], "minutes.")


#Note that this code assumes that the labyrinth graph is represented as a dictionary where the keys are the nodes
# and the values are lists of adjacent nodes. You will need to adjust the code accordingly if your
# representation is different.