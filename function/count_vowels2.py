#Count Vowels in a String
def vowel_count(word):
    vowels="aeiouAEIOU"
    count=0
    for letter in word:
        if letter in vowels:
            count=count+1
    return count
print("the vowels in the word is",vowel_count("apple"))
