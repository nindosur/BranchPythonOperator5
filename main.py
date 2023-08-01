# 1
VTrue = True
while (VTrue):
    MTrue = True
    while(MTrue):
        user_time = int(input("Введите время в секундах: "))
        if (user_time<=86400)and(user_time>=0):
            print("Меню программы: ")
            MTrue = False
        else:
            print("Ввод некорректен!")
    print(" 1 - отображение в часах;\n 2 - отображение в минутах;\n 3 - отображение в секундах;\n 0 - выход из программы.")
    value_switch = int(input("Введите режим отоброжения: "))
    if(value_switch==1):
        print("До полуночи осталось ", int((86400-user_time)/3600), " часов.")
    elif(value_switch==2):
        print("До полуночи осталось ", int((86400-user_time)/60), " минут.")
    elif(value_switch==3):
        print("До полуночи осталось ", 86400-user_time, " секунд.")
    elif (value_switch == 0):
        print("Выход из программы...")
        VTrue = False
    else:
        print("Неправильный ввод. Введите значение от 1 до 3.")

# 2
value1 = int(input("Введите диаметр окружности: "))
print(" 1 - площадь;\n 2 - периметр окружности.")
value2 = input("Выберите пункт: ")
if(value2=='1'):
    print("Площадь окружности составляет - ", int(3.14*value1))
elif(value2=='2'):
    print("Периметр окружности составляет - ", int(2*3.14*(value1/2)))
else:
    print("Значение некорректно!")

# 3
value3 = int(input("Введите стоимость одной приставки: "))
value4 = int(input("Введите колличество приставок: "))
value5 = int(input("Введите скидку: "))
itog = (value3/100)*value5
print(" 1 - общую сумму заказа;\n 2 - стоимость одной приставки с учетом скидки.")
value6 = int(input("Выберите пункт: "))
if(value6==1):
    print("Общая сумма заказа составляет: ", value3*value4, "рубля.")
elif(value6==2):
    print("Стоимость одной приставки с учетом скидки составляет: ", itog, "рубля.")
else:
    print("Введите корректное значение!")

# 4
value7 = int(input("Введите размер файла в гигайбайтах: "))
value8 = int(input("Введите скорость интернет соединения в битах в секунду: "))
print(" 1 - часы;\n 2 - минуты;\n 3 - секунды")
value9 = int(input("Выберите пункт рассчета: "))
bit = value7*100000
if(value9==1):
    print("Файл скачается за ", value8/bit/3600," часов")
elif(value9==2):
    print("Файл скачается за ", value8/bit/60," минут")
elif(value9==3):
    print("Файл скачается за ", value8/bit," секунд")
else:
    print("Введите корректное значение!")

# 5
value10 = int(input("Введите количество часов: "))
if(value10>=0)and(value10<=5):
    print("Good night")
elif(value10>=6)and(value10<=12):
    print("Good morning")
elif(value10>=13)and(value10<=16):
    print("Good day")
elif(value10>=17)and(value10<=24):
    print("Good evening")
else:
    print("В сутках всего 24 часа!")
