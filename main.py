from objeto import Objeto
from mochila import Mochila
from fcn_frac import knapsack_fraccional
from fcn_dp import knapsack_01
from clima import obtener_clima

def main():
    print("Bienvenido al optimizador de mochila para acampadas.")
    
    # Solicitar la ciudad para el clima
    ciudad = input("Ingrese la ciudad de destino para consultar el clima: ")
    try:
        clima, temp = obtener_clima(ciudad)
        print(f"El clima en {ciudad} es {clima} con {temp}°C.")
    except Exception as e:
        print(f"No se pudo obtener el clima: {e}")
        return

    # Crear lista de objetos proporcionados por el usuario
    print("\nIngrese los objetos que quiere llevar en su mochila:")
    objetos = []
    while True:
        nombre = input("Nombre del objeto (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break
        try:
            peso = float(input("Peso del objeto (kg): "))
            valor = float(input("Valor o importancia del objeto (1 mín. - 10 máx.): "))
            divisible = input("¿El objeto es divisible? (s/n): ").lower() == 's'
            objetos.append(Objeto(nombre, peso, valor, divisible))
        except ValueError:
            print("Entrada inválida. Por favor, introduzca valores numéricos para peso y valor.")

    # Definir la capacidad de la mochila
    try:
        capacidad = float(input("\nIngrese la capacidad de la mochila (kg): "))
    except ValueError:
        print("Capacidad inválida. El valor debe ser numérico.")
        return

    mochila = Mochila(capacidad)
    for obj in objetos:
        mochila.agregar_objeto(obj)

    # Selección del algoritmo
    print("\nSeleccione el algoritmo a usar:")
    print("1. Mochila 0/1 (Programación Dinámica)")
    print("2. Mochila Fraccional (Greedy)")
    opcion = int(input("Opción: "))

    if opcion == 1:
        beneficio, seleccion = knapsack_01(mochila)
    elif opcion == 2:
        beneficio, seleccion = knapsack_fraccional(mochila)
    else:
        print("Opción no válida.")
        return

    # Mostrar resultados
    print(f"\nBeneficio total: {beneficio}")
    print("Objetos seleccionados:")
    for obj in seleccion:
        print(obj)

if __name__ == "__main__":
    main()
