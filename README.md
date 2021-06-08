# Unique-Shortest-Paths-via-the-isolation-lemma
Repo for my masters project, Unique Shortest Paths via the isolation lemma. All implementation done in Python.

Project Description:
The goal of this project is to understand and visualize the isolation lemma, where the set F is the set of all s-t-paths in a directed graph. 
The user inputs this graph in a convenient manner and inputs the number m. Then the algorithm randomises the lengths of the arcs in a range from 1 to m and then finds 
a shortest s-t-path using Dijkstra's algorithm. This s-t-path is presented to the user. 
Moreover, the algorithm outputs the probability (from Ta-Shma's estimate) that this shortest s-t-path is unique. 
This requires an efficient implementation that counts the number of s-t-paths.
