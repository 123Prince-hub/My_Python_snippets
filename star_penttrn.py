# # num = int(input("Enter Your Number :-\n"))

# for row in range(1, 5):
#     for col in range(1, 5):
#         if (col <= row):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for row in range(1, 5):
#     for col in range(1, 5):
#         if col >= 5-row:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
 

# for row in range(1, 5):
#     for col in range(1, 5):
#         if col<=5-row:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for row in range(1, 5):
#     for col in range(1, 5):
#         if col>=row:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for row in range(1, 5):
#     for col in range(1, 8):
#         if col >=5-row and col<=3+row:
#             print("*", end=" ")
#         else:   
#             print(" ", end=" ")
#     print()


# for row in range(1, 5):
#     for col in range(1, 8):
#         if col >=row and col <=8-row :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for row in range(1, 5):
#     for col in range(1, 8):
#         if col<=5-row or col>=3+row:
#             print("*", end=" ")
#         else:
#              print(" ", end=" ")
#     print()


# for row in range(1, 6):
#     for col in range(1, 6):
#         if (col <=6- row):
#             print(6-col, end=" ")
#         else:
#             print(" ", end=" ")
#     print()




# def Fibonacci(n):
# 	if n < 0:
# 		print("Incorrect input")
# 	elif n == 0:
# 		return 0
# 	elif n == 1 or n == 2:
# 		return 1
# 	else:
# 		return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(int(input("Enter Your Number \n"))))




# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     else:
#         return n * factorial(n - 1)
# number = int(input("Enter Your Numebr :-\n"))
# print(factorial(number))


# def fibonachi(n):
#     if (n==1):
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonachi(n - 1) + fibonachi(n - 2)
# number = int(input("Enter Your Numebr :-\n"))
# print(fibonachi(number))



# num = input("Enter Your Number \n")
# order = len(num)
# num2 = 0
# for i in range(len(num)):
#     num2 = num2 + int(num[i])**order
# if int(num) == num2:
#     print("This is armstrong number")
# else:
#     print("This is not armstrong number")




# import requests
# url = "https://api.twitter.com/2/users/310679156/tweets"
# payload={}
# headers = {
#   'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAPX6VgEAAAAAO79eTP1ruiVDb5DPpkpigNQ7gRc%3D4ig3I5gccyj3Aef35xuQJIk4CUDNUKWvq16dNKjrToxMseGBbL',
#   'Cookie': 'guest_id=v1%3A163679722583515377; personalization_id="v1_0ZTOAdRa8ysK+tTBexrw1w=="'
# }
# response = requests.request("GET", url, headers=headers, data=payload)
# print(response.text)




# for row in range(1, 5):
#     for col in range(1, 8):
#         if (col <= row) or (col >= 8-row):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for row in range(2, 5):
#     for col in range(1, 8):
#         if (col <= 5-row) or (col >= 3+row):
#             print("*", end=" ")
#         else:
#             print(' ', end=" ")
#     print()


# for row in range(1, 5):
#     for col in range(1, 8):
#         if (col >=row) and (col <= 8-row):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for row in range(2, 5):
#     for col in range(1, 8):
#         if (col >= 5-row) and (col <= 3+row):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for row in range(1, 5):
#     for col in range(1, 5):
#         if col <= row:
#             print('*', end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for row in range(2, 5):
#     for col in range(1, 5):
#         if col <= 5-row:
#             print("*", end=" ")
#         else:
#             print(" ", end=' ')
#     print()




#tringle shape star pettern
# for i in range(1, 7+1):
#     print(" "*(7-i)+"* "*i)