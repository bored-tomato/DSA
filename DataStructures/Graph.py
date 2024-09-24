from copy import deepcopy
from collections import deque

class Graph:
    def __init__(self, edge_list = None, directed = False, weighted = False):
        self.edge_list = dict()
        self.directed = directed
        self.weighted = weighted

        if edge_list:
            for src_node, dest_node, *weight in edge_list:
                self.add_edge(src_node, dest_node, weight[0] if weight else None)

    def add_edge(self, src_node, dest_node, weight = None):
        if src_node == dest_node: return
        if self.directed and self.edge_list.get(dest_node, None) and src_node in self.edge_list[dest_node]: return

        if src_node in self.edge_list:
            if not (dest_node in self.edge_list[src_node]):
                if self.weighted: self.edge_list[src_node][dest_node] = weight
                else: self.edge_list[src_node][dest_node] = None

                if not(self.directed): self.add_edge(dest_node, src_node, weight)
        else:
            if self.weighted: self.edge_list[src_node] = {dest_node: weight}
            else: self.edge_list[src_node] = {dest_node: None}

            if not(self.directed): self.add_edge(dest_node, src_node, weight)

    def remove_edge(self, src_node, dest_node):
        if self.directed:
            if self.edge_list.get(src_node, None) and dest_node in self.edge_list[src_node]:
                self.edge_list[src_node].pop(dest_node)
        else:
            if self.edge_list.get(src_node, None) and dest_node in self.edge_list[src_node]:
                self.edge_list[src_node].pop(dest_node)
                self.edge_list[dest_node].pop(src_node)

    def remove_node(self, node):
        edge_list_copy = deepcopy(self.edge_list)

        if node in edge_list_copy:
            for dest_node in edge_list_copy[node]:
                self.remove_edge(node, dest_node)
            self.edge_list.pop(node)
        else:
            for src_node in edge_list_copy:
                self.remove_edge(src_node, node)


    def breadth_first_search(self, starting_node, cb = None):
        visited = set(starting_node)
        queue = deque([starting_node])
        
        while queue:
            vertex = queue.popleft()
            cb(vertex) if cb else print(vertex, end=" ")

            if vertex in self.edge_list:
                for neighbor in self.edge_list[vertex].keys():
                    if not(neighbor in visited):
                        visited.add(neighbor)
                        queue.append(neighbor)
                
            
    def __str__(self):
        return str(dict(self.edge_list))