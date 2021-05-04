import random
import hashlib
from itertools import combinations
import time
import datetime


def convert(n):
    return str(datetime.timedelta(seconds=n))

line = 1
def goto(linenum):
    global line
    line = linenum


start_time = time.time()


U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L = "abcdrfghijklmnopqrstuvwxyz"
D = "0123456789"
S = " !@#$%^&*()_-=+|/+?~"

length = int(input("Input length of the password:"))
print("For next 4 questions answer \"y\" or \"n\"")
uppercase = input("Do you want that the password will include uppercase letters?")
lowercase = input("Do you want that the password will include lowercase letters?")
digits = input("Do you want that the password will include a digits (0-9)?")
symbols = input("Do you want that the password will include a symbols like !@#...?")

string = ""
if uppercase == "y":
    string = string + U
if lowercase == "y":
    string = string + L
if digits == "y":
    string = string + D
if symbols == "y":
    string = string + S

print("Possible symbols are:\n", string, sep="")
print("Password length is:", length)
password = ""

for i in range(1, length + 1):
    password = password + random.choice(string)
    i += 1
print("Password is:", password, sep="")

password_md5 = hashlib.md5(password.encode())
print("MD5 hash is:", password_md5.hexdigest(), sep="")

#BRUTE FORCE

crack = []
comb = ""
STRING = U + L + D + S

print("Building list of combinations...")

for sym1 in STRING:
    comb = sym1
    print(comb)
    crack.append(comb)
    for sym2 in STRING:
        comb = sym1 + sym2
        print(comb)
        crack.append(comb)
        for sym3 in STRING:
            comb = sym1 + sym2 + sym3
            print(comb)
            crack.append(comb)
            for sym4 in STRING:
                comb = sym1 + sym2 + sym3 + sym4
                print(comb)
                crack.append(comb)
                # for sym5 in STRING:
                #   comb = sym1 + sym2 + sym3 + sym4 + sym5
                #   print(comb)
                #   crack.append(comb)
                #   for sym6 in STRING:
                #       comb = sym1 + sym2 + sym3 + sym4 + sym5 + sym6
                #       crack.append(comb)


print("Building list time: ", convert(time.time() - start_time))
print("Combination's qty:", len(crack))

print("Brute forcing...")


for i in crack:
    if i == password:
        print("Your password is:", i)


print("Brute force time:", convert(time.time() - start_time))
exit()


