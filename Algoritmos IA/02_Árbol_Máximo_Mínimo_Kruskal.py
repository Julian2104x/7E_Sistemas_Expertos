class Kruskal:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.graph = []    # Lista para almacenar las aristas

    # Agregar una arista al grafo
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Función para encontrar el conjunto al que pertenece un vértice
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Función para unir dos conjuntos en un solo conjunto
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

    # Función principal que implementa el algoritmo de Kruskal
    def kruskal(self):
        result = []  # Para almacenar el árbol de expansión mínima
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        minimum_cost = 0
        for u, v, weight in result:
            minimum_cost += weight
        return minimum_cost, result

# Ejemplo de uso
g = Kruskal(5)  # Supongamos 5 lugares
# Añadimos las conexiones con sus respectivos costos
g.add_edge(0, 1, 10)  # Casa - Trabajo
g.add_edge(0, 2, 20)  # Casa - Supermercado
g.add_edge(1, 2, 15)  # Trabajo - Supermercado
g.add_edge(1, 3, 5)   # Trabajo - Gimnasio
g.add_edge(2, 3, 10)  # Supermercado - Gimnasio
g.add_edge(3, 4, 8)   # Gimnasio - Parque

minimum_cost, tree = g.kruskal()

print("Árbol de expansión mínima:")
for u, v, weight in tree:
    print(f"Lugar {u} - Lugar {v}: {weight}")

print(f"Costo mínimo total: {minimum_cost}")
