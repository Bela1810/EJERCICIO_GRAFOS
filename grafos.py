class Graph:
    def __init__(self):
        self.graph: dict = {}  # lista de adyacencia

    def add_vertex(self, label):  # AGREGAR NODO
        if label not in self.graph.keys():
            self.graph[label] = []  # nodo desconectado

    def has_edge(self, v1, v2):  # TIENE ARISTAS
        return v2 in self.graph[v1]

    def add_edge(self, v1, v2, directed=True):  # AGREGAR ARISTA
        self.add_vertex(v1)
        self.add_vertex(v2)

        if (not directed and not self.has_edge(v2, v1)):
            self.graph[v2].append(v1)

        if (not self.has_edge(v1, v2)):
            self.graph[v1].append(v2)

    def print_graph(self):
        print(self.graph)  # VISUALIZAR GRAFO

    def delete_vertex(self, label):
        # Verificar si los vértices son válid}os
        if label not in self.graph:
            return None
        self.graph.pop(label)
        for node in self.graph:
            if label in self.graph[node]:
                # self.graph[label]
                self.graph[node].remove(label)


def find_way(graph, origin, destiny):  # BUSCAR CAMINO
    # Verificar si los vértices son válidos
    if origin not in graph or destiny not in graph:
        return None

    # queue para realizar el BFS
    queue = []
    queue.append((origin, [origin]))  # Tupla con el vértice y el camino hasta él

    while queue:
        actual_vertex, actual_way = queue.pop()

        # Si se encuentra el destiny, se retorna el camino
        if actual_vertex == destiny:
            print(f"Way found: {actual_way}")

            return actual_way

        # Explorar los neighbors del vértice actual
        for neighbor in graph[actual_vertex]:
            if neighbor not in actual_way:  # Evitar ciclos
                queue.append((neighbor, actual_way + [neighbor]))

    # Si no se encontró un camino, retorna None
    print("No path found between the given vertices.")
    return None


while True:
    print("\n1. Create Graph")
    print("2. View Graph")
    print("3. Add vertex")
    print("4. Add edge")
    print("5. find way")
    print("6. Delete vertex")
    print("7. Exit")
    option = input("Select an option: ")

    if option == "1":
        graph = Graph()  # CREAR grafo
        print("New graph created.")

    elif option == "2":
        graph.print_graph()

    elif option == "3":
        node = input("Enter new value for node: ").upper()
        graph.add_vertex(node)
        print(f"Added {node} to the graph.")

    elif option == "4":
        origin = input("Enter name of the node origin: ").upper()

        destiny = input("Enter name of the node destination: ").upper()
        graph.add_edge(origin, destiny)

        print(f"Added an edge between {origin} and {destiny}")

    elif option == "5":
        origin = input("Enter first value: ").upper()
        destiny = input("Enter final value: ").upper()
        way = find_way(graph.graph, origin, destiny)

        if way:
            print("the way found is:", "->".join(way))
        else:
            print(f"We did not find a way")
    elif option == "6":
        label = input("Enter the name of the vertex").upper()
        graph.delete_vertex(label)
    elif option == "7":
        break
    else:
        print("Selected an option.")
