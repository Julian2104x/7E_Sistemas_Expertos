import heapq

class Prim:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.graph = [[] for _ in range(vertices)]  # Lista para almacenar las aristas

    # Agregar una arista al grafo
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    # Función principal que implementa el algoritmo de Prim
    def prim(self, start):
        visited = [False] * self.V
        min_heap = []
        min_spanning_tree = []

        # Inicializamos el algoritmo desde el nodo de inicio
        heapq.heappush(min_heap, (0, start))

        while min_heap:
            weight, vertex = heapq.heappop(min_heap)

            # Si el nodo ya ha sido visitado, lo ignoramos
            if visited[vertex]:
                continue

            visited[vertex] = True
            min_spanning_tree.append((weight, vertex))

            # Exploramos los nodos vecinos del nodo actual
            for neighbor, edge_weight in self.graph[vertex]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))

        return min_spanning_tree

# Ejemplo de uso
g = Prim(5)  # Supongamos 5 lugares
# Añadimos las conexiones con sus respectivos costos
g.add_edge(0, 1, 10)  # Casa - Trabajo
g.add_edge(0, 2, 20)  # Casa - Supermercado
g.add_edge(1, 2, 15)  # Trabajo - Supermercado
g.add_edge(1, 3, 5)   # Trabajo - Gimnasio
g.add_edge(2, 3, 10)  # Supermercado - Gimnasio
g.add_edge(3, 4, 8)   # Gimnasio - Parque

min_spanning_tree = g.prim(3)  # Supongamos que el nodo de inicio es la casa (nodo 0)

print("Árbol de expansión mínima (Prim):")
for weight, vertex in min_spanning_tree:
    print(f"Lugar {vertex} - Peso: {weight}")
