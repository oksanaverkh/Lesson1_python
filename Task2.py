# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


# num1 = int(input('num 1 = '))
# num2 = int(input('num 2 = '))
# num3 = int(input('num 3 = '))
# num4 = int(input('num 4 = '))
# num5 = int(input('num 5 = '))

# max = num1

# if max < num2:
#     max = num2
#     if max < num3:
#         max = num3
#         if max < num4:
#             max = num4
#             if max < num5:
#                 max = num5


max = 0
# n = 1
for i in range(5):
    num = int(input(f'Enter number {i+1}: '))
    if num > max:
        max = num
    # n += 1
print(f'Max is {max}')


# def get_numbers(num): 
#     list = []
#     for i in range(num):
#         list.append(int(input('Введите число: '))) append adds an element in the end of the list
#     return list
    

# def find_max(list):
#     max = list[0]
#     for i in list:
#         if i>max:
#             max = i
#     return max

# list = get_numbers(5)
# print(find_max(list))


# list = (-1, 4, 118, 7, 8)

# max = list[0]
# for i in  range(1,len(list)):
#     if list[i] > max:
#         max = list[i]
# print(max)

