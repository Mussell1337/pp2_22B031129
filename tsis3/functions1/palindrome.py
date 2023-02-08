def palindrome(arg):
    rev_arg = arg[::-1]
    if rev_arg == arg:
        print("This word is palindrome")
    else:
        print("This word is not palindrome")


sample = "madam"
palindrome(sample)