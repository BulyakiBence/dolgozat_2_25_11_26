# #A csoport
# Szimuláljuk egy 20 oldalú D&D kocka 100 db dobását! A dobásokat egy listában tároljuk! Majd oldjuk meg a következő feladatokat!
# Minden feladat előtt a program írja ki a feladat sorszámát!

# 1. Volt-e 6-os a dobások között?
# 2. Hányadikra sikerült először 18-nál nagyobbat dobni?
# 3. Hány darab 1-est dobtak?
# 4. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?
# 5. Mennyi a 4-es dobások szorzata?
import random
import math
dobasok = []
tizennyolcnal_nagyobb = []
egyesek = []
tiznel_kisebbek = []
negyes_dobasok = [] 
negyes_dobasok_szorzata = []
for i in range(101):
    i = random.randint(1,20)
    dobasok.append(i)
print("--------------/n")
print(f"Eddigi számok: {dobasok}")
print("1. feladat")
if 6 in dobasok:
    print("Volt 6-os a dobások között")

else:
    print("Nem volt 6-os dobásod")
print("--------------/n")        

print("2. feladat")
for szam in dobasok:
    if szam > 18:
        tizennyolcnal_nagyobb.append(szam)
if len(tizennyolcnal_nagyobb) > 0:
    print(f"A tizennyolcnál nagyyobb szám helye:{dobasok.index(len(tizennyolcnal_nagyobb))+1}")
else:
    print("Nem volt 18-nál nagyobb dobásod.")
print("----------------/n")
print("3.feladat")
if 1 in dobasok:
    for szam in dobasok:
        if szam == 1:
            egyesek.append(szam)
if len(egyesek) > 0:
    print(f"Ennyi egyes volt benne: {len(egyesek)}")

else:
    print("Nem volt benne 1-es.")
print("------------------/n")
print("4. feladat")
for szam in dobasok:
    if szam < 10:
        tiznel_kisebbek.append(szam)
if len(tiznel_kisebbek) > 0:
    print(f"Tíznél kisebbek között a legnagyobb: {max(tiznel_kisebbek)}")
    print(f"Ennek helye: {dobasok.index(max(tiznel_kisebbek)) + 1}")
else:
    print("Nem volt 10-nél kisebb dobás.")
print("--------------------/n")
print("5. feladat")
if 4 in dobasok:
    for szam in dobasok:
        if szam == 4:
            negyes_dobasok.append(szam)          
print(f"Négyzetük: {int(math.pow(4, len(negyes_dobasok)))}")





