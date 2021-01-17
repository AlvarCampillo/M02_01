def maxi(*l):
    if len(l) == 0:
        return 0
    n = l[0]
    for ix in range(1, len(l)):
        if l[ix] > n:
            n = l[ix]
    return n

def mini(*l):
    if len(l) == 0:
        return 0
    n = l[0]
    for ix in range(1, len(l)):
        if l[ix] < n:
            n = l[ix]
    return n

funciones = {"min": mini,
             "max": maxi}

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    
    return None

print(returnF("max")(1, 3, 8, 5, 6))
print(returnF("min")(1, 3, 8, 5, 6))
