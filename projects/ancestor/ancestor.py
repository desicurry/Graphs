# from util import Stack, Queue


# def earliest_ancestor(ancestors, starting_node):
#     # Create an empty queue
#     q = Queue()
#     # Create an list called 'path' housing the starting_node
#     path = [starting_node]
#     # Add that path(just the starting_node) to the queue
#     q.enqueue(path)
#     # While the queue is not empty
#     while q.size() > 0:
#         # Create a currentPath variable set to be our dequeued queue
#         currentPath = q.dequeue()
#         # Create an empty newPath list
#         newPath = []
#         # Create a changed variable set to False
#         changed = False
#         # Loop over each node in the currentPath
#         for node in currentPath:
#             # Loop through its ancestors
#             for ancestor in ancestors:
#                 # If the value of the next ancestor is equal to the node:
#                 if ancestor[1] == node:
#                     # Append the current ancestor to the newPath
#                     newPath.append(ancestor[0])
#                     # Set its changed value to true
#                     changed = True
#                     # Add the new path to the queue
#                     q.enqueue(newPath)
#         # If changed is False
#         if changed is False:
#             # If it has no parents
#             if currentPath[0] == starting_node:
#                 return -1
#             # If it does return it
#             else:
#                 return currentPath[0]


from collections import deque
from collections import defaultdict

def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    # A tuple with a node and its distance from the starting node
    # At the beginning, the starting node's earliest ancestor is itself
    earliestAncestor = (starting_node, 0)
    stack = deque()
    stack.append((starting_node, 0))
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        currNode, distance = curr[0], curr[1]
        visited.add(curr)

        # This checks if the node is a terminal node
        if currNode not in graph:
        # Only consider terminal nodes that have a greater distance than the ones we've found so far
            if distance > earliestAncestor[1]:
                earliestAncestor = curr
            # If there's a tie then choose the ancestor with the lower id
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = curr
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    # If the starting node's earliest ancestor is itself, then just return -1
    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1

# Creates a graph where the keys are a node and its values are its ancestors
def createGraph(edges):
    # This convenience method simply allows us to initialize default values when assigning
    # a key to a dictionary. In this case, the default value for a new key is an empty set
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph