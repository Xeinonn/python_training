#Create basic if statements and test stuff. I tested the operators or, and, not. You have to uncomment some line to check everything and 
Eugene = False
Iov = False
Valentina = True
Planinc = True
#If one of both Variables is used, the output will be positive, otherwise the message down will be printed.
if Eugene and Iov:
   print("Hello Eugene, what can I do for you?")
#elif Valentina and not(Planinc):
    #print("Hello senior Family Member Valentina, what can I do for you?")
#elif Iov or not(Valentina):
    #print("Hello family Member, you are welcome.")
#elif not(Eugene) and not(Iov):
    #print("Welcome Eugene!")
elif not(Valentina) and not(Planinc):
    print("You are not Valentina, access to this property is not granted.")
#I checked if my reversion worked as planed by printing the reversed variables. 
#Set the 2 Variables at the top of the code to FALSE and they will be transformed to TRUE and you will get the output.
print(not Valentina)
print(not Planinc)
#else:
    #print("You are not authorised for access.")