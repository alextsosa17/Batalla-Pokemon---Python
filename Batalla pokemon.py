# JUEGO POKEMON
import random


class Pokemon:
    def __init__(self, nombre, ataque, clase):
        self.nombre = nombre
        self.ataque = ataque
        self.clase = clase
        self.vida = 100


    def gano(self):
        print(f"{self.nombre} gano esta BATALLA y quedo con {self.vida}")




p1 = Pokemon("Pikachu", 30,"Electricidad")
p2 = Pokemon("Bulbasur", 30, "Tierra")
p3 = Pokemon("Charmander",30,"Fuego")
p4 = Pokemon("Scuartle", 30, "Agua")



def pelea_pokemon(usuario, rival):
    usuario.vida = 100
    rival.vida = 100
    turno = random.randint(1, 2)


    print(f"{usuario.nombre} se enfreneta a {rival.nombre}\n")
    vuelta = 1
    
    while usuario.vida > 0 and rival.vida > 0 :
        if turno == 1:
            while vuelta == 1:
                if (usuario.clase == "Electricidad" and rival.clase == "Agua") or (
                        usuario.clase == "Agua" and rival.clase == "Fuego") \
                        or (usuario.clase == "Tierra" and rival.clase == "Electricidad") or (
                        usuario.clase == "Fuego" and rival.clase == "Tierra"
                ):

                    usuario.ataque = usuario.ataque * 2
                    rival.ataque = rival.ataque // 2
                    vuelta = 2

                else:
                    if (usuario.clase == "Agua" and rival.clase == "Electricidad") or (
                            usuario.clase == "Fuego" and rival.clase == "Agua") \
                            or (usuario.clase == "Electricidad" and rival.clase == "Tierra") or (
                            usuario.clase == "Tierra" and rival.clase == "Fuego"
                    ):
                        usuario.ataque = usuario.ataque // 2
                        rival.ataque = rival.ataque * 2
                        vuelta = 2

                    else:
                        usuario.ataque = usuario.ataque
                        rival.ataque = rival.ataque
                        vuelta = 2




                print(f"el ataque de {usuario.nombre} es de {usuario.ataque}")
                print(f"el ataque de {rival.nombre} es de {rival.ataque}")

            usuario.vida = usuario.vida - rival.ataque
            turno = 2
            print(f"{rival.nombre} ataca, {usuario.nombre} ahora tiene {usuario.vida} de vida")
            print("======PROXIMA RONDA======")
        else:
            while vuelta == 1:
                if (usuario.clase == "Electricidad" and rival.clase == "Agua") or (
                        usuario.clase == "Agua" and rival.clase == "Fuego") \
                        or (usuario.clase == "Tierra" and rival.clase == "Electricidad") or (
                        usuario.clase == "Fuego" and rival.clase == "Tierra"
                ):

                    usuario.ataque = int(usuario.ataque * 2)
                    rival.ataque = int(rival.ataque // 2)
                    vuelta = 2

                else:
                    if (usuario.clase == "Agua" and rival.clase == "Electricidad") or (
                            usuario.clase == "Fuego" and rival.clase == "Agua") \
                            or (usuario.clase == "Electricidad" and rival.clase == "Tierra") or (
                            usuario.clase == "Tierra" and rival.clase == "Fuego"
                    ):
                        usuario.ataque = int(usuario.ataque // 2)
                        rival.ataque = int(rival.ataque * 2)
                        vuelta = 2

                    else:
                        usuario.ataque = usuario.ataque
                        rival.ataque = rival.ataque
                        vuelta = 2



                vuelta = 2


            rival.vida = rival.vida - usuario.ataque
            print(f"el ataque de {usuario.nombre} es de {usuario.ataque}")
            print(f"el ataque de {rival.nombre} es de {rival.ataque}")
            turno = 1
            vuelta = 2
            print(f"{usuario.nombre} ataca, {rival.nombre} ahora tiene {rival.vida} de vida")
            print("======PROXIMA RONDA======")

    if usuario.vida <= 0:
        rival.gano()
        print("MAS SUERTE LA PROXIMA")
    else:
        usuario.gano()
        print("HAS GANADO")



opcion = 1
continuar = True
while continuar:



    jugador1 = str(input("Con que pokemon Desea pelear?\n>").capitalize())
    jugador2= str(input('Contra que pokemon desea pelear?\n>').capitalize())

    while jugador1 == jugador2:
            print("no puedes pelear con el mismo pokemon de hambos bamdnos")
            jugador1 = input("Con que pokemon Desea pelear?").capitalize()
            jugador2 = input("Contra que pokemon desea pelear?").capitalize()



    if jugador1 == "Pikachu" and jugador2 == "Bulbasor":
        pelea_pokemon(p1, p2)
    else:
        if jugador1 == "Bulbasor" and jugador2 == "Pikachu":
            pelea_pokemon(p2, p1)
        else:
            if jugador1 == "Charmander" and jugador2 == "Pikachu":
                pelea_pokemon(p3, p1)
            else:
                if jugador1 == "Charmander" and jugador2 == "Bulbasor":
                    pelea_pokemon(p3, p2)
                else:
                    if jugador1 == "Bulbasor" and jugador2 == "Charmander":
                        pelea_pokemon(p2, p3)
                    else:
                        if jugador1 == "Pikachu" and jugador2 == "Charmander":
                            pelea_pokemon(p1, p3)
                        else:
                            if jugador1 == "Squartle" and jugador2 == "Pikachu":
                                pelea_pokemon(p4, p1)
                            else:
                                if jugador1 == "Squartle" and jugador2 == "Bulbasor":
                                    pelea_pokemon(p4, p2)
                                else:
                                    if jugador1 == "Squartle" and jugador2 == "Charmander":
                                        pelea_pokemon(p4,p3)
                                    else:
                                        if jugador1 == "Pikachu" and jugador2 == "Squartle":
                                            pelea_pokemon(p1, p4)
                                        else:
                                            if jugador1 == "Bulbasor" and jugador2 == "Squartle":
                                                pelea_pokemon(p2, p4)
                                            else:
                                                if jugador1 == "Charmander" and jugador2 == "Squartle":
                                                    pelea_pokemon(p3, p4)


    opcion = int(input("ingrese 1 si quiere volver a pelear 2 para terminar\n>"))
    if opcion == 2:
        print("Gracias por jugar Batallas Pokemon")
        continuar = False
    else:
        continuar = True