class Kruskal:
    def __init__(self):
        self.graph = []

    def add_edge(self, country1, country2, distance):
        self.graph.append([country1, country2, distance])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self, start, end):
        result = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = {}
        rank = {}
        for country1, country2, distance in self.graph:
            parent[country1] = country1
            parent[country2] = country2
            rank[country1] = 0
            rank[country2] = 0
        for country1, country2, distance in self.graph:
            x = self.find(parent, country1)
            y = self.find(parent, country2)
            if x != y:
                result.append([country1, country2, distance])
                self.union(parent, rank, x, y)
        return result

# Función para obtener un nodo válido del usuario
def get_valid_node(prompt):
    while True:
        node = input(prompt).strip()
        if node:
            return node
        print("Por favor, ingresa un nodo válido.")

# Ejemplo de uso
g = Kruskal()
g.add_edge("España", "Francia", 100)
g.add_edge("España", "Portugal", 50)
g.add_edge("Francia", "Alemania", 200)
g.add_edge("Portugal", "Francia", 150)
g.add_edge("Alemania", "Italia", 300)
g.add_edge("Italia", "España", 250)

start_node = get_valid_node("Ingrese el nodo de inicio: ")
end_node = get_valid_node("Ingrese el nodo final: ")

minimum_spanning_tree = g.kruskal(start_node, end_node)

print("Árbol de expansión mínima:")
for country1, country2, distance in minimum_spanning_tree:
    print(f"{country1} - {country2}: {distance} km")
