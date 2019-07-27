class Vertex(object):
    """ Vertex Class
    A helper class for the Graph class that defines vertices and vertex neighbors.
    """

    def __init__(self, vertex):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight):
        """Add a neighbor along a weighted edge."""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.id} adjacent to {[x.id for x in self.neighbors]}'

    def get_neighbors(self, as_string=False):
        """Return the neighbors of this vertex.

        Args:
            as_string (bool): if True, returns iterable of ids instead of vertex objects
        """
        if as_string:
            iter(i.id for i in self.neighbors.keys())
        return iter(self.neighbors.keys())

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        return self.neighbors[vertex]
