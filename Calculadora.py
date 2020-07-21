calc = input("Escolha a operação = ")
#Multiplicação
if calc == 'multiplicação':
    a = int(input("Escreva o primeiro numero = "))
    b = int(input("Escreva o segundo numero = "))
    print(f"A Multiplicação entre {a} e {b} é igual a = {a * b}")
#Subtração
elif calc == "subtração":
    a = int(input("Escreva o primeiro numero = "))
    b = int(input("Escreva o segundo numero = "))
    print(f"A Subtração entre {a} e {b} é igual a = {a - b}")
#Soma
elif calc == "soma":
    a = int(input("Escreva o primeiro numero = "))
    b = int(input("Escreva o segundo numero = "))
    print(f"A Soma entre {a} e {b} é igual a = {a + b}")
#Divisão
elif calc == 'divisão':
    a = int(input("Escreva o primeiro numero = "))
    b = int(input("Escreva o segundo numero = "))
    print(f"A Divisão entre {a} e {b} é igual a = {a / b:.2f}")
else:
    print ("Comando invalido,tente novamente")
