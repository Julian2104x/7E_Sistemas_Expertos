import heapq # Mantiene ordenados los nodos por distancia

# Definición del grafo como un diccionario de listas de adyacencia
graph = {
    'casa': {'escuela': 10, 'trabajo': 20, 'gimnasio': 15},
    'escuela': {'casa': 10, 'trabajo': 5},
    'trabajo': {'casa': 20, 'escuela': 5, 'gimnasio': 10, 'supermercado': 8},
    'gimnasio': {'casa': 15, 'trabajo': 10},
    'supermercado': {'trabajo': 8}
}

def dijkstra(graph, start): # Definimos la función con dos argumentos (graph y start)
    # Diccionario para almacenar la distancia más corta desde el nodo de inicio a cada nodo
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    
    # Cola de prioridad (heap) para mantener los nodos sin visitar
    priority_queue = [(0, start)]

    while priority_queue:
        # Extraer el nodo con la distancia más corta desde el inicio
        dist_to_current, current_node = heapq.heappop(priority_queue)

        # Si encontramos una distancia más corta a este nodo, actualizamos
        if dist_to_current > distance[current_node]:
            continue

        # Iterar sobre los nodos vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            dist = distance[current_node] + weight
            # Si encontramos una distancia más corta a un vecino, actualizamos
            if dist < distance[neighbor]:
                distance[neighbor] = dist
                heapq.heappush(priority_queue, (dist, neighbor))

    return distance

start_node = 'supermercado' # Aquí se modifica el nodo de inicio
distances = dijkstra(graph, start_node)

print("Distancias más cortas desde", start_node + ":") #ME imprime resultados
for node, dist in distances.items():
    print("Hacia", node + ":", dist)

