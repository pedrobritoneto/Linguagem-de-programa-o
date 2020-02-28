
def divisores (n):
    i = 1
    while i <= n:
        if n % i == 0:
            print (i)
        i = i + 1

num = int (input('digite um numero'))
divisores (num)