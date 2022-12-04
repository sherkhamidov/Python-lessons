# son topish
import random

def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"men 1 dan {x} gacha son o'yladim. Topa olaszmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("kattaroq son ayting", end="")
        elif taxmin> tasodifiy_son:
            print("kichikroq son ayting", end="")
        else:
            print("yutdingiz!")
            break

        print(f"Tabriklayaman. {taxminla} ta taxmin bilan topdingiz")
        return taxminlar


def sontop_pc(x=10):
    input(f"1 dan{x}gacha son o'ylangva istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar+= 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(
            f"Siz {taxmin} sonini o'yladingiz; tog'ri (t),"
            f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
        )
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar


def play(x=10):
    yana = True
    while yana:
        taxminlar_pc = sontop_pc(x)
        taxminlar_user > sontop(x)

        if taxminlar_user> taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdimv va yutdim!")
        elif taxminlar_user< taxminlar_pc:
            print(f"siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("durrang")
        yana= int(input("yana o'ynaymizmi? ha(1)/yoq(0):"))


play()