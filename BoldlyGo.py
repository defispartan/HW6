line = [int(i) for i in input().split()]
n = line[0]  # number of vertices
m = line[1]  # number of edges
k = line[2]  # number of vertices tested for 

edges = set()
# Collect all edges in a single set
for i in range(m):
    edge = tuple(int(i) for i in input().split())
    edges.add(edge)
    edges.add(edge[::-1])  # Undirected graph, add the other edge 

# Convert to independent set: we ask whether there exists an independent set of size n - k
independent_set_param = n - k

# Convert to the clique problem 
# There are n(n-1)/2 possible edges, of which m are occupied 
k_clique_param = int(n * (n-1)/2 - m)

print(n, k_clique_param, independent_set_param)

complement = []
# Now we just need to list all these edges 
for i in range(n):
    for j in range(i):
            if (i, j) not in edges:
                complement.append((min(i, j), max(i, j)))
           
complement.sort()
for edge in complement:
    print(edge[0], edge[1])
