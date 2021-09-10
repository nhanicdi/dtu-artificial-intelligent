import math
def input_data():
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    return a, b

#-------------------
def solve_equal(a, b):
    if a == 0:
        if b == 0:
            print('Vo so nghiem')
        else:
            print('Vo nghiem')
    else:
        x = -b / a
        print('Nghiem x = %.3lf'%x, end = '\n')
#---------------------
def main():
    a, b = input_data()
    solve_equal(a, b)
if __name__=='__main__':
    main()