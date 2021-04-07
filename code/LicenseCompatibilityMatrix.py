class LicenseCompatibilityMatrix:

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.matrix = self.transitive_closure(edges)
        print(self.matrix)

    def reachable_nodes(self, graph, v):
        visited = {}
        queue = []
        queue.append(v)
        visited[v] = True
        while queue:
            v = queue.pop(0)
            for w in graph[v].keys():
                if (visited.get(w) == None or not visited.get(w)) and graph[v][w] != "Exception":
                    visited[w] = graph[v][w]
                    if(visited[w]):
                        queue.append(w)
        return visited.keys()

    def transitive_closure(self, graph):
        for node in graph.keys():
            for reachable_node in self.reachable_nodes(graph, node):
                graph[node][reachable_node] = True
            # Add exceptions that were ignored during transitive closure
            graph
        return graph

    def is_compatible(self, dependency_licence, derivative_license):

        # Get the uniqie node name for the license strings
        dependency_node = self.nodes.get(dependency_licence)
        derivative_node = self.nodes.get(derivative_license)

        if dependency_node == None or derivative_node == None: # If a license string is unknown
            return "Unknown"
        elif dependency_node == derivative_node: # If licenses belong to the same node (e.g., "MIT" and "MIT-0")
            return True
        else:
            return self.matrix.get(dependency_node).get(derivative_node) != None

    def applicable_licenses(self, dependency_licenses):
        applicable_licenses = set(self.matrix[self.nodes.get(dependency_licenses[0])].keys())
        for dep_license in dependency_licenses:
            applicable_licenses = applicable_licenses.intersection(set(self.matrix[self.nodes.get(dep_license)].keys()))
        return list(applicable_licenses)
