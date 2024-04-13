import random

print("Piedra, Papel o tijera, v0.3")

print ("1 = piedra")
print ("1 = piedra")
print ("1 = piedra")
tirada = int (input("Escoge tu tirada: "))
tiradaordenador = random.randint(1,3)

if tiradaordenador == 1:
    print("el ordenador ha sacado piedra")
elif tiradaordenador == 2:
    print("el ordenador ha sacado papel")
elif tiradaordenador == 3:
    print("el ordenador ha sacado tijera")
if tirada == 1 and tiradaordenador == 1:
    print ("empate")
elif tirada == 1 and tiradaordenador == 2:
    print ("maquina gana")
elif tirada == 1 and tiradaordenador == 3:
    print ("jugador gana")
elif tirada == 2 and tiradaordenador == 1:
    print ("jugador gana")
elif tirada == 2 and tiradaordenador == 2:
    print ("empate")
elif tirada == 2 and tiradaordenador == 3:
    print ("tijeras")
elif tirada == 3 and tiradaordenador == 1:
    print ("maquina gana")
elif tirada == 1 and tiradaordenador == 2:
    print ("jugador gana")
elif tirada == 1 and tiradaordenador == 3:
    print ("empate")