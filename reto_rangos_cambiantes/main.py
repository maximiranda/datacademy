
def rango_cambiante(lower, upper, number):

    if  lower <= number <= upper:
        print(f"Tu número: {number} esta dentro del rango")
    
    elif number < lower:
        print(f"Tu número: {number} está por debajo del rango")
        number = int(input("Ingresa un numero mayor: "))
        rango_cambiante(lower, upper, number)
    elif number > upper:
        print(f"Tu número: {number} está por arriba del rango")
        number = int(input("Ingresa un numero menor: "))
        rango_cambiante(lower, upper, number)


if __name__=="__main__":

    lower = int(input("Ingresa el limite inferior del rango: "))
    upper = int(input("Ingresa el limite superior del rango: "))
    number = int(input("Ingresa el número deseado: "))
    rango_cambiante(lower,upper, number)
