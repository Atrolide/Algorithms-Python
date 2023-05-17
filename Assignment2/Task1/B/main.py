from queue import Queue

def bfs(graph, start, end):
    # perform BFS to find the shortest path from start to end

    # initialize a queue with a tuple containing the starting node and its distance from the start node
    queue = Queue()
    queue.put((start, 0))

    # initialize a set to keep track of visited nodes
    visited = set()

    # continue the BFS until the queue is empty
    while not queue.empty():
        # dequeue the node at the front of the queue and its distance from the start node
        node, dist = queue.get()

        # if the dequeued node is the destination node, return its distance from the start node
        if node == end:
            return dist

        # if the dequeued node has already been visited, skip it
        if node in visited:
            continue

        # mark the dequeued node as visited
        visited.add(node)

        # enqueue all of the dequeued node's neighbors and their distances from the start node
        for neighbor in graph[node]:
            queue.put((neighbor, dist + 1))

    # if the destination node is not reachable from the start node, return infinity
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
    'Harry': ('A', 1),
    'Ron': ('C', 1),
    'Hermione': ('C', 9)
}

# find the shortest distance from each wizard's initial position to the exit
distances = {}
for wizard, (position, speed) in wizards.items():
    distances[wizard] = bfs(labyrinth, position, 'Exit')
print(distances)

# calculate the time it will take for each wizard to reach the exit
times = {}
for wizard, (position, speed) in wizards.items():
    times[wizard] = distances[wizard] / float(speed)


# predict which wizard will reach the exit first
winner = min(times, key=times.get)
print("The winner is", winner, "with a time of", times[winner] * 60, "seconds.")



