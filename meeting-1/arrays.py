#------------ one dimension --------
m = []
n = 10
#---------------
def init(m, n):
    for i in range(n + 1):
        m.append(0)
#--------- 2 dimensions ----------
a = []
b = []
c = []
m = 2
n = 3
def init(a, m, n):
    for i in range(m + 1):
        a.append([])
        for j in range(n + 1):
            a[i].append(0)
#------------------
def create_matrix(a, m, n, c):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            x = int(input('%c[%d][%d] = '%(c, i, j)))
            a[i][j] = x
#-----------
def view_matrix(a, m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print('%d'%a[i][j], end = ' ')
        print()

#--------------
def sum_matrix(a, b, m, n):
    c = []
    init(c, m, n)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            c[i][j] = a[i][j] + b[i][j]
    return c
#----------
def main():
    init(a, m, n)
    print('Create matrix a: ', end = '\n')
    create_matrix(a, m , n, 'A')
    print('View matrix a: ', end = '\n')
    view_matrix(a, m , n)
    init(b, m, n)
    print('Create matrix b: ', end = '\n')
    create_matrix(b, m , n, 'B')
    print('View matrix b: ', end = '\n')
    view_matrix(b, m , n)
    c = sum_matrix(a, b, m, n)
    print('View matrix c: ', end = '\n')
    view_matrix(c, m, n)
#---------------
if __name__=='__main__':
    main()