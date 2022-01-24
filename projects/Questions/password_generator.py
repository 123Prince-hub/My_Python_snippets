# ******************************* Method 1 ***********************************

import string as s
from random import *

ch = s.ascii_letters + s.digits + s.punctuation
password = "".join(choice(ch) for x in range(randint(8, 16)))
print(password)


# ******************************* Method 2 ***********************************

import random
import string as s

print('Hello, Welcome to Password generator')
length = int(input('\nEnter the lenth of password:  '))

lower = s.ascii_lowercase
upper = s.ascii_uppercase
num = s.digits
symbol = s.punctuation

all = lower + upper + num + symbol
temp = random.sample(all, length)
password = "".join(temp)
print(password)



# ******************************* Method 3 ***********************************

import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password =  "".join(random.sample(s, passlen))
print (password)



# ******************************* Method 4 ***********************************

import string as s
from random import *
ch = s.ascii_letters + s.digits + s.punctuation

password = "".join(choice(ch) for x in range(randint(8, 16)))
print(password)