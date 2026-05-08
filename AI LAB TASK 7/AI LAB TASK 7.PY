class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, node):
        return self.adjacency_list[node]

    # heuristic function
    def h(self, node):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return H[node]

    def a_star_algorithm(self, start, stop):

        open_list = set([start])
        closed_list = set()

        g = {}
        g[start] = 0

        parents = {}
        parents[start] = start

        while open_list:

            n = None

            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print("Path does not exist")
                return None

            if n == stop:
                path = []

                while parents[n] != n:
                    path.append(n)
                    n = parents[n]

                path.append(start)
                path.reverse()

                print("Path found:", path)
                return path

            for (m, weight) in self.get_neighbors(n):

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist")
        return None


adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

graph = Graph(adjacency_list)

graph.a_star_algorithm('A', 'D')