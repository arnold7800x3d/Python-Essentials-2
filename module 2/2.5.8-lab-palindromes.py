# Request for text input
text = input("Enter some text to check whether or not the text is a palindrome or not: ")
text = text.lower() # Have all characters in the text as lowercase characters
state = True # Variable to determine if text is a palindrome
text = text.replace(" ","") # Remove all spaces

for i in range(0, int(len(text)/2)): # Split the text 'array' by half
    if (text[i] != text[len(text)-i-1] or text[i] == " "): # Match each character in the first half with its correspondent in the second half
        state = False
        break
    
if state:
    print("It\'s a palindrome")
else:
    print("It\'s not a palindrome")
