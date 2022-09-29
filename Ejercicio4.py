# Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).
# ¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
# Sugerencia
# Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.

import operator

tareas = {"trabajo":1, "dormir":4, "cenar":3, "deberes":2}
tareas_ordenadas = sorted(tareas.items(), key=operator.itemgetter(1), reverse=False)

print(tareas_ordenadas)

