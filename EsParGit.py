def esPar(n):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Introduce un número"))
if esPar(num):
    print("El número {} es par".format(num))
else:
    print("El número {} no es par".format(num))