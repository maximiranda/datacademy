

def run():

    puntoj1 = 0
    puntoj2 = 0
    for i in range(3):
        eleccion_j1 = input("Jugador 1 : Elije 'Pieda-Papel-Tijer' ")
        eleccion_j2 = input("Jugador 2 : Elije 'Pieda-Papel-Tijer' ")
    
        if eleccion_j1 == "piedra":
            if eleccion_j2 == "tijera":
                print("punto jugador 1")
                puntoj1 += 1
                
            elif eleccion_j2 == "piedra":
                    print("empate")
                    
            elif eleccion_j2 == "papel":
                    print("punto para el jugador 2")
                    puntoj2 += 1
        elif eleccion_j1 == "papel":
            if eleccion_j2 == "tijera":
                print("punto jugador 2")
                puntoj2 += 1
            elif eleccion_j2 == "piedra":
                print("punto para jugador 1")
                puntoj1 += 1
            elif eleccion_j2 == "papel":
                print("empate")
        elif eleccion_j1 == "tijera":
            if eleccion_j2 == "tijera":
                print("empate")
                
            elif eleccion_j2 == "piedra":
                print("punto juador 2")   
                puntoj2 += 1
            elif eleccion_j2 == "papel":
                print("punto para el jugador 1")
                puntoj1 += 1
        else:
                print("porfavor elija 'piedra-papel-tijera'")
        if puntoj1 == 2:
            print("ganador jugador 1")
            break
        elif puntoj2 == 2:
            print("ganador jugador 2")
            break
        elif i == 2 and puntoj1 < 2 and puntoj2 < 2 :
            print("No hay ganadores")
            break
if __name__ == '__main__':
    run()