# palindrome

word = input("enter the string:")
reverse_word = word[::-1]
if reverse_word == word:
    print("palindrome")
else:
    print("not palindrome")
