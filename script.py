print("Задание 1: ".upper())
from sys import argv
file_name, worked_hour, rate, benefit = argv
calculation = (int(worked_hour) * int(rate)) + int(benefit)
print(f"our pay is equal {calculation}")