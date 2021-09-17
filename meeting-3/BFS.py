G = []
#-------------
def init(path, G):
    f = open(path) # the number of lines equals to the number of sides of the graph
    n = int(f.readline(), base = 10) # n = 8
    for i in range(n + 1):
        G.append([])
        for j in range(n + 1):
            G[i].append(0)
    while True:     # example with line: 1 2 1
        string = f.readline()  # string = 1 2 1
        if not string:
            break
        string = string.replace('\t', ' ') # replace tab character with space
        i, j, x = (string.split(' ')) # destructuring: https://riptutorial.com/python/example/14981/destructuring-assignment
        i = int(i)
        j = int(j)
        x = int(x)
        G[i][j] = G[j][i] = x # G[1][2] = G[2][1] = 1
    f.close() # close the file
    return n
#------------------
#-----------
def view_matrix(G, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print('%d'%G[i][j], end = ' ')
        print()
#------------------
def BFS(u, n):
    Q = []
    C = []
    for j in range(n + 1):
        Q.append(0)
        C.append(0)
    first = 1
    last = 1
    Q[last] = u
    C[u] = 1
    while first <= last:
        u = Q[first]
        first = first + 1
        print('%d' %u, end = '\t')
        for v in range(1, n + 1):
            if G[u][v] != 0 and C[v] == 0:
                last = last + 1
                Q[last] = v
                C[v] = 1

#-------------------
def main():
    n = init('.\meeting-3\data\graph-bfs-g1.inp', G)
    print('Xem ma tran G: ', end = '\n')
    view_matrix(G, n)
    u = 1   # start
    BFS(u, n)
if __name__ == '__main__':
    main()
