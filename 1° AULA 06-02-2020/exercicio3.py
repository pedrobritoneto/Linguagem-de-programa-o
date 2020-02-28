salario = float(input("Informe o salario"))
if salario < 2000:
    salarionovo = salario*0.15 + salario
else: 
    salarionovo = salario*0.07 + salario
print ('salario reajustado é', salarionovo)



