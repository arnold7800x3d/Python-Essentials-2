def mysplit(string):
    words_list = []
    word = ""
    for i in range(len(string)):
        if string[i] == " ":
            if word != "":
                words_list.append(word)
                word = ""
        else:
            word += string[i]
    if word != "":
        words_list.append(word)
    return words_list

print(mysplit("To be or not to be, that is the question")) 
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))