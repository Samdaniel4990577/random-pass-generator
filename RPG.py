import random

print("welcome to random passsword generator")
randomechars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%"
nbrofpwds = int(input("Please enter the number of password to be generator: "))
pwdlen = int(input("Please enter the length of the password needed: "))

print("Here are your random passwords:")
for x in range(nbrofpwds):
    pwd = ""
    for chars in range(pwdlen):
        pwd = pwd + random.choice(randomechars)
    print(pwd)    
