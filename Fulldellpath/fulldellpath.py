'''
Небольшой код для полного удаления файла. Без возможности восстановления в изначальном виде.
Моя реализация весьма необычна. Для большей уверенности следует увеличить значения overwrite.
'''
import random
import os

def Path(path):
    if path[-3:] != "txt": #если расширение не txt.
        newpath = path[:-3] + "txt" #создаем переменную с новым путем в котором расширение txt.
        os.rename(path, newpath) #меняем расширение на txt.
        return newpath #возвращаем полный путь с новым расширением.
    else: #иначе возвращаем полный путь с старым расширением.
        return path
def Del(inpath):
    path = Path(inpath)
    #-------------------------------------------------------
    overwrite = 15 #количество перезаписей.
    #-------------------------------------------------------
    cycle = 0
    while cycle != overwrite: #обычно файл не востановить после 10ти перезаписей.
        i = 0  # счетчик
        file = open(path, "r", encoding="ANSI")
        l = len(file.read()) #считываем кол. символов в файле.
        file = open(path, "w", encoding="ANSI")
        file.write("") #удаляем все символы в файле.
        file = open(path, "a", encoding="ANSI")
        if l <= 500: # если символов меньше или равно 150, изменить кол символов на 150.
            l = 500 # это нужно для удоления пустых текстовых файлов, или файлов с кодом.
        while i != l: #пока счетчик не равно кол. символов - создай случайное число от 1 до 9 и запиши его в файл.
            ran = random.random() #создадим случайное число.
            ran = str(ran)
            ran = ran[2:3] #обрежем 0. и остаток для получения целого числа от 1 до 9.
            file.write(ran)
            i += 1 #счетчик +1.
        cycle += 1 #цикл +1.
        file.close() #закрываем файл.
    os.remove(path) #удаляем файл после обработки.

langue = input("Ur langue:    ru/en?\ninput:    ")
if langue == "ru" or langue == "russia" or langue == "r" or langue == "Ru" or langue == "1":
    print("Напишите полный путь к файлу, включая его название и расширение.")
    print(r"Пример: C:\path\path\path\Hello.txt" + "\n")
    inpath = input(r"Полный путь:   ")
    Del(inpath) # передаем путь функции.
    print("Удалено!")
if langue == "en" or langue == "english" or langue == "e" or langue == "En" or langue == "2":
    print("Write full path, including name and extension.")
    print(r"Example: C:\path\path\path\Hello.txt" + "\n")
    inpath = input(r"Full path:   ")
    Del(inpath) # передаем путь функции.
    print("Delated!")
else:
    print("Wrong! type correct langue!")