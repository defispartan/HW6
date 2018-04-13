def test_cycle(edges, path):
    iter = 0
    last = None
    while iter + 1 < len(path):
        tup = (int(path[iter]),int(path[iter + 1]))
        if last != None:
            reversed = (last[1], last[0])
            if tup == last or tup == reversed:
                return "NO"
        last = tuple(tup)
        found = False
        for edge in edges:
            if tup == edge:
                found = True
                break
            reversed_tup = (tup[1], tup[0])
            if reversed_tup == edge:
                found = True
                break
        if found == False:
            return "NO"

        iter += 1

    first = int(path[0])
    last_place = int(path[len(path)-1])
    tup = (first, last_place)
    if tup not in edges:
        reverse_tup = (tup[1], tup[0])
        if reverse_tup not in edges:
            return "NO"
    reversed = (last[1], last[0])
    if tup == last or tup == reversed:
        return "NO"
    return "YES"


line = input()
line = line.split(" ")
n = int(line[0])
m = int(line[1])

edges = []
for i in range(m):
    line = input()
    line = line.split(" ")
    a = int(line[0])
    b = int(line[1])
    edges.append((a,b))
    i += 1

t = int(input())
for j in range(t):
    line = input()
    line = line.split(" ")
    result = test_cycle(edges,line)
    print(result)
