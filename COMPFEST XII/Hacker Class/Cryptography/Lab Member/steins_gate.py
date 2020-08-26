#!/usr/bin/env python
from Crypto.Cipher import AES
import itertools, os


class LabMember:
    __count = __import__('itertools').count(1)
    __secret_sets = itertools.cycle(os.environ['SECRET_TEXT'].split())
    del os.environ['SECRET_TEXT']

    def __init__(self, name):
        self.__number = next(self.__count)
        self.__secret = next(self.__secret_sets)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def divergence(self):
        aes = AES.new('supersecretvalue', AES.MODE_ECB)
        pad = (16 - len(self.__secret) % 16) * ' '
        enc = aes.encrypt(self.__secret + pad)
        return "0.%d" % int(enc.encode('hex'), 16)

    def __str__(self):
        return "Lab Member No. %03d: %s" % (self.__number, self.__name)

def main():
    names = 'Okabe Rintarou', 'Shinna Mayuri', 'Super Hacka "Daru"', 'Makise Kurisu', \
            'Kiryuu Moeka', 'Lukako', 'Faris', 'Suzuha Amane', 'Hiyajou Maho', \
            'Shinna Kagari', 'Yuki Amane'

    lab_members = [LabMember(name) for name in names]

    for member in lab_members:
        print(member)

    prompt = 'Please select a lab member (or 0 to break): '
    num = True
    while num:
        try:
            num = int(input(prompt))

            if num == 0:
                break

            selected = lab_members[num - 1]
            message = ("%s\n"
                       "%s\n"
                       "\n"
                       "Divergence level:\n"
                       "%s") % (selected, len(str(selected)) * '=', selected.divergence)
            print(message)
        except (Exception, TypeError, NameError, ValueError, IndexError):
            print("Please select from lab member 1 - 11")
            num = True

    print("May we meet again in the Steins;Gate")

if __name__ == '__main__':
    main()
