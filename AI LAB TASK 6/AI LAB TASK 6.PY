graph = {
 'A':['B','C'],
 'B':['D','E'],
 'C':['F'],
 'D':['G','H'],
 'E':[],
 'F':['I','K'],
 'G':[],
 'H':['L'],
 'I':[],
 'K':['M'],
 'L':[],
 'M':[]
}

def dls(node, goal, depth, limit, path):

    path.append(node)

    if node == goal:
        return True

    if depth == limit:
        path.pop()
        return False

    for child in graph[node]:
        if dls(child, goal, depth+1, limit, path):
            return True

    path.pop()
    return False


start = 'A'
goal = input("Enter goal node: ")
limit = int(input("Enter depth limit: "))

path = []

if dls(start, goal, 0, limit, path):
    print("Path:", path)
else:
    print("Goal not found within limit")