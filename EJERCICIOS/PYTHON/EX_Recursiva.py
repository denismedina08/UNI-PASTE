# def fat(n):
#     if n ==0:
#         return 1
#     else:
#         return n*fat(n-1)

# n = int(input("Imforme um número: "))
# print(fat(n))

# # Exercicios
# def fib(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# Bucle for por lineas(row)
# matrix = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]

# for row in matrix:
#     print(row)


# # Bucle for por columnas
# matrix = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]

# for row in matrix:
#     for element in row:
#         print(element)


# Bucle for por lineas y columnas
matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()