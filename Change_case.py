"""
    Name = Panchal Jay Manojkumar
    Id = 20CE068

    You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
    Sample Input: HackerRank.com presents "Pythonist 2".

    Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

    Github Link = https://github.com/jaypanchal1706/change_case.git

"""

# take the input as a string
str = input()
# Make a new string called newStr and insert with the changing the case
newStr = ""
# run the for loop
# and take the length of the string and check if the letter is uppercase or not if letter is uppercase it change to the lowercase and vice versa
for i in range (len(str)) :
    if str[i].isupper() :
        newStr += str[i].lower()
    elif str[i].islower() :
        newStr += str[i].upper()
    else :
        newStr += str[i]
# print the new string with mixture of the uppercase and lower case
print(newStr)