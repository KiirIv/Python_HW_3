# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X 

n = int(input()) 
a = list(map(int, input().split()))  
x = int(input()) 
closest = a[0]
for element in a:
    if abs(element - x) < abs(closest - x):
        closest = element 
print(closest)
