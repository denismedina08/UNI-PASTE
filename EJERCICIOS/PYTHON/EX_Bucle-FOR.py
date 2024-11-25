# Exercicio 1
# Eccreva um programa para encontrar a soma S = 3 + 6 + 9 + 333.
# soma = 0

# for i in range(3,334,3):
#     soma += i
#     print(soma)

# Exercicio 2
# soma = 0

# for i in range(10):
#     nota = float(input('Imforme a nota'))
#     soma += nota
#     media = nota/10
#     print(media)

# Exercicio 3
# n = int(input('Digite um número de 1 a 10'))

# if n < 0 or n > 10:
#     print('Valor invalido!')

# else:
#     for i in range(1,10):
#         print(i,'X', n,"=" ,i*n)

# Exercicio 4
# soma = 0

# for i in range(10):
#     sal = int(input('Informe o salário: '))
#     soma += sal

# Exercicio 5
# Um numero natural é primo se ele possui apenas dois divisores distintos. Assim, um número
# maior que 1 é primo se for divisível apenas por si próprio e por 1. Crie um programa que imprime
# se um numero é primo ou não.
n = int(input('Digite um número: '))
contador = 0

if n <= 1:
    print('Não e um número primo')
else:
    for i in range(1, n):
        if n % i == 0:
            print('E um número primo')

