import random

print("Piedra, Papel o tijera, v0.3")

print ("1 = piedra")
print ("1 = piedra")
print ("1 = piedra")
tirada = input("Escoge tu tirada: ")
tiradaordenador = random.randint(1,3)

if tiradaordenador == 1:
    print("el ordenador ha sacado piedra")
elif tiradaordenador == 2:
    print("el ordenador ha sacado papel")
elif tiradaordenador == 3:
    print("el ordenador ha sacado tijera")
