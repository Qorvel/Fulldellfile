import os
import random

class FullDel:

    di = os.listdir()
    trash = []

    for i in di:
        if os.path.isdir(i) == False and i != "FullDel.py":
            trash.append(i)

    for i in trash:
        new = ""


        file = open(i,"rb")
        reader = file.read()
        file.close()
        for j in range(50):
            ran = random.random()
            ran = str(ran)[3]
            overwrite = str(ran)*len(reader)

            file = open(i,"w")
            file.write(overwrite)
            file.close()
        os.remove(i)
