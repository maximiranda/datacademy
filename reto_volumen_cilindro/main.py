import math

def cylinder_vol(diameter, height):
    volume = round((((math.pi) * (diameter ** 2)) / 4) * height)
    return volume


def sphere_vol(radius):
    volume = round((4 * math.pi * (radius ** 3)) / 3, 2)
    return volume


def cone_vol(radius, height):
    volume = round((cylinder_vol((2 * radius), height) / 3), 2)
    return volume


def tetrahedron_vol(base_triangle, height_triangle, height):
    volume = round((1 / 3) * ((base_triangle * height_triangle) / 2) * height, 2)
    return volume


def run():
    option = int(input("""Bienvenido a la calculadora de volumenes, puedes elegir 4 opciones:
                            1 - Calcular volumen del cilindro
                            2 - Calcular volumen de la esfera
                            3 - Calcular volumen del cono
                            4 - Calcular volumen del tetrahedro
                                Tu opcion: """))
    
    if option == 1:
        diameter = int(input("""Para calcular el volumen del cilindro necesitas dos datos:
                                1 - Diametro de la base: """))
        height = int(input("""
                                2 - Altura: """))
        print(f"el volumen del cilindro con altura: {height} y diametro de base: {diameter} es igual a: {cylinder_vol(diameter, height)}")
    
    
    elif option == 2:
        radius = int(input("""Para calcular el volumen de la esfera necesitas:
                                . radio de la esfera: """))
        print(f"el volumen de la esfera con radio: {radius} es igual a: {sphere_vol(radius)}")
    
    
    elif option == 3:
        radius = int(input("""Para calcular el volumen del cono necesitas:
                                1 - radio de la base: """))
        height = int(input("""
                                2 - altura del cono: """)) 
        print(f"el volumen del cono con altura: {height} y radio de base: {radius} es igual a: {cone_vol(radius, height)}")
    
    
    elif option == 4:
        base_triangle = int(input("""Para calcular el volumen del tetrahedro necesitas tres datos:
                                1 - Base del triangulo: """))
        height_triangle = int(input("""
                                2 - Altura del triangulo: """))
        height = int(input("""
                                2 - Altura del tetrahedro: """))

        print(f"el volumen del tetrahedro con altura: {height} y area de la base: {((base_triangle * height_triangle) / 2)} es igual a: {tetrahedron_vol(base_triangle, height_triangle, height)}")
    
    
    else:
        print("elige una opcion valida")
        run()
                            

if __name__ == '__main__':
    run()