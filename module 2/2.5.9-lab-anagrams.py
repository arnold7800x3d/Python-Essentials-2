introduction = """
Welcome to the anagram checker. Enter your texts separately at the prompts
"""
print(introduction)

text1 = input("First text: ").lower().replace(" ", "") # first text input
text2 = input("Second text: ").lower().replace(" ", "") # second text input

if not text1 or not text2: # check if either input is empty
    print("Not anagrams")
else:
    state = True # anagram state

    for char in text1: # iterate through each character of the first string
        if char not in text2: # check if the character is present in the second string
            state = False 

    if state:
        print("Anagrams")
    else:
        print("Not anagrams")

