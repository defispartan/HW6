import itertools

line = input()
line = line.split(" ")
n = int(line[0])
m = int(line[1])
k = int(line[2])
inputs = [i for i in range(n)]
old_edges = []
for i in range(m):
    line = input()
    line = line.split(" ")
    a = int(line[0])
    b = int(line[1])
    old_edges.append((a,b))
    i += 1
total_edges = itertools.combinations(inputs,2)
new_edges = []
for edge in total_edges:
    if edge not in old_edges:
        new_edges.append(edge)
new_k = n - k
print(str(n) + " " + str(len(new_edges)) + " " + str(new_k))
for edge in new_edges:
    print(str(edge[0]) + " " + str(edge[1]))