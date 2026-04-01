"""
1. Get input number n from user. Print all the factors of n.
2. Get a List of to do tasks from the user and add it to a to_do list. Print the list.
3. Given an array of integers. Find a peak element in it. An array element is a peak if it is NOT smaller
 than its neighbours.
 For corner elements, we need to consider only one neighbour. Eg: in [3,4,6,7,5] - 7 is a peak element.
4. List = [3,4,5,-2,-1,2,8,0,-4]. Move all negative numbers to the end of the list.
"""
List = [3,4,5,-2,-1,2,8,0,-4]
List.sort(reverse=True)
print(List)
