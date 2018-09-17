## 1-1. Finding an Exit from a Maze.
*Given an undirected graph and two distinct vertices u and v, check if there is an path between u and v.*

**Input:** An undirected graph with n vertices and m edges. The next line contains two vertices u and v of the graph.

**Output:** 1 if there is a path between u and v and 0 otherwise.

## 1-2. Adding Exits to a Maze.
*Given an undirected graph with n vertices and m edges, compute the number of connected components in it.*

**Input:** An undirected graph with n vertices and m edges.

**Output:** The number of connected components.

## 2-1. Checking Consistency of CS Curriculum.
*Check whether a given directed graph with n vertices and m edges contains a cycle.*

**Input:** A directed graph with n vertices and m edges.

**Output:** 1 if the graph contains a cycle and 0 otherwise.

## 2-2. Determining an Order of Courses.
*Compute a topological ordering of a given directed acyclic graph (DAG) with n vertices and m edges.*

**Input:** A graph

**Output:** Any topological ordering of its vertices.

## 2-3. Checking Whether Any Intersection in a City is Reachable from Any Other.
*Compute the number of strongly connected components of a given directed graph with n vertices and m edges.*

**Input:** A graph.

**Output:** The number of strongly connected components.

## 3-1. Computing the Minimum Number of Flight Segments.
*Given an undirected graph with n vertices and m edges and two vertices u and v, compute the length of a
shortest path between u and v.*

**Input:** A graph. The next line contains two vertices u and v.

**Output:** The minimum number of edges in a path from u to v, or -1 if there is no path.

## 3-2. Checking whether a Graph is Bipartite.
*Given an undirected graph with n vertices and m edges, check whether it is bipartite.*

**Input:** An undirected graph.

**Output:** 1 if the graph is bipartite and 0 otherwise.

## 4-1. Computing the Minimum Cost of a Flight.
*Given an directed graph with positive edge weights and with n vertices and m edges as well as two vertices
u and v, compute the weight of a shortest path between u and v.

**Input:** A directed graph. The next line contains two vertices u and v.

**Output:** The minimum weight of a path between u to v, or -1 if there is no path.

## 4-2. Detecting Anomalies in Currency Exchange Rates.
*Given a directed graph with possibly negative edge weights and with n vertices and m edges, check
whether it contains a cycle of negative weight.*

**Input:** A directed graph.

**Output:** 1 if the graph contains a cycle of negative weight and 0 otherwise.

## 4-3. Exchanging Money Optimally.
*Given a directed graph with possibly negative edge weights and with n vertices and m edges as well as its
vertex s, compute the length of shortest paths from s to all other vertices of the graph.*

**Input:** A directed graph.

**Output:** For all vertices i from 1 to n output the following on a separate line:
- "*", if there is no path from s to u;
- "-", if there is a path from s to u, but there is no shortest path from s to u.
- the length of a shortest path otherwise.

## 5-1. Building Roads to Connect Cities.
* The goal is to build roads between some pairs of the given cities such that there is a path between any two
cities and the total length of the roads is minimized. Given n points on a plane, connect them with segments 
of minimum total length such that there is a path between any two points.*

**Input:** The first line contains the number n of points. Each of the following n lines defines a point (x_i, y_i)

** Output:** The minimum total length of segments. The absolute value of the difference 
between the answer of your program and the optimal value should be at most 10^−6
. To ensure this, output your answer with at least seven digits after the decimal point. 

## 5-2. Clustering.
* Given n points on a plane and an integer k, compute the largest possible value of d such that the
given points can be partitioned into k non-empty subsets in such a way that the distance between any
two points from different subsets is at least d.*

**Input:** The first line contains the number n of points. Each of the following n lines defines a point
(xi , yi). The last line contains the number k of clusters.

**Output:** the largest value of d. The absolute value of the difference between the answer of
your program and the optimal value should be at most 10^−6.

## 6-1. Friend suggestion.
* Compute the distance between several pairs of nodes in the network. *

**Input:** The first line contains two integers 𝑛 and 𝑚 — the number of nodes and edges in the
network, respectively. The nodes are numbered from 1 to 𝑛. Each of the following 𝑚 lines contains
three integers 𝑢, 𝑣 and 𝑙 describing a directed edge (𝑢, 𝑣) of length 𝑙 from the node number 𝑢to the
node number 𝑣.
The next line contains an integer 𝑞 — the number of queries for computing the distance. Each of the
following 𝑞 lines contains two integers 𝑢 and 𝑣 — the numbers of the two nodes to compute the distance
from 𝑢 to 𝑣.

**Output:** For each query, output one integer on a separate line. If there is no path from 𝑢 to 𝑣,
output −1. Otherwise, output the distance from 𝑢 to 𝑣.

