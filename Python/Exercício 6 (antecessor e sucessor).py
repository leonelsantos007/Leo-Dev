# Programa que lê um número inteiro e mostra o seu antecessor e o seu sucessor

# Solicitando o número 
numero = int(input("Digite um número: "))

# Mostrando o antecessor e sucessor
antecessor = numero - 1
sucessor = numero + 1
print(f"O antecessor de {numero} é {antecessor}")
print(f"O sucessor de {numero} é {sucessor}")