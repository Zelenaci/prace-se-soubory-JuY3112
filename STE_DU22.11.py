from random import randint, choice
pismena = dict()
samohlasky = "aeiyou"
souhlasky = "qwrtpsdfghjklzxcvbnm"
try:

    soubor1 = input("Zadejte soubor ke čtení:")
    f_r = open(soubor1, 'r')
except FileNotFoundError:
    print("Soubor nenalezen!!!")
    exit(1)

try:

    soubor2 = open(input("Zadejte soubor k zápisu: "),"w")
except FileNotFoundError:
    print("Soubor nebyl nalezen!!!")

rezim = int(input("Co chcete se souborem udělat?\n[1] - Převest na malé písmena.\n[2] - Nahradit výskyt zadaného znaku jiným zadaný znakem.\n[3] - Vytvořit statistiku výskytu jednotlivých znaků v souboru.\n[4] - Generování náhodného textu.\n"))
if rezim == 1:
    data = f_r.read().lower()
    vystup = soubor2.write(data)
    print("Text ve vašem souboru byl uspěšně převeden na malé písmena :) ")
if rezim == 2:
    prevadeny = input("Jaký znak chcete převést?")
    prevedeny = input("Za jaký znak chcete tento znak zaměnit?")
    while True:
        data = f_r.read(1).upper()
        if data == prevadeny:
            data = prevedeny
        if data == "":
            break
        vystup = soubor2.write(data)
    print("Záměna byla úspěná :)")
if rezim == 3:
    while True:
        znak = f_r.read(1).upper()
        if znak == "":
            break
        if znak in pismena.keys():
            pismena[znak] += 1
        else:
            pismena[znak] = 1

    for znak in sorted(pismena.keys()):
        if znak.isalpha():
            vystup = soubor2.write("| {0} | -> | {1} |\n".format(znak, pismena[znak]))
    print("Statistika počtu znaků byla napsána do vámi zvoleného souboru :) ")
if rezim == 4:

    def word_gen(minchars=1, maxchars=9):
        data = ""
        pocet = randint(minchars, maxchars)
        if pocet == 1:
            zacatek = 0
        else:
            zacatek = randint(0, 1)
        for i in range(pocet):
            if i % 2 == zacatek:
                data = data + choice(samohlasky)
            else:
                data = data + choice(souhlasky)
                if randint(1, 10) == 1:
                    data = data + choice(souhlasky)
        return data



    def sentence_gen():
        data = ""
        slova = int(input("Kolik se přejete slov?"))
        for i in range(slova):
            data = data + word_gen() + " "
        return data.capitalize()[0:-1] + "."

    vystup = soubor2.write(sentence_gen())
    print("Vaše věta byla vygenerována do vámi zvoleného souboru :)")

