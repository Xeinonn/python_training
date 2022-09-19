#Simple calculator, adds full and decimal numbers.
num_1 = input("Give me a number:")
num_2 = input("Give me the second number:")
#calculated = int(num_1) + int(num_2) -Commented out, because it uses only full numbers with no possibility of using the decimal numbers.
#The float function alows to input and use decimal numbers.
calculated = float(num_1) + float(num_2)

print(calculated)
#Note: standard user input converts to a string. I use the float function in the variable calculated to convert the input into a number.