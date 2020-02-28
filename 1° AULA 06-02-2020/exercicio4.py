def fatorial (n):
    fat = 1
    for i in range (n, 0, - 1):
        fat = fat * i
    return fat


n = int (input('Informe um numero: '))
f = fatorial(n)
print (f)
print (fatorial(n))