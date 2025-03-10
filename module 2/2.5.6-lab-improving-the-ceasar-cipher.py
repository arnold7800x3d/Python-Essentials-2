# Request for message input
message = input("Enter the message you wish to be encrypted: ")

# Request for shift value
shift_value = int(input("Enter the shift value for the encryption (Range: 1 - 25): "))

cipher = "" # variable to store the final encrypted text

# Ensure the value provided is in the range
if shift_value not in range(1, 26):
    shift_value = int(input("Invalid choice. Enter a valiu between 1 and 25: "))
    
# Loop over characters in the message
for char in message:
    if not char.isalpha(): # Check if character is an letter
        cipher += char # Add to cipher if not a letter to simply output
        continue

    code = ord(char) + shift_value # Get the code for the character
    
    # Handle the letter if it is in uppercase or lowercase
    if char.isupper():
        if code > ord('Z'):
            code -= 26
    elif char.islower(): 
        if code > ord('z'):
            code -= 26
    
    cipher += chr(code) # Increment the cipher string

print(cipher) # Print the cipher string
