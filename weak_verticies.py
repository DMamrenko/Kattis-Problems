#Weak Verticies

#This Function will get the neighbors of a node depending on the given adjacency matrix
def getNeighbors(node, matrix):
    neighbors = []
    for line in range(len(matrix)):
        if matrix[line][node] == 1:
            neighbors.append(line)
    return neighbors

#This Function check to see if three nodes are triangular
def areTriangular(node1, node2, node3, matrix):
    node1_neighbors = getNeighbors(node1, matrix)
    node2_neighbors = getNeighbors(node2, matrix)
    node3_neighbors = getNeighbors(node3, matrix)
    if node1 in node2_neighbors and node1 in node3_neighbors and node2 in node3_neighbors and node2 in node1_neighbors and node3 in node2_neighbors and node3 in node1_neighbors:
        return True
    else:
        return False


n = int(input())
while n != -1:
    given = []
    neighborsByIndex = []
    weakVerticies = []
    #Storing the Given Adjacency Matrix in list called given
    for i in range(n):
        line = [int(s) for s in input().split(' ')]
        given.append(line)

        
    #Seeing if the current node is a weak node
    for node in range(len(given)):
        #getting the neighbors of the current node in the loop
        neighborsByIndex.append(getNeighbors(node, given))

    #Showing all the neighbors of each node:
    for node in range(len(given)):
        print('Node', node, 'Neighbors:', neighborsByIndex[node])

    for i in range(len(neighborsByIndex)):
        if len(neighborsByIndex[i]) == 1:
            weakVerticies.append(i)
        
    print(*weakVerticies, sep=' ')
    n = int(input())
