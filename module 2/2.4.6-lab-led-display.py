def led_display(num):
    # digit dictionary
    digits = {
        0: ["###", "# #", "# #", "# #", "###"],
        1: ["  #", "  #", "  #", "  #", "  #"],
        2: ["###", "  #", "###", "#  ", "###"],
        3: ["###", "  #", "###", "  #", "###"],
        4: ["# #", "# #", "###", "  #", "  #"],
        5: ["###", "#  ", "###", "  #", "###"],
        6: ["###", "#  ", "###", "# #", "###"],
        7: ["###", "  #", "  #", "  #", "  #"],
        8: ["###", "# #", "###", "# #", "###"],
        9: ["###", "# #", "###", "  #", "  #"]
    }

    num_str = str(num)
    
    for i in range(5):
        value = ""
        for digit in num_str:
            value += digits[int(digit)][i] + " "
        print(value)

number = int(input("Enter a number to view it\'s LED display correspondent:"))
led_display(number)
