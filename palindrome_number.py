def palindrome_number(x):
    return str(x) == str(x)[::-1]

print(palindrome_number(-121))