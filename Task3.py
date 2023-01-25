# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


n = int(input('Enter N: '))
if n > 0:
    for i in range(-n, n):
        print(f'{i}, ', end='')
    print(n)
if n < 0:
    for i in range(n, -n, 1):
        print(f'{i}, ', end='')
    print(-n)

# num = int(input('введите число = '))
# new_list = range(-num, num+1, 1)
# print(*new_list)

# num = int(input("Введите число N: "))
# for number in range(-num, num+1):
#     print(number, end=', ')


# num = int(input('введите число 1 = '))
# my_list = range(-num, num + 1)
# print(*my_list, sep=', ')
# print(list(my_list))

