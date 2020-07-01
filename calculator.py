import time
import sys
print("Приветствую вас в своем калькуляторе!\nЗдесь вы сможете сложить/вычесть/умножить/разделить два числа.")
a = (input("Введите первое число и нажмите ENTER.\n"))
try:
    a = float(a)
except (ValueError) as a:
    print("до связи.")
    time.sleep(1.5)
    sys.exit()
b = (input("Введите второе число и нажмите ENTER.\n"))
try:
    b = float(b)
except (ValueError) as b:
    print("до связи.")
    time.sleep(1.5)
    sys.exit()
znak = input("Введите знак и нажмите ENTER.(+,-,*,/)\n")
if znak != '+' and znak != '-' and znak != '*' and znak != '/':
    print("до связи")
    time.sleep(1.5)
    sys.exit()
if b == 0 and znak == "/":
    print("хорошая попытка.")
    time.sleep(3)
    sys.exit()
if znak == "+":
    c = (a+b)
    if str(c)[-2:] == ".0":
        print("Результат равен:", str(c)[:-2])
    else:
        print("Результат равен:", (c))
if znak == "-":
    c = (a-b)
    if str(c)[-2:] == ".0":
        print("Результат равен:", str(c)[:-2])
    else:
        print("Результат равен:", (c))
if znak == "*":
    c = (a*b)
    if str(c)[-2:] == ".0":
        print("Результат равен:", str(c)[:-2])
    else:
        print("Результат равен:", (c))
if znak == "/":
    c = (a/b)
    if str(c)[-2:] == ".0":
        print("Результат равен:", str(c)[:-2])
    else:
        print("Результат равен:", (c))
input("Работа программы завершена.\nЧтобы выйти из программы,нажмите ENTER.\n")
