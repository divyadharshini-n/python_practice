#numbers
list = [1,2,3,4,5]
for i in list:
    print(i)

#string
s_list = ["dog"]
for i in s_list[0]:
    print(i)

#if list contains many strings
m_list = ["dog","cat","bat"]
for word in m_list:     # gives only words
    for char in word:   # gives the character
        print(char)

