import heapq
from copy import deepcopy
from collections import deque

from Node import GraphNode

class Graph:
    def __init__(self, vertices = [], edges = [], directed = False, weighted = False):
        self.vertices = dict()
        self.edges = dict()
        self.directed = directed
        self.weighted = weighted


        if vertices:
            for node in vertices:
                self.add_node(node)
                # self.edges[node.key] = {}

        if edges:
            for src_node_key, dest_node_key, *weight in edges:
                self.add_edge(src_node_key, dest_node_key, weight[0] if weight else None)

    def add_node(self, node):
        if node.key in self.vertices: return
        self.vertices[node.key] = GraphNode(node.key, node.val)

        if not(node.key in self.edges):
            self.edges[node.key] = {}

    def remove_node(self, node_key):
        edge_list_copy = deepcopy(self.edges)

        if node_key in edge_list_copy:
            for dest_node_key in edge_list_copy[node_key]:
                self.remove_edge(node_key, dest_node_key)
            self.edges.pop(node_key)
        
        for src_node_key in edge_list_copy:
            self.remove_edge(src_node_key, node_key)

        self.vertices.pop(node_key)

    def add_edge(self, src_node_key, dest_node_key, weight = None):
        if src_node_key == dest_node_key or not(src_node_key in self.vertices) or not(dest_node_key in self.vertices): return
        if self.directed and self.edges.get(dest_node_key, None) and src_node_key in self.edges[dest_node_key]: return

        if src_node_key in self.edges:
            if not (dest_node_key in self.edges[src_node_key]):
                if self.weighted: self.edges[src_node_key][dest_node_key] = weight
                else: self.edges[src_node_key][dest_node_key] = None

                if not(self.directed): self.add_edge(dest_node_key, src_node_key, weight)
        else:
            if self.weighted: self.edges[src_node_key] = {dest_node_key: weight}
            else: self.edges[src_node_key] = {dest_node_key: None}

            if not(self.directed): self.add_edge(dest_node_key, src_node_key, weight)

    def remove_edge(self, src_node_key, dest_node_key):
        if self.directed:
            if self.edges.get(src_node_key, None) and dest_node_key in self.edges[src_node_key]:
                self.edges[src_node_key].pop(dest_node_key)
        else:
            if self.edges.get(src_node_key, None) and dest_node_key in self.edges[src_node_key]:
                self.edges[src_node_key].pop(dest_node_key)
                self.edges[dest_node_key].pop(src_node_key)

    def breadth_first_search(self, starting_node, cb = None):
        visited = set(starting_node)
        queue = deque([starting_node])
        
        while queue:
            vertex = queue.popleft()
            cb(vertex) if cb else print(vertex, end=" ")

            if vertex in self.edges:
                for neighbor in self.edges[vertex].keys():
                    if not(neighbor in visited):
                        visited.add(neighbor)
                        queue.append(neighbor)
                
    def depth_first_search(self, starting_node, cb = None):
        visited = set(starting_node)
        stack = deque([starting_node])

        while stack:
            vertex = stack.pop()
            cb(vertex) if cb else print(vertex, end=" ")

            if vertex in self.edges:
                for neighbor in self.edges[vertex].keys():
                    if not(neighbor in visited):
                        visited.add(neighbor)
                        stack.append(neighbor)
            
    def shortest_path_djikstra(self, src_node_key):
        visited_vertices = set()

        shortest_paths = {node_key: {"previous_node_key": None, "shortest_distance": float("inf")} for node_key in self.vertices}
        shortest_paths[src_node_key] = {"previous_node_key": None, "shortest_distance": 0}

        pq = [(0, src_node_key)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node in visited_vertices:
                continue

            visited_vertices.add(current_node)

            for neighbor_key, edge_weight in self.edges[current_node].items():
                distance = current_distance + edge_weight
                if distance < shortest_paths[neighbor_key]["shortest_distance"]:
                    shortest_paths[neighbor_key]["shortest_distance"] = distance
                    shortest_paths[neighbor_key]["previous_node_key"] = current_node
                    heapq.heappush(pq, (distance, neighbor_key))

        return shortest_paths

    def __str__(self):
        result = []
        if self.vertices and self.edges:
            result.append("Vertices:")
            result.append(str([str(value) for value in self.vertices.values()]))
            result.append("Edges:")
            result.append(str(dict(self.edges)))
            return "\n".join(result) + "\n"
        return ""