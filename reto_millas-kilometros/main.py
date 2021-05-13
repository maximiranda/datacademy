def mi_a_km(mi):
    return  round((1.60934 * mi), 2)


def km_a_mi(km):
    return round((0.621371 * km), 2)


def run():
    opcion = int(input("""Bienvenido al conversor de Millas-Kilometros
                Elije una opcion:
                    1 - Millas a Kilometros
                    2 - Kilometros a Millas 

                    """))
    if opcion == 1:
        millas = int(input("Millas: "))
        print(f"{millas} millas equivalen a {mi_a_km(millas)} Kilometros ")


    elif opcion == 2:
        kilometros = int(input("Kilometros: "))
        
        print(f"{kilometros} Kilometros equivalen a {km_a_mi(kilometros)} millas")

    else:
        print("por favor elija una opcion correcta")
        run()

if __name__ == '__main__':
    run()