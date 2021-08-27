#!/usr/bin/env python
# coding: utf-8

# # Directed Graphs

# File that holds graph dictionaries for testing bound accuracy

# In[40]:


from graphviz import Digraph


# ### To-Do:
# - add graphviz ability to output a selected graph
#     - e.g. user calls all_graphs(), picks 'medium4', calls draw('medium4')
# - test out user adding in graph with function, passing in dictionary

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


# In[42]:


#getter for graph name param
def get(graph_name):
    return graphs[graph_name]


# In[43]:


#shows all available graphs for user
def all_graphs():
    return list(graphs.keys())


# In[44]:


#draw a graph with graphviz
def draw(name):
    #initialize graph
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




