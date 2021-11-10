print("Задание 1: ".upper())
from sys import argv
file_name, worked_hour, rate, benefit = argv
print(f"our pay is equal {calculation}")
В чем ошибка? Ни в терминале, ни в run код не запускается!

print("Задание 2: ".upper())
#генератор
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)
#цикл
i = 0
new= []
for el in my_list:
    if el > my_list[i-1]:
        new.append(el)
    i+=1
print(new)

print("Задание 3: ".upper())
numbers = range(20, 241)
new_list = [el for el in numbers if el%20==0 or el%21==0]
print(new_list)

print("Задание 4:".upper())
from itertools import permutations
from itertools import repeat
from itertools import combinations
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in my_list if my_list.count(el)==1]
print(new)

print("Задание 5:".upper())
from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el
print(reduce(my_func, my_list))

print("Задание 6: ".upper())
from itertools import count
from itertools import cycle
def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)
def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1
my_count_func(start_number = int(input("enter start number: ")), stop_number = int(input("enter stop number: ")))
my_cycle_func(my_list = [1, 2], iteration = int(input("enter iteration: ")))

print("Задание 7: ".upper())
def fibo_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
my_fifteen = []
for el in fibo_gen(5):
    if i > 15:
        break
    else:
        my_fifteen.append(el)
        i += 1
print(my_fifteen)

