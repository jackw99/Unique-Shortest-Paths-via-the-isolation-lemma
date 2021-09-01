#!/usr/bin/env python
# coding: utf-8

# # Directed Graphs

# File that holds graph dictionaries for testing bound accuracy

# In[40]:


from graphviz import Digraph


# In[41]:


# nested dictionary for all graphs
graphs = {'small':
          {
              'S': {'E': 3, 'G': 2},
              'E': {'W': 4, 'J': 6},
              'G': {'J': 3},
              'W': {'K': 1, 'T': 2},
              'J': {'K': 5},
              'K': {'T': 1},
              'T': {}
          },
          'medium':
          {
              'S': {'B': 4, 'C': 3},
              'A': {'F': 5, 'E': 5},
              'B': {'E': 2, 'G': 2, 'A': 1, 'D': 2, 'C': 0},
              'C': {'D': 3, 'G': 2},
              'D': {'H': 2, 'F': 4},
              'E': {'I': 3},
              'F': {'H': 6},
              'G': {'I': 3, 'K': 0},
              'H': {'J': 2, 'G': 2, 'K': 0},
              'I': {'J': 3},
              'K': {'J': 3},
              'J': {'T': 3},
              'T': {}
          },
          'medium2':
          {
              'S': {'A': 2,'B': 4, 'C': 3},
              'A': {'F': 5, 'D': 5},
              'B': {'E': 2, 'D': 2},
              'C': {'F': 3, 'E': 2},
              'D': {'H': 2, 'G': 4},
              'E': {'G': 2,'I': 3},
              'F': {'H': 6, 'I': 9},
              'G': {'T': 3},
              'H': {'T': 2},
              'I': {'T': 3},
              'T': {}
          },
          'medium3':
          {
              'S': {'A': 2,'B': 4, 'C': 3},
              'A': {'F': 5},
              'B': {'E': 2},
              'C': {'D': 3},
              'D': {'H': 2},
              'E': {'I': 3},
              'F': {'G': 6},
              'G': {'T': 3},
              'H': {'T': 2},
              'I': {'T': 3},
              'T': {}
          },
          'medium4':
          {
              'S': {'A': 2, 'C': 3},
              'A': {'F': 5, 'H': 5},
              'B': {'E': 2, 'I': 2, 'T':2},
              'C': {'B': 3, 'E': 2, 'H':1},
              'D': {'H': 2, 'G': 4},
              'E': {'T': 2,'I': 3},
              'F': {'I': 6, 'I': 9},
              'G': {'T': 3},
              'H': {'T': 2},
              'I': {'T': 3},
              'T': {}
          },
          'medium5':
          {
              'S': {'A': 2,'B': 4, 'C': 3},
              'A': {'F': 5, 'D': 5},
              'B': {'E': 2, 'D': 2},
              'C': {'F': 3, 'E': 2},
              'D': {'H': 2, 'G': 4},
              'E': {'G': 2,'I': 3},
              'F': {'H': 6, 'I': 9},
              'G': {'L': 3, 'K': 2},
              'H': {'J': 2, 'K': 3},
              'I': {'L': 3, 'J': 2},
              'L': {'N': 6, 'O': 9},
              'J': {'N': 6, 'M': 9},
              'K': {'O': 6, 'M': 9},
              'N': {'T': 3},
              'O': {'T': 2},
              'M': {'T': 6},
              'T': {}
          },
          'large':
          {
              'S': {'1': 0, '2': 0, '3': 0, '4': 0},
              '1': {'4': 0, '6': 0, '7': 0, '10': 0},
              '2': {'3': 0, '4': 0, '5': 0, '7': 0, '11': 0},
              '3': {'2': 0, '7': 0, '8': 0, '9': 0},
              '4': {'11': 0, '12': 0, '14': 0, '15': 0},
              '5': {'6': 0, '9': 0, '10': 0, '13': 0},
              '6': {'8': 0, '11': 0, '14': 0},
              '7': {'11': 0, '12': 0, '13': 0, '15': 0},
              '8': {'11': 0, '14': 0, '16': 0},
              '9': {'10': 0, '13': 0, '16': 0},
              '10': {'11': 0, '12': 0, '15': 0},
              '11': {'12': 0, '14': 0, '16': 0},
              '12': {'14': 0, '15': 0, '16': 0, '17': 0, '18': 0},
              '13': {'14': 0, '19': 0, '20': 0},
              '14': {'16': 0, '17': 0, '18': 0},
              '15': {'12': 0, '18': 0, '20': 0},
              '16': {'18': 0, '19': 0, '20': 0, 'T': 0},
              '17': {'18': 0, '19': 0, '20': 0, 'T': 0},
              '18': {'20': 0, 'T': 0},
              '19': {'16': 0, '17': 0, 'T': 0},
              '20': {'17': 0, '19': 0, 'T': 0},
              'T': {},
          }
          }


# In[4]:


#getter for graph name param
def get(graph_name):
    '''Takes in graph name, returns nodes and arc connections as dictionary'''
    return graphs[graph_name]


# In[5]:


def get_arcs(graph_name):
    '''Takes in graph name, returns how many arcs in graph'''
    return sum([len(i.keys()) for i in graphs[graph_name].values()])


# In[1]:


#setter for graph
def add_graph(name, graph):
    '''Takes in graph name and graph as dictionary,
    adds graph to dictionary of graphs'''
    graphs[name] = graph
    return True


# In[6]:


#shows all available graphs for user
def all_graphs():
    '''Returns list of all possible graphs in dictionary'''
    return list(graphs.keys())


# In[7]:


#draw a graph with graphviz
def render(name):
    '''Takes in graph name, outputs a pdf of graph'''
    g = Digraph(name)
    g.attr(size='10,8')
    g.attr('node', shape='circle')
    #get graph from dictionary
    graph = graphs[name]
    
    #getting nodes
    nodes = list(graph.keys())
    
    #node connections as tuples stored in list
    arcs = []
    
    #nested loop for arcs
    for key in graph.keys():
        for sub_key in graph[key]:
            arcs.append((key, sub_key))
            
    #looping through nodes creating them
    for node in nodes:
        g.node(node)
        
    #looping through edges
    for arc in edges:
        g.edge(arc[0], arc[1], label=str(random.randint(1, 5)))
    
    #saving graph
    g.render(f"{name}", 'graph_graphics')
    
    #inform of completion
    print("Graph pdf Generated")


# In[ ]:




