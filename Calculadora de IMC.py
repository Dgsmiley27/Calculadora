#Pergunta o peso da pessoa
peso = int(input("Digite o peso da pessoa: "))
#Pergunta a altura da pessoa
alt = int(input("Digite a altura da pessoa: "))
#Envia na tela a resposta
print (f"o imc da pessoa é = {peso / (alt*alt):.4}")
#Envia na tela a resolução
print (f"resolução \n {peso} kg / {alt} m x {alt} m = {peso / (alt*alt):.4}")
