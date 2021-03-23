class LicenseCompatibilityMatrix:

    def __init__(self, graph):
        self.matrix = self.transitive_closure(graph)

    def reachable_nodes(self, graph, v):
        visited = {}
        queue = []
        queue.append(v)
        visited[v] = True
        while queue:
            v = queue.pop(0)
            for w in graph[v].keys():
                if visited.get(w) == None or not visited.get(w):
                    visited[w] = graph[v][w]
                    if(visited[w]):
                        queue.append(w)
        return visited.keys()

    def transitive_closure(self, graph):
        for node in graph.keys():
            for reachable_node in self.reachable_nodes(graph, node):
                graph[node][reachable_node] = True
        return graph

    def is_compatible(self, source_licence, derivative_license):
        if source_licence == derivative_license:
            return True
        elif self.matrix.get(source_licence) == None:
            return False
        else:
            return self.matrix.get(source_licence).get(derivative_license) != None

    def applicable_licenses(self, source_licenses):
        applicable_licenses = set(self.matrix[source_licenses[0]].keys())
        for source_license in source_licenses:
            applicable_licenses = applicable_licenses.intersection(set(self.matrix[source_license].keys()))
        return list(applicable_licenses)
