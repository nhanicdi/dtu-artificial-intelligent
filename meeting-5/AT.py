G = []
P = []
const = 10
#--------------------
def init_open(Open):
    for i in range(const):
        Open.append([])
        for j in range(2):
            Open[i].append(0)
#--------------------
def is_empty_open(Open):
    return len(Open) - Open.count(Open[0]) == 0
#--------------------
def add_q(Open, n, value, index):
    n = n + 1
    Open[n][0] = value
    Open[n][1] = index
    i = n
    while i > 1:
        j = int(i / 2)
        if Open[i][0] < Open[j][0]:
            Open[i], Open[j] = Open[j], Open[i]
        i = j
    return n
#--------------------
def remove_q(Open):
    value = Open[1][0]
    index = Open[1][1]
    n = len(Open) - Open.count(Open[0])
    Open[1][0] = Open[n][0]
    Open[1][1] = Open[n][1]
    Open[n][0] = 0
    Open[n][1] = 0
    n = n - 1
    i = 1
    while i <= int(n / 2):
        j = i * 2
        if j < n:
            if Open[j][0] > Open[j + 1][0]:
                j = j + 1
                if Open[i][0] > Open[j][0]:
                    Open[i], Open[j] = Open[j], Open[i]
        else:
            if Open[i][0] > Open[j][0]:
                Open[i], Open[j] = Open[j], Open[i]
        i = i + 1
    return value, index, n
#--------------------
def split_string(string):
    a, b, c = string.split(' ')
    return int(a), int(b), int(c)
#--------------------
def init_matrix(path, G):
    f = open(path)
    string = f.readline()
    n, a, z = split_string(string.replace('\t', ' '))
    for i in range(n + 1):
        G.append([])
        for j in range(n + 1):
            G[i].append(0)
    while True:
        string = f.readline()
        if not string:
            break
        i, j ,x = split_string(string.replace('\t', ' '))
        G[i][j] = G[j][i] = int(x)
    f.close()
    return int(n), int(a), int(z)
#--------------------
def view_matrix(G, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print('%d' %G[i][j], end = ' ')
        print()
#--------------------
def algorithm_for_tree(G, P, n, s, g):
    result = 0
    Close = []
    O = []
    for i in range(const):
        Close.append(0)
        O.append(0)
    Open = []
    init_open(Open)
    m = 0
    m = add_q(Open, m, result, s)
    O[s] = 1
    P[s] = s
    while not is_empty_open(Open):
        value, u, m = remove_q(Open)
        if u == g:
            result = value
        for v in range(1, n + 1):
            if G[u][v] != 0 and O[v] == 0 and Close[v] == 0:
                x = value + G[u][v]
                m = add_q(Open, m, x, v)
                O[v] = 1
                P[v] = u
        Close[u] = 1
        O[u] = 0
    return result
#--------------------
def print_path(P, n, s, g):
    Path = []
    for i in range(0, n + 1):
        Path.append(0)
    print('\nDuong di ngan nhat tu %d' %s, 'den %d' %g, 'la\nPath:', end = ' ')
    Path[0] = g
    i = P[g]
    k = 1
    while i!= s:
        Path[k] = i
        k = k + 1
        i = P[i]
    Path[k] = s
    for j in range(0, k + 1):
        i = k - j
        if i > 0:
            print('%d => ' %Path[i], end = ' ')
        else:
            print('%d ' %Path[i], end = ' ')
#--------------------
def main():
    n, s, g = init_matrix('.\meeting-5\data\graph.inp', G)
    print('n: %d' %n, end = '\n')
    view_matrix(G, n)
    for i in range(0, n + 1):
        P.append(0)
    result = algorithm_for_tree(G, P, n, s, g)
    print_path(P, n, s, g)
    print('\nresult: %d' %result, end = '\n')
if __name__ == '__main__':
    main()

