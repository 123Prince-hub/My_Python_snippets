# ================================= Type 1 ==================================

def isPalindrome(s):
	return s == s[::-1]
# Driver code
s = input("Enter Your String\n")
ans = isPalindrome(s)

if ans:
	print("Yes! This is Palindrome string")
else:
	print("No! This is not a Palindrome string")



# ================================= Type 2 ==================================
def isPalindrome(s):	
	rev = ''.join(reversed(s))

	if (s == rev):
		return True
	return False

# main function
s = input("Enter Your String\n")
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")

