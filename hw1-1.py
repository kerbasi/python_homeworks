# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

day_number = int(input("Введите номер дня недели:"))
if 5 < day_number < 8:
    print("Введенный день является выходным")
elif(0 < day_number < 6):
    print("Введенный день не является выходным")
else:
    print(print("Введен неверный формат дня"))