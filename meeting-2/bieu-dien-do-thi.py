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
        # k = string.index(' ') # k = 1
        # str = string[0:k] # str = [0:1] = 1
        # i = int(str, base = 10) # i = 1
        # m = string.index(' ', k + 1, -1) # m = 4
        # str = string[k+1:m] # str = 2
        # j = int(str, base = 10) # j = 2
        # str = string[m+1:len(string)] # str = 1
        # x = int(str, base = 10) # x = 1
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
def main():
    n = init('.\data\graph.inp', G)
    print('Xem ma tran G: ', end = '\n')
    view_matrix(G, n)
if __name__ == '__main__':
    main()
