#Palindrome Checker
def palindrome(word):
    reverse = word[::-1]
    if word == reverse:
        return "palindrome"
    else:
        return"not palindrome"
print(palindrome("apple"))