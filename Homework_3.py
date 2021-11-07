print("Задание 1".upper())
def first_func():
    try:
        arg_1 = int(input("Введите число: "))
        arg_2 = int(input("Введите число: "))
    except ValueError:
        return ValueError
    except ZeroDivisionError:
        return division_on_zero
    chastnoe = int(arg_1//arg_2)
    return chastnoe
print(first_func())

print("Задание 2".upper())
def person_data(**kwargs):
    return kwargs
print(person_data(name = "Роман", surname = "Харламов", year_of_birsday = str("20 марта 1985 г."), town = "Moscow", email = "www.leningrad.ru", phone = str(777777777)))

print("Задание 3".upper())
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
print(f'Result - {my_func(int(input("enter first argument: ")), int(input("enter second argument: ")), int(input("enter third argument: ")))}')

print("Задание 4".upper())
def my_func(x, y):
    return x ** abs(y)
print(my_func(2, -3))

print("Задание 5".upper())
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')
my_sum()

print("Задание 6".upper())
def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()
