# # join tow dictionary method1
# dic1 = {"stephen":"follow"}
# dic2 = {"youtube":"subscribe"}
# print({**dic1, **dic2})


# # join tow dictionary method2
# dic1 = {"stephen":"follow"}
# dic2 = {"youtube":"subscribe"}
# print(dic1 | dic2)


# # multification oprator working with string data type
# a = "prince"
# print(a*2*True)


# # ****************** Quiz 1 ****************
# l = [1, 2, 3, 4]
# if 3 in l:
#     l.remove(3)
# print(l[2])


# # ****************** Quiz 2 ****************
# def f(n):
#     if n==0:
#         return 0
#     else:
#         return f(n-1)+100
# print(f(3))


# # ****************** Quiz 3 ****************
# print("The sum of {0} and {1} is {2}".format(2,10,12))


# # ****************** Quiz 4 ****************
# # print(type(evel('{1,2,3}')))

# a, b = input("marks \n").split()
# print(a)
# print(b)









# ========================================================================================================================
# **************************************   Python String Formating Type  ************************************************
# ========================================================================================================================


person = {'name':'prince', "age":23}


# **************************************   Type 1st  ************************************************
sentence = 'My Name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)


# **************************************   Type 2nd  ************************************************
sentence = "My name is {} and I am {} years old.".format(person['name'], person['age'])
# sentence = "My name is {0[name]} and I am {1[age]} years old.".format(person, person)
# sentence = "My name is {0[name]} and I am {0[age]} years old.".format(person)
# sentence = "My name is {name} and I am {age} years old.".format(**person)
# sentence = "My name is {name} and I am {age} years old.".format(name='Prince', age='24')
print(sentence)


# **************************************   Type 3rd (create HTML tag)  ************************************************
tag = 'h1'
txt = 'This is a Heading'

sentence = '<{0}>{1}</{0}>'.format(tag, txt)
print(sentence)


# **************************************   Type 4th (Class Oops)  ************************************************
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Prince', '24')
sentence = "My name is {0.name} and I am {0.age} years old".format(p1)
print(sentence)


# **************************************   Type 5th (In For Loop)  ************************************************
for i in range(1, 11):
    # sentence = 'The value is {}'.format(i)
    sentence = 'The value is {:02}'.format(i)
    print(sentence)


# **************************************   Type 6th (Decimal Places)  ************************************************
pi = 3.14159265
# sentence = 'Pi is equal to {}'.format(pi)
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)


# **************************************   Type 7th (add charectors)  ************************************************
# sentence = '1 MB is equal to {} bytes'.format(10000**2)
# sentence = '1 MB is equal to {:,} bytes'.format(10000**2)
sentence = '1 MB is equal to {:,.2f} bytes'.format(10000**2)
print(sentence)


# **************************************   Type 7th (Date Format)  ************************************************
from datetime import datetime
my_date = datetime(2018, 9, 24, 12, 30, 45)
print(my_date)
# sentence = '{}'.format(my_date)
sentence = '{:%d %b, %Y}'.format(my_date)
print(sentence)

#************* Date type 2
sentence = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(my_date)
print(sentence)











# ========================================================================================================================
# **************************************   Automate Parsing & Renaming Of Multiple Files  *******************************
# ========================================================================================================================

