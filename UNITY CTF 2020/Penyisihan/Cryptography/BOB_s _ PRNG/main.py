import string
from random import randint, shuffle
from os import urandom
from fastecdsa.curve import P256
from fastecdsa.point import Point

flag = "<REDACTED>"
USERNAME = "BOB"

# Create random password
p = list(string.ascii_letters+string.digits+string.punctuation)
shuffle(p)
PASSWORD = "".join(p[:8])

def mod_inv(a, m):
    return pow(a, m-2, m)

def sanity_check(P, Q, d):
    assert(d * Q == P)

def gen_pq():
    P = P256.G
    d = randint(2, 2**12)
    e = mod_inv(d, P256.q)
    Q = e * P

    sanity_check(P, Q, d)
    return P, Q, d

class ECPRNG():
    def __init__(self, seed, P, Q):
        self.seed = seed
        self.P = P
        self.Q = Q

    def genbits(self):
        t = self.seed
        s = (t * self.P).x
        self.seed = s
        r = (s * self.Q).x
        return r

def main():
    P, Q, d = gen_pq()
    seed = int.from_bytes(urandom(8), 'little')
    ecprng = ECPRNG(seed, P, Q)
    while True:
        print("[1] Login")
        print("[2] Forgot Password")
        print("[3] Maybe this is useful")
        print("[4] Exit")
        choice = input("> ")
        if choice == "1":
            user = input("Enter Username: ")
            pasw = input("Enter Password: ")
            if user == USERNAME and pasw == PASSWORD:
                print("You logged in..")
                print("Here is your flag {}".format(flag))
            else:
                print("Invalid username or password")
        elif choice == "2":
            secret_code = "{:02X}".format(ecprng.genbits())
            print("Secret code sent to BOB's email")
            code_sent = input("Enter secret code: ")
            if secret_code != code_sent:
                print("Invalild secret code ({})".format(secret_code))
                continue
            new_pasw = input("Enter new password: ")
            PASSWORD = new_pasw
            print("Password changed successfully")
        elif choice == "3":
            print('P = (0x{:x}, 0x{:x})'.format(P.x, P.y))
            print('Q = (0x{:x}, 0x{:x})'.format(Q.x, Q.y))
        elif choice == "4":
            print("Bye hackers!")
            break
        else:
            print("Input error")
main()
