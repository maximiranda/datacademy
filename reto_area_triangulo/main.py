

def area_triangulo(base, height):
    
    area = (base * height) // 2

    return area



def run():

    b = int(input("Cual es la base de tu triangulo? "))
    h = int(input("Cual es la Altura de tu triangulo? "))
    print(area_triangulo(b, h))




if __name__ == '__main__':
    run()