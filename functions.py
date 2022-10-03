#With def we decide in python to use a function and give it a name. The containing parts must be indented.
#In this function I inserted a variable person.
def greetings(person):
    print("Good evening " + person + ".")
#Call function and define the variable content of person.
greetings("Karl")

#Return modifier returns information to us from the function.
def calculator(num_1, num_2):
    return int(num_1) * int(num_2)    
#Outside the fuction we ask from user for the input of the numbers.    
num_1 = input("Give me your first number:")
num_2 = input("Give me your second number:")
#Then we print the output of the called function. 
print(calculator(num_1, num_2))