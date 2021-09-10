M = []
n = 10
#----------------------
def createArr(M, n):
    for i in range(n):
        M.append(int(input('Nhap so thu %d: ' % (i + 1))))
#------------------
def viewArr(M, n):
    for i in range(n):
        print(M[i], end = ' ')
    print()
#---------------------
def sumArr(M, n):
    s = 0
    for i in range(n):
        s = s + int(M[i])
    return s
#--------------
def sumLe(M, n):
    s = 0
    for i in range(n):
        if int(M[i]) % 2 != 0:
            s = s + int(M[i])
    return s
#------------
def sortArr(M, n):
    for i in range(n):
        for j in range(n):
            if int(M[j]) > int(M[j]):
                temp = M[i]
                M[i] = M[j]
                M[j] = temp
#--------------
def deleteArr(M, n, k):
    for i in range(k, n - 1):
        M[i] = M[i + 1]
    n = n - 1
    return n
#----------
def insertArr(M, n, k, x):
    for i in range(n, k):
        M[i + 1] = M[i]
    M[k] = x
    n = n + 1
    return n
#-------------------
def Input(x):
    try:
        n = int(input('Nhap ' + x + ': '))
        if n <= 0:
            exit()
        return n
    except: 
        print('Phai nhap so tu nhien')
        exit()
#---------
def main():
    n = Input('n')
    createArr(M, n)
    viewArr(M, n)
    s = sumLe(M, n)
    print('Tong: ', s, '\n')
    sortArr(M, n)
    viewArr(M, n)
    k = Input('k')
    m = deleteArr(M, n, k)
    viewArr(M, m)
    m = insertArr(M, m, 2, 100)
    viewArr(M, m)
#-----------------------
if __name__ == '__main__':
    main()