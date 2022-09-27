survivals = ["Rick", "Michonne", "Daryl", "Abraham", "Glenn", "Shane", "Carl"]
attributes =["strong", "leader", "hunter", "smart", "ruthless", "shooter", "samurai"]
survivals.extend(attributes)
print(survivals)
survivals.append("Hershel")
print(survivals)
survivals.insert(15, "is dead")
print(survivals[0:])
survivals.remove("Shane")
print(survivals)
survivals.pop()
print(survivals)
print(survivals.index("Glenn"))
print(survivals.count("leader"))
survivals.sort()
attributes.reverse
print(survivals)
survivals_lost = survivals.copy
print(survivals_lost)
survivals.clear()
print(survivals)