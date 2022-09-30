import operator

tareas = {"trabajo":1, "dormir":4, "cenar":3, "deberes":2}
tareas_ordenadas = sorted(tareas.items(), key=operator.itemgetter(1), reverse=False)

print(tareas_ordenadas)

