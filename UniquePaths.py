#!/usr/bin/env python
# coding: utf-8

# ### Render Unique Shortest Paths

# In[1]:


# file to render all shortest unique paths after a run through of 1000 randomisations
# compatibility with graph.py file


# In[2]:


import graphs as g
from graphviz import Digraph
from random import randint
from statistics import mean
from copy import deepcopy
from time import process_time


# In[3]:


# my own dijkstra's, returns multiple shortest paths
def wijkstra(graph, source, destination):
    paths = []
    current = source
    vertices = {vertex for vertex in graph.keys()}
    distances = {vertex: float("inf") for vertex in vertices}
    previous = {vertex: None for vertex in vertices}
    distances[source] = 0

    while len(vertices) > 0:
        # make a temp set with only vertices still in vertices
        temp_dists = {i: distances[i]
                      for i in distances.keys() if i in vertices}
        current = min(temp_dists, key=temp_dists.get)
        vertices.remove(current)

        for neighbour in graph[current].items():
            alt = distances[current] + neighbour[1]
            if alt <= distances[neighbour[0]]:
                distances[neighbour[0]] = alt
                previous[neighbour[0]] = current
                # if the end node has a value, store that path
                if distances[destination] != float("inf"):
                    temp_prev = deepcopy(previous)
                    paths.append(temp_prev)
    #print(f"Distances: {distances}\n\npaths: {paths}\n\ndistances[destination]: {distances[destination]}")
    return (distances, paths, distances[destination])


# In[4]:


def random_graph(m, start, end, graph):
    # randomizing graphs arcs upper bound m
    for key in graph.keys():
        for sub_key in graph[key].keys():
            graph[key][sub_key] = randint(1, m)

    #print(f"graph: {graph}\n\n")

    # dijkstra's for shortest paths
    edge_distances, shortest_paths, shortest_distance = wijkstra(
        graph, start, end)

    # use 'previous' dict to determine shortest path
    all_paths = []
    for previous in shortest_paths:
        source, target = start, end
        path = [target]
        current = target
        while current != source:
            # loop back through dictionary
            current = previous[current]
            path.insert(0, current)
        all_paths.append(path)

    # removing duplicate paths
    unique_paths = [list(y) for y in set([tuple(x) for x in all_paths])]
    #print(f"Unique Paths: {unique_paths}")

    # making shortest paths into list of arcs as tuples
    temp_paths = []
    for path in unique_paths:
        temp = []
        for i in range(len(path)):
            if i < len(path)-1:
                temp.append(tuple(path[i:i+2]))
        temp_paths.append(temp)

    # get arc weights from arcs in tuples
    arc_weights = []
    for path in temp_paths:
        temp_arcs = []
        for arc in path:
            temp_arcs.append(graph[arc[0]][arc[1]])
        arc_weights.append(temp_arcs)

    # all path lengths
    path_lengths = [sum(i) for i in arc_weights]

    # if check, if 1 path its unique, if more than 1, all must be equal
    if len(path_lengths) == 1:
        # unique path
        pass
    elif path_lengths.count(path_lengths[0]) == len(path_lengths):
        # non unique shortest path
        pass
    else:
        # bigger path snook into list
        arc_weights = [arc_weights[path_lengths.index(min(path_lengths))]]
        temp_paths = [temp_paths[path_lengths.index(min(path_lengths))]]

    # get min of path lengths and first path if third option triggers
    # end int equals 1 for unique and 2 or more for non-unique
    un_check = len(temp_paths)
    #print([sum(i) for i in arc_weights])
    # print(un_check)
    return (graph, temp_paths, arc_weights, un_check)


# In[5]:


def render(graph_paths_arcs):
    '''Takes in tuple of graph dictionary, unique paths and arc weights, draws all unique paths as pdfs'''
    # unpacking input
    graph = graph_paths_arcs[0]
    unique_path = graph_paths_arcs[1]
    arc_weights = graph_paths_arcs[2]
    for i in range(len(unique_path)):
        # creating graph
        g = Digraph('UsersDigraph', filename='UsersDigraph.gv')
        g.attr(size='8,5')
        g.attr('node', shape='circle')
        # loop through keys to get all nodes
        for node in graph.keys():
            g.node(node)
        # nested loop to create all edges
        for node, connections in graph.items():
            for con_node, arc_length in connections.items():
                if (node, con_node) in unique_path[i]:
                    g.edge(node, con_node, label=str(arc_length), color='red')
                else:
                    g.edge(node, con_node, label=str(arc_length))
        # showing graph
        g.render(f"shortest_path{i+1}", 'shortest_paths')
    return True


# In[6]:


def draw_unique(graph, m):
    '''Takes in graph and m value, creates one random instance of graph,
    outputs pdf of unique shortest path/s through graph as pdf'''
    render(random_graph(m, 'S', 'T', graph))
    print('Finished')


# In[7]:


def test_bound_iterate(graph, limit):
    '''Takes in graph dictionary and upper bound of m value to iteratively test, returns if bound held'''
    for m in range(1, limit+1):
        all_cases = [random_graph(m, 'S', 'T', graph)[3] for i in range(1000)]

        # amount of unique path cases
        un_sum = all_cases.count(1)/10

        # arcs calculated for bound
        arcs = sum([len(i.keys()) for i in graph.values()])

        # Ta-Shma's bound
        bound = round((1 - (1/m))**arcs, 2)*100

        # printing every 25
        if m % 25 == 0:
            print(f"---------------------------\n\nm = {m}\n\nUnique Path Found {un_sum}%")
            print(f"\nTa Shma's Bound: {bound}%\n")

        # Checking if bound held
        if m == limit:
            print(f"\n*****************\n\n\nBOUND HELD!\n\n\n******************")
            return True
    print('did not hold')
    return False


# In[8]:


def test_bound(graph, m):
    '''Takes in graph and m value, outputs unique path percentage and bound estimation'''
    all_cases = [random_graph(m, 'S', 'T', graph)[3] for i in range(1000)]

    # amount of unique path cases
    un_sum = all_cases.count(1)/10

    # arcs calculated for bound
    arcs = sum([len(i.keys()) for i in graph.values()])

    # Ta-Shma's bound
    bound = round((1 - (1/m))**arcs, 2)*100
    
    print(f"---------------------------\n\nm = {m}\n\nUnique Path Found {un_sum}%")
    print(f"\nTa Shma's Bound: {bound}%\n\n---------------------------")


# In[9]:


#draws unique from one instance of a graph
#draw_unique(g.get('medium2'), 10)


# In[10]:


#testing bound
#test_bound_iterate(g.get('small'), 100)


# In[16]:


#testing bound
#for name in g.all_graphs():
#    print(f"\n{name.capitalize()} Graph: \n")
#    test_bound(g.get(name), 100)


# In[ ]:




