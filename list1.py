#More work with lists and functions. In this one I created some characters from walking dead and made their characteristics in the list attributes.
survivals = ["Rick", "Michonne", "Daryl", "Abraham", "Glenn", "Shane", "Carl"]
attributes =["strong", "leader", "hunter", "smart", "ruthless", "shooter", "samurai"]
#Adds to the end of your list the addition from the list attributes.
survivals.extend(attributes)
print(survivals)
#Adds Hershel to the end of the list. This means he will be added after the word samurai in the list attributes.
survivals.append("Hershel")
print(survivals)
#After Hershel I added is dead with the insert funtion. Hershel has the index 15, so the insert is added after him.
survivals.insert(15, "is dead")
#We are printing everything in the list from 0 to end.
print(survivals[0:])
#Shane is removed from the list.
survivals.remove("Shane")
print(survivals)
#I removed the last element from the list (is dead).
survivals.pop()
print(survivals)
#Shows the index of element Glenn.
print(survivals.index("Glenn"))
#Counts how many elements (leader) are in the list.
print(survivals.count("leader"))
#Alphabetical sort of the list survivals, the appended list attributes is also affected.
survivals.sort()
#The list is reversed now and starts from Hershel but Alphabetically.
survivals.reverse()
print(survivals)
#Identical copy of the survivals list with all the modifications.
survivals_lost = survivals.copy()
print(survivals_lost)
survivals.clear()
print(survivals)