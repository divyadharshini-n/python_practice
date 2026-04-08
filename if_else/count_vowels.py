#vowel count and constant count

word=input("enter the word:")
vowels = "AEIOUaeiou"

vowel_count=0
constant_count=0

for char in word:
    if char in vowels:
        vowel_count+=1
    else:
        constant_count+=1

print("vowel count:",vowel_count)
print("constant count:",constant_count)
