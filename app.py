import random

# Prioridad posic pipeass
posiciones_prioridad = [
    "CF", "CM", "RW", "LW",
    "RCB", "LCB",
    "RB", "LB", "LF", "RF"
]

def asignar_posiciones(jugadores):
    random.shuffle(jugadores)
    equipo = {}
    
    for i, jugador in enumerate(jugadores):
        posicion = posiciones_prioridad[i % len(posiciones_prioridad)]
        equipo[jugador] = posicion
    
    return equipo

# datos pipasworld
nombres = []

cantidad = int(input("¿Cuántos jugadores hay? (min 6): "))

if cantidad < 6:
    print("6 jugadores min.")
else:
    for i in range(cantidad):
        nombre = input(f"Nombre {i+1}: ")
        nombres.append(nombre)

    random.shuffle(nombres)

    mitad = len(nombres) // 2
    equipo1 = nombres[:mitad]
    equipo2 = nombres[mitad:]

    equipo1_asignado = asignar_posiciones(equipo1)
    equipo2_asignado = asignar_posiciones(equipo2)

    print("\n equipo shadow detonando a pipa")
    for jugador, posicion in equipo1_asignado.items():
        print(f"{jugador} → {posicion}")

    print("\n equipo pipa tomandolo todo")
    for jugador, posicion in equipo2_asignado.items():
        print(f"{jugador} → {posicion}")
