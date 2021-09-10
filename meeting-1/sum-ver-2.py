def input_data():
    print('Nhap 2 so a, b: \n')
    a = float(input('a = '))
    b = float(input('b = '))
    return a, b
#------------------
def sum(a, b):
    c = a + b
    return c
#------------------
def main():
    a, b = input_data()
    c = sum(a, b)
    print('Tong(%.2f'%a,',%.2f'%b, ')=%.2f'%c)
#-----------------
if __name__=='__main__':
    main()
