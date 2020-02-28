
def divisores (n):
    i = 1
    cont = 0
    while i <= n:
        if n % i == 0:
            cont = cont + i
        i = i + 1
    print (cont)
num = int (input('digite um numero'))
divisores (num)


'''def divisores1 (n):
    soma = 0
    for i in range (1, n, + 1):
        if n % i == 0
            soma +=i
    return soma

num = int (input('digite um numero'))
print (divisores(num))'''