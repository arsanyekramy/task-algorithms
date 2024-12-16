# -*- coding: utf-8 -*-
"""Prim’s algorithm .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TUudTnnmppibJ24UdN8zO3ttNaQK__He
"""

import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = {}    # Dictionary to store the graph

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph

    def prim_mst(self):
        # Initialize a priority queue
        min_heap = []
        visited = set()
        mst_edges = []

        # Start from the first vertex (0)
        starting_vertex = 0
        visited.add(starting_vertex)

        # Add all edges from the starting vertex to the priority queue
        for neighbor, weight in self.graph.get(starting_vertex, []):
            heapq.heappush(min_heap, (weight, starting_vertex, neighbor))

        while min_heap:
            weight, u, v = heapq.heappop(min_heap)

            if v not in visited:
                visited.add(v)
                mst_edges.append((u, v, weight))

                # Add all edges from the newly added vertex to the priority queue
                for next_neighbor, next_weight in self.graph.get(v, []):
                    if next_neighbor not in visited:
                        heapq.heappush(min_heap, (next_weight, v, next_neighbor))

        return mst_edges

# Example usage
if __name__ == "__main__":
    g = Graph(5)  # Create a graph with 5 vertices
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    mst = g.prim_mst()

    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")