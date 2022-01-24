# import math
# a = 5.3
# print(math.ceil(a))             # return furture roundup value

# b = -6
# print(math.fabs(b))             # return positive number of any negetive number and give float value

# c = 5
# print(math.factorial(c))        # return factorial of any number

# d = 5.7
# print(math.floor(d))            # return back roundup value

# e = [2, 8, 1, 4]
# print(math.fsum(e))             # return total of complete list in float value

# f = 36
# print(math.sqrt(f))             # return square root of any number in float value




# num = int(input("Enter Your Number :-\n"))
# fac = ""
# for i in range(2, num):
#     if num % i == 0:
#         fac = fac + str(i) + ","
# else:
#     print("noooooo")
# print(fac)

# st = input("Enter Your String :-\n")
# re = input("Enter Your String :-\n")

# if len(re)>=1:
#     print(st.replace(re, ""))
# else:
#     print(st)



# txt = input("Enter Your String :5-\n")
# remove_lettr = input("Enter Your String :-\n")
# count = 0
# for i in range(len(txt)):
#     if txt[i] == remove_lettr:
#         count = count + 1
# print(count)
    
# def anagramCheck(str1, str2):
#     if (sorted(str1) == sorted(str2)) :  
# 	    return True 
#     else :  
# 	    return False 
    
# str1 = input("Please enter String 1 : ")
# str2 = input("Please enter String 2 : ")
# if anagramCheck(str1,str2):
#     print("Anagram")
# else:
#     print("Not an anagram")


# str1 = input("Enter Your String First :-\n")
# str2 = input("Enter Your String Second :-\n")

# if sorted(str1) == sorted(str2):
#     print("This is anagram string")
# else:
#     print("This is not anagram string")



## check prime number or not
# def isprime(num):
#     for n in range(2, int(num**1/2)+1):
#         if num % n == 0:
#             return "Not a Prime Number"
#     return "Prime Number"
# num = int(input("Enter Your Number :-\n"))
# print(isprime(num))




# def sum_of_digits(num):
#     if num <10:
#         return num
#     else:
#         return num % 10+ sum_of_digits(num/10)
# num = int(input("Enter Your Number :-\n"))
# num = sum_of_digits(num)
# print("Sum of numbers %d" % num)


# # lcm
# def calculate_lcm(x, y):
#     if x > y: 
#         greater = x  
#     else:  
#         greater = y  
#     while(True):  
#         if((greater % x == 0) and (greater % y == 0)):  
#             lcm = greater  
#             break  
#         greater += 1  
#     return lcm      
# num1 = int(input("Enter first number: "))  
# num2 = int(input("Enter second number: "))  
# print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2))  




# ***********************************  Function to find HCF   ***********************************
# num1 = int(input("Enter first number: "))  
# num2 = int(input("Enter second number: ")) 
# if num1>num2:
#     mn = num2
# else:
#     mn = num1
# for i in range(1, mn+1):
#     if (num1 % i == 0) and (num2 % i==0):
#         hcf = i
# print("HCF is :", hcf)


# ***********************************  Function to find LCM   ***********************************
# num1 = int(input("Enter first number: "))  
# num2 = int(input("Enter second number: ")) 
# if num1<num2:
#     mx = num2
# else:
#     mx = num1
# while(True):
#     if (mx % num1==0) and (mx % num2==0):
#         break
#     mx+=1
# print("LCM is ", mx)



# l = [1, 2, 3, 4]
# if 3 in l:
#     l.remove(3)
# print(l[2])
# print(l)






