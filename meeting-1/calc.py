def input_data():
    print('Nhap 2 so a, b:\n')
    a = float(input('a = '))
    b = float(input('b = '))
    return a, b
#--------------
def sum(a, b):
    c = a + b
    return c
#---------------
def subtract(a, b):
    c = a - b
    return c
#-------------
def multiply(a, b):
    return a * b
#------------
def division(a, b):
    if b == 0:
        print('Division by zero')
        exit()
    return a / b
#---------------
def main():
    a, b = input_data()
    c = sum(a, b)
    print(a, ' + ', b, ' = ', c)
    c = subtract(a, b)
    print(a, ' - ', b, ' = ', c)
    c = multiply(a, b)
    print(a, ' * ', b, ' = ', c)
    c = division(a, b)
    print(a, ' / ', b, ' = ', c)
#----------------
if __name__=='__main__':
    main()