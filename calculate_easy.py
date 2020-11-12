def welcome():
    print("Добро пожаловать в калькулятор ")

def calculate():

    a = float(input("Ввидите значение 1: "))
    b = float(input("Ввидите значение 2: "))

    what = input("+/-/*/**/ / /%/ : ")

    if what == "+":
        c = a + b
        print("Результат: " + str(c))
    elif what == "-":
        c = a - b
        print("Результат: " + str(c))
    elif what == "*":
        c = a * b
        print("Результат: " + str(c))
    elif what == "**":
        c = a ** b
        print("Результат: " + str(c))
    elif what == "/":
        c = a / b
        print("Результат: " + str(c))
    elif what == "%":
        c = a % b
        print("Результат: " + str(c))
    else:
        print("Выбрана не верная операция! ")
    again()

def again():
    calc_again = input("Хочешь остаться пиши - Y: ")
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print("Увидимся ещё!")
    else:
        again()

welcome()
calculate()