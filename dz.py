def palindrome(string):
    if string == string[::-1]:
        print(True)
    else:
        print(False)


palindrome('level')
palindrome('chahc')
palindrome('hello')