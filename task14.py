# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input("Введите число N: "))
print("вывод всех чисел от 1 до N во второй степени:")
for i in range(1, num + 1):
    print(i**2, end = " ")

print("\nвывод всех чисел от 1 до N 2 в степени i:")
for i in range(1, num + 1):
    print(2 ** i, end = " ")        
