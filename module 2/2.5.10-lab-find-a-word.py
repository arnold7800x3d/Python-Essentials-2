# prompt user for multiple inputs
string1 = input("Enter the word to be searched: ")
string2 = input("Enter the character sequence in which the first string will be searched: ")

pos = 0
status = True

for char in string1:
    pos = string2.find(char, pos)
    if pos == -1:
        status = False
        break
    pos += 1  

# Output result
if status:
    print("Yes")
else:
    print("No")