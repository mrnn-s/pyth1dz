#Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
#и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

day = int(input('Введите номер дня недели: '))
if day == 6 or day == 7:
    print('Этот день выходной')
if day <= 5 and day >= 1:
    print('Этот день рабочий')
else:
    print('Это не день недели')