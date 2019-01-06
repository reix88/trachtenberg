# -*- coding: utf-8 -*-

# |------------------------------------|
# |TRAXTENBERG-SYSTEM UNREAL PRIMERS...|
# |------------------------------------|

import random

# Author: Anti-Social
# Creation Date: 31.12.2018
# Last Change: 05.01.2019
# Verion: 1.3
# Созданно при поддержке Lil Uzi Vert & Scarlxrd.

pravilno = 0
ne_pravilno = 0

def schet(one , two):
    global pravilno
    global ne_pravilno

    if one == two:
        pravilno = pravilno + 1
    else:
        ne_pravilno = ne_pravilno + 1

input("Press Enter to START...")

print("\n----------------\nУМНОЖЕНИЕ НА 11:\n----------------\n")

i = 0
while i < 5:
    i = i + 1

    int_1 = random.randrange(101, 10000, 1)
    print("Пример № " + str(i) + ":  " + str(int_1) + " x 11 = ?")
            
    while True:
        try:
            otv = int(input())
        except ValueError:
            print('Введите число!')
        else:
            break
            
    src = int_1 * 11
    schet(otv, src)


print("\n----------------\nУМНОЖЕНИЕ НА 12:\n----------------\n")

i = 0
while i < 5:
    i = i + 1

    int_1 = random.randrange(101, 10000, 1)
    print("Пример № " + str(i) + ":  " + str(int_1) + " x 12 = ?")
    
    while True:
        try:
            otv = int(input())
        except ValueError:
            print('Введите число!')
        else:
            break
            
    src = int_1 * 12
    schet(otv, src)


print("\n---------------\nУМНОЖЕНИЕ НА 9:\n---------------\n")

i = 0
while i < 5:
    i = i + 1

    int_1 = random.randrange(101, 10000, 1)
    print("Пример № " + str(i) + ":  " + str(int_1) + " x 9 = ?")
    
    while True:
        try:
            otv = int(input())
        except ValueError:
            print('Введите число!')
        else:
            break
            
    src = int_1 * 9
    schet(otv, src)


print("\n---------------\nУМНОЖЕНИЕ НА 8:\n---------------\n")

i = 0
while i < 5:
    i = i + 1

    int_1 = random.randrange(101, 10000, 1)
    print("Пример № " + str(i) + ":  " + str(int_1) + " x 8 = ?")
    
    while True:
        try:
            otv = int(input())
        except ValueError:
            print('Введите число!')
        else:
            break
            
    src = int_1 * 8
    schet(otv, src)


print("\n-----------------------------------\nУМНОЖЕНИЕ ДВУЗНАЧНЫХ НА ДВУЗНАЧНЫЕ:\n-----------------------------------\n")

i = 0
while i < 5:
    i = i + 1

    int_1 = random.randrange(10, 100, 1)
    int_2 = random.randrange(10, 100, 1)
    print("Пример № " + str(i) + ":  " + str(int_1) + " x " + str(int_2) + " = ?")
    
    while True:
        try:
            otv = int(input())
        except ValueError:
            print('Введите число!')
        else:
            break
            
    src = int_1 * int_2
    schet(otv, src)


print("\n----------------------\nМНОГОЗНАЧНЫЕ МНОЖИМЫЕ:\n----------------------\n")

i = 0
while i < 5:
    i = i + 1

    int_1 = random.randrange(100, 1000, 1)
    int_2 = random.randrange(10, 100, 1)
    print("Пример № " + str(i) + ":  " + str(int_1) + " x " + str(int_2) + " = ?")
    
    while True:
        try:
            otv = int(input())
        except ValueError:
            print('Введите число!')
        else:
            break
            
    src = int_1 * int_2
    schet(otv, src)


print("\n----------------------\nУМНОЖЕНИЕ ЛЮБОЙ ДЛИНЫ:\n----------------------\n")

i = 0
while i < 5:
    i = i + 1

    int_1 = random.randrange(100, 99000, 1)
    int_2 = random.randrange(100, 2000, 1)
    print("Пример № " + str(i) + ":  " + str(int_1) + " x " + str(int_2) + " = ?")
    
    while True:
        try:
            otv = int(input())
        except ValueError:
            print('Введите число!')
        else:
            break
            
    src = int_1 * int_2
    schet(otv, src)


print("\n------------------------------\nВОЗВЕДЕНИЕ В КВ. (ОКАН. НА 5):\n------------------------------\n")

i = 0
while i < 9:
    arr_five = [15, 25, 35, 45, 55, 65, 75, 85, 95]

    for x in arr_five:
        print("Пример № " + str(i) + ":  " + str(x) + " x " + str(x) + " = ?")
        
        while True:
            try:
                otv = int(input())
            except ValueError:
                print('Введите число!')
            else:
                break
            
        src = x * x
        i = i + 1
        schet(otv, src)


print("\n-----------------------------\nВОЗВЕДЕНИЕ В КВ. (НАЧ. НА 5):\n-----------------------------\n")

i = 0
while i < 8:
    arr_five2 = [51, 52, 53, 54, 56, 57, 58, 59]

    for x in arr_five2:
        print("Пример № " + str(i) + ":  " + str(x) + " x " + str(x) + " = ?")
        
        while True:
            try:
                otv = int(input())
            except ValueError:
                print('Введите число!')
            else:
                break
            
        src = x * x
        i = i + 1
        schet(otv, src)


print("\n---------------------\nВОЗВЕДЕНИЕ В КВАДРАТ:\n---------------------\n")

i = 0
while i < 6:
    i = i + 1

    int_1 = random.randrange(10, 100, 1)
    print("Пример № " + str(i) + ":  " + str(int_1) + " x " + str(int_1) + " = ?")
    
    while True:
        try:
            otv = int(input())
        except ValueError:
            print('Введите число!')
        else:
            break
            
    src = int_1 * int_1
    schet(otv, src)

# Количество правильных ответов
print("\nКол.во правильных отв: " + str(pravilno) + " - Кол.во не правильных отв: " + str(ne_pravilno))

# Процент
no_cof = (ne_pravilno * 100) / 58
cof = 100 - no_cof
print("\nПроцент правильных: " + str(cof) + "% - Процент не правильных: " + str(no_cof) + "%\n")

# Запись Лога
f = open("log.txt", 'a+')
f.write("Кол.во правильных отв: " + str(pravilno) + " - Кол.во не правильных отв: " + str(ne_pravilno) + 
"\n" + "Процент правильных: " + str(cof) + "% - Процент не правильных: " + str(no_cof) + "%\n\n")
f.close()

# Закончить программу
while True:
    suka = input("Введите 'Z' чтобы закрыть программу: ")
    
    if str.lower(suka) == "z":
        break
