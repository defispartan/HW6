ef test_cycle(path):
    # Check that our path is hamiltonian 
    if set(path) != vertex_set:
        # print("NOT EVERYTHING")
        # print(set(path))
        # print(vertex_set)
        print("NO")
        return 
    # Check that every edge actually exists 
    for i in range(len(path) - 1):
        if not (path[i], path[i + 1]) in edges:
            # print("EDGE: ", path[i], " to ", path[i + 1], " does not exist")
            print("NO")
            return
    # Check that it is a cycle
    if not (path[-1], path[0]) in edges:
        # print("NOT A CYCLE")
        print("NO")
        return
    # If it satisfies all these, it must be a hamiltonian cycle
    print("YES")


# Get params 
line = input()
line = line.split(" ")
n = int(line[0])
m = int(line[1])

vertex_set = set((i for i in range(n)))

# Construct edge dictionary 
edges = set()
for i in range(m):
    line = input()
    line = [int(i) for i in line.split()]
    # Undirected graph assumption
    edges.add((line[0], line[1]))
    edges.add((line[1], line[0]))

t = int(input())
for j in range(t):
    line = input()
    line = [int(j) for j in line.split()]
    test_cycle(line)
