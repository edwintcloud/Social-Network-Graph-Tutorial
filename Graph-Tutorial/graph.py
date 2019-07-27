from vertex import Vertex
from queue import SimpleQueue


class Graph:
    """ Graph Class
    A class demonstrating the essential facts and functionalities of graphs.
    """

    def __init__(self, file_name=None):
        """Initialize a graph object with an empty dictionary."""
        self.vertices = {}
        self.num_vertices = 0
        self.num_edges = 0
        self.type = "G"

        # if file_name specified, read in graph from file
        if file_name:
            self._read_from_file(file_name)

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        if key not in self.vertices:
            self.num_vertices += 1
            self.vertices[key] = Vertex(key)
        return self.vertices[key]

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        return None if key not in self.vertices else self.vertices[key]

    def add_edge(self, key1, key2, weight=1):
        """Add an edge from vertex with key `key1` to vertex with key `key2` with an optional weight."""
        if self.get_vertex(key1) is None:
            self.add_vertex(key1)
        if self.get_vertex(key2) is None:
            self.add_vertex(key2)
        self.num_edges += 1
        self.vertices[key1].add_neighbor(self.vertices[key2], weight)

    def get_vertices(self):
        """Return all the vertices in the graph."""
        return self.vertices.keys()

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g."""
        return iter(self.vertices.values())

    def get_edges(self, weighted=False):
        """Return a list of edges in the graph.

        Args:
            weighted (bool): if True, resulting list will also contain the edge weights
        """
        result = []
        for v in self.vertices.values():
            for w in v.neighbors:
                if weighted:
                    result.append((v.get_id(),
                                   w.get_id(), v.get_edge_weight(w)))
                else:
                    result.append((v.get_id(),
                                   w.get_id()))
        return result
    
    def breadth_first_search(self, vertex, n):
        "Performs bfs."

        # Make sure the input node is actually in the graph
        if vertex not in self.vertices:
            raise Exception(f"Vertex {vertex} not in graph.")

        # Run breadth_first_search starting from the input node and going `n` levels deep
        # create needed structures
        result = []
        visited = set()
        queue = SimpleQueue()

        # initialize queue with start vertex
        queue.put(self.vertices[vertex])

        # while there are vertices in the queue
        while queue.qsize() > 0:
            # dequeue a vertex
            curVtx = queue.get()
            # if the vertex has not been visited
            if curVtx not in visited:
                # add it to visited set and result list
                visited.add(curVtx)
                result.append(curVtx.id)
                if len(result) == n:
                    return result
                # iterate through its neighbors
                for neighbor in curVtx.get_neighbors():
                    # put the neighbor in the queue
                    queue.put(neighbor)

        # return result list of vertex ids
        return result

    def find_shortest_path(self, vtxA, vtxB):
        """Return the shortest path from vertex a to vertex b."""

        # ensure that vtxA and vtxB are in graph
        if vtxA not in self.vertices or vtxB not in self.vertices:
            raise Exception("One or both of the supplied vertices " +
                            vtxA + ", " + vtxB + " is not in this graph.")

        # create our needed structures
        result = []
        visited = set()
        queue = SimpleQueue()

        # initialize queue with start vertex
        queue.put(self.vertices[vtxA])

        # while there are vertices in the queue
        while queue.qsize() > 0:
            # dequeue a vertex
            curVtx = queue.get()
            # if the vertex has not been visited
            if curVtx not in visited:
                # add it to visited set and result list
                visited.add(curVtx)
                result.append(curVtx.id)
                # iterate through its neighbors
                for neighbor in curVtx.get_neighbors():
                    # if the neighbor is the vertex we are looking for, we are done
                    # append the neighbor to the result and return
                    if neighbor.id == vtxB:
                        result.append(neighbor.id)
                        return result
                    # otherwise, put the neighbor in the queue
                    queue.put(neighbor)

        # return result list of vertex ids
        return result

    def _read_from_file(self, file_name):
        """Read a graph from a file."""

        # load file specified
        with open(file_name, 'r') as f:
            file_lines = f.readlines()

        # if less than 3 lines in file, throw error
        if len(file_lines) < 3:
            raise Exception("Expected input file to contain at least 3 lines.")

        # set graph type
        self.type = file_lines[0].strip()
        if self.type != "G" and self.type != "D":
            raise Exception(
                "Expected input file to have a type of G or D for line 1 but " + self.type + " was given.")

        # add graph vertices
        for vtx in file_lines[1].strip().split(','):
            self.add_vertex(vtx)

        # add graph edges
        for line in file_lines[2:]:
            edge_spec = line.strip("() \n").split(',')
            if len(edge_spec) != 3 and len(edge_spec) != 2:
                raise Exception(
                    "Expected input file edge specification to have 2 or 3 items but " + line + " was given.")
            vtx1, vtx2 = edge_spec[:2]
            weight = 1 if len(edge_spec) != 3 else int(edge_spec[2])
            if self.type == "G":
                self.add_edge(vtx1, vtx2, weight)
                self.add_edge(vtx2, vtx1, weight)
            else:
                self.add_edge(vtx1, vtx2, weight)
