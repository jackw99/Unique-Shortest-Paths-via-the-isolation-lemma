#!/usr/bin/env python
# coding: utf-8

# # Carries out testing of passed in graph by user

# In[1]:


#libraries needed
from random import randint
from statistics import mean
from copy import deepcopy
from time import process_time


# In[2]:


#my own dijkstra's, returns multiple shortest paths
def wijkstra(graph, source, destination):
    paths = []
    current = source
    vertices = {vertex for vertex in graph.keys()}
    distances = {vertex: float("inf") for vertex in vertices}
    previous = {vertex: None for vertex in vertices}
    distances[source] = 0
    
    while len(vertices) > 0:
        #make a temp set with only vertices still in vertices
        temp_dists = {i: distances[i] for i in distances.keys() if i in vertices}
        current = min(temp_dists, key=temp_dists.get)
        vertices.remove(current)
    
        for neighbour in graph[current].items():
            alt = distances[current] + neighbour[1]
            if alt <= distances[neighbour[0]]:
                distances[neighbour[0]] = alt
                previous[neighbour[0]] = current
                #if the end node has a value, store that path
                if distances[destination] != float("inf"):
                    temp_prev = deepcopy(previous)
                    paths.append(temp_prev)
    return (distances, paths, distances[destination])


# In[3]:


def random_graph(m, start, end, graph):
    #randomizing graphs arcs upper bound m
    for key in graph.keys():
        for sub_key in graph[key].keys():
            graph[key][sub_key] = randint(1, m)

    #dijkstra's for shortest paths
    edge_distances, shortest_paths, shortest_distance = wijkstra(graph, start, end)

    #use 'previous' dict to determine shortest path
    all_paths = []
    for previous in shortest_paths:
        source, target = start, end
        path = [target]
        current = target
        while current != source:
            #loop back through dictionary
            current = previous[current]
            path.insert(0, current)
        all_paths.append(path)
        
    #removing duplicate paths
    unique_paths = [list(y) for y in set([tuple(x) for x in all_paths])]
    return len(unique_paths)


# In[4]:


def average_accuracy(m, start, end, graph):

    #run 1000 times
    all_shortest_paths = [random_graph(m, start, end, graph) for i in range(1000)]

    #percentage of time a unique path found
    return round((all_shortest_paths.count(1)/1000)*100, 2)


# In[5]:


def run(graph):
    #arcs calculated for bound
    arcs = sum([len(i.keys()) for i in graph.values()])
    print('***RESULTS***\n')
    for m in range(1, 101):
        start = 'S'
        end = 'T'
        iterations = 1

        #average accuracy over n runs
        accuracy_scores = [average_accuracy(m, start, end, graph) for i in range(iterations)]
        
        #average accuracy
        acc = round(mean(accuracy_scores), 2)

        #Ta-Shma's bound
        bound = round((1 - (1/m))**arcs, 2)*100
        
        #printing every ten
        if m % 10 == 0:
            print(f"---------------------------\n\nm = {m}\n\nUnique Path Found {acc}%")
            print(f"\nTa Shma's Bound: {bound}%\n")
        
        #check if bound has overtaken unique percentage
        if bound > acc:
            print(f"\n*****************\n\nBOUND FAILED ON m = {m}\n\n******************")
            break
        
        #bound held check
        if m == 100:
            print(f"\n*****************\n\n\nBOUND HELD!\n\n\n******************")
    


# In[ ]:




