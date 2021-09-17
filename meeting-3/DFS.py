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
def DFS(u, n):
    S = []
    C = []
    for i in range(n + 1):
        S.append(0)
        C.append(0)
    top = 1
    S[top] = u
    while top > 0:
        u = S[top]
        top = top - 1
        if C[u] == 1:
            continue
        print('%d' % u, end = '\t')
        C[u] = 1
        for j in range(1, n + 1):
            v = n + 1 - j
            if G[u][v] != 0 and C[v] == 0:
                top = top + 1
                S[top] = v

#-------------------
def main():
    n = init('.\meeting-3\data\graph-g4.inp', G)
    print('Xem ma tran G: ', end = '\n')
    view_matrix(G, n)
    u = 1   # start
    DFS(u, n)
if __name__ == '__main__':
    main()
