def retrocontador(n):
    print("{},".format(n), end = "")
    if n > 0:
        retrocontador(n-1)
        

retrocontador(10)