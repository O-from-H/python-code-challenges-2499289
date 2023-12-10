import sys

eingabe = False
liste=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print(liste)

while eingabe == False:
    print("Bitte geben Sie eine Zahl zwischen 0 und 9 ein: ")
    wert = input()

    liste=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

    print(liste)

    if wert in liste:
        print("Die Zahl ist: " + wert)
        eingabe = True
    elif wert.isnumeric() and len(wert) > 1:
        wert_len = len(wert)
        erste_ziffer = str(wert)[:1]
        print("Deine Die Zahl hat " + str(wert_len) + " Ziffern. Wir wollten aber nur eine Ziffer haben! \nDie erste Ziffer ist: " + erste_ziffer)
    else:
        print("Da darf nur eine einstellige Zahl stehen, sonst nüscht!")
