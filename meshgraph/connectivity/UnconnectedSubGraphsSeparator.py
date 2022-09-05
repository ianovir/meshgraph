from meshgraph.Graph import Graph


def _get_unconnected_nodes_by_node(node):
    visited = []
    sub_graph_nodes = _bfs(node, visited)
    return sub_graph_nodes


def _bfs(node, visited):
    queue = []
    result = []
    queue.append(node)
    result.append(node)

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for neighbour in current_node.neighbors:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                result.append(neighbour)

    return result


def separate_unconnected_sub_graphs(graph):
    """Returns a list of unconnected sub-graphs
    Perform a BFS to separate unconnected nodes from graph;
    found unconnected nodes are removed from original graph"""

    sub_graphs = []
    copy_graph = Graph()
    copy_graph.nodes = graph.nodes
    while len(copy_graph.nodes) != 0:
        unconnected_nodes = _get_unconnected_nodes_by_node(copy_graph.nodes[0])
        copy_graph.subtract_nodes(unconnected_nodes)
        sub_graph = Graph()
        sub_graph.nodes = unconnected_nodes
        sub_graph.sort_nodes()
        sub_graph.reset_nodes_indexes()
        sub_graphs.append(sub_graph)

    return sub_graphs
