#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Împăratul a primit serie de mesaje importante pe care este
important să le descifreze cât mai repede.

Din păcate mesagerul nu a apucat să îi spună împăratul care au fost
cheile alese pentru fiecare mesaj și tu ai fost ales să descifrezi
misterul.

Informații:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe poziția aflată
la un n pași de ea în alfabet (unde este n este un număr întreg cunoscut
"""
# pylint: disable=unused-argument

from __future__ import print_function


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    cheie = ord(mesaj[0]) - ord('a')
    msj = ""
    for curent in mesaj:
        if ord('a') <= ord(curent) <= ord('z'):
            copie = chr((ord(curent) - cheie))
            if ord(copie) < ord('a'):
                curent = chr(26 + ord(copie) + cheie)
            msj += chr((ord(curent) - cheie))
        else:
            msj += curent
    print(msj)


def main():
    """ Main function docstring """
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)

if __name__ == "__main__":
    main()