# propmt user for birthday input
birthday = input("Enter your birthday in format YYYYMMDD: ")

while len(birthday) > 1:
    digit_of_life = 0 # variable for the final sum
    
    # iterate over the digits 
    for char in birthday:
        digit_of_life += int(char)
    birthday = str(digit_of_life)

print("Digit of life is: " + birthday)
