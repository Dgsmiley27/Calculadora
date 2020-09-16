from math import sqrt
print('''####################################################
#      bem vindo a calculadora feita em python     #
#    multiplicação = 1                             #
#    subtração = 2                                 #
#    soma = 3                                      #
#    divisão = 4                                   #
#    raiz = 5                                      #
####################################################''')
calc = input("Escolha a operação = ")
#Multiplicação
if calc == '1':
    a = int(input("Escreva o primeiro numero = "))
    b = int(input("Escreva o segundo numero = "))
    print(f"A Multiplicação entre {a} e {b} é igual a = {a * b}")
#Subtração
elif calc == "2":
    a = int(input("Escreva o primeiro numero = "))
    b = int(input("Escreva o segundo numero = "))
    print(f"A Subtração entre {a} e {b} é igual a = {a - b}")
#Soma
elif calc == "3":
    a = int(input("Escreva o primeiro numero = "))
    b = int(input("Escreva o segundo numero = "))
    print(f"A Soma entre {a} e {b} é igual a = {a + b}")
#Divisão
elif calc == '4':
    a = int(input("Escreva o primeiro numero = "))
    b = int(input("Escreva o segundo numero = "))
    print(f"A Divisão entre {a} e {b} é igual a = {a / b:.2f}")
#Raiz
elif calc =='5':
    a = int(input("Escreva o numero = "))
    print(f"a raiz de {a} é igual a {sqrt(a)}")
else:
    print ("Comando invalido,tente novamente")
