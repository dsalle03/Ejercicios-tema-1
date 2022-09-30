import operator
tareas = {"trabajo":1, "dormir":4, "cenar":3, "deberes":2}
tareas_ordenadas = sorted(tareas.items(), key=operator.itemgetter(1), reverse=False)

listOfKeys = tareas_ordenadas.keys()
print("Type of variable listOfKeys is: ", type(listOfKeys))

listOfKeys = list(listOfKeys)

print("Printing the entire list containing all Keys: ")
print(listOfKeys)

