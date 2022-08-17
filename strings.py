print ("Hello\nWorld")
print ("Backslashtest \\")
#            0123456789
meine_box = "DIE WELT iSt VielFÄltig"
#The content of the variable is printed in capital, then a true/false statement chechks if it is printed capital.
print(meine_box.upper().isupper())
#The len functions shows how many characters are use in the string.
print(len(meine_box))
#A string variable, in which the texts starts in the next line.
ich_in_der_box = "\nund ich bin ein Teil davon!."
#The first variable is printed in capital, while the second in low cases.
print(meine_box.upper() + ich_in_der_box.lower())
#The letter with the integer value of 6 is being printed.
print(meine_box[6])
#Index function prints the integer number of the certain letter in the string.
print(meine_box.index("E"))
#Replace function replaces the certain value in your variable to the specific one.
print(meine_box.replace("DIE", "The"))