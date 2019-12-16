import math


#insight to go off of here is A * B = a(100,000) + b( 10,000) +c (1000) +c (100) + b(10) + a(1)
largest_palindrome = -1

def isPalindrome(num):
    num_str = str(num)
    if num_str[0:3] == num_str[3:6][::-1]:
        return True
    return False

def biggest_palindrome():
    global largest_palindrome

    a = 999
    b = 990
    for i in range(a,100, -1):
        if a % 11 != 0:
            for j in range(b, 100, -11):
                if isPalindrome(i*j):
                    if i*j > largest_palindrome:
                        largest_palindrome = i*j
        else:
            for j in range(b, 100, -1):
                if isPalindrome(i*j):
                    if i*j > largest_palindrome:
                        largest_palindrome = i*j

    print(largest_palindrome)

biggest_palindrome()