def input_data():
    n = int(input('n = '))
    return n
#-------------
def factorial(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s
#------------
def main():
    n = input_data()
    s = factorial(n)
    print('%d'%n, '! = %d'%s)
#-------------
if __name__=='__main__':
    main()