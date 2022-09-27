family_members = ["Julia", "Jurii", "Valentina", "Dmitirii", "Eugene"]
#Print the content of the list.
print(family_members)
#Print f the specific value.
print(family_members[3])
#The first value is 0, in this example it is Julia.
print(family_members[0])
#We can print the value backwards, it starts from -1 and is Eugene.
print(family_members[-1])
#It prints from Valentina till the end.
print(family_members[2:])
#It prints from (1)Jurii to (4)Eugene, but Eugene is not included.
print(family_members[1:4])
#I changed the value with the mark 4(Eugene) to Jake. From this point the programm works with the name Jake. 
family_members[4] = "Jake"
print(family_members)