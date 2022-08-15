
def cambio_Pesos_Dolares(pesos):
    return pesos/134.53
def cambio_Dolares_Pesos(dolares):
    return dolares*134.53

while True:
    print("""\t.:MENU:.
1.Convertir Pesos a Dolares
2.Convertir Dolares a Pesos
3. Salir""")
    opcion = int(input("Digite una opcion: "))
    print()
    
    if opcion == 1:
        pesos = float(input("Digite la candidad de pesos: "))
        print(f"Dolares -> UDS/{cambio_Pesos_Dolares(pesos):.2f}")
        
    elif opcion == 2:
        dolares = float(input("Digite la cantidad de dolares: "))
        print(f"Pesos -> ARS/{cambio_Dolares_Pesos(dolares):.2f}")
        
    elif opcion == 3:
        break
    else:
        print("Se equivoco de opcion")
    print()
    