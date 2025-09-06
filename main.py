from hash_table import HashTable
from messages import Mensajes
import os

RESET   = "\033[0m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

hash_table = HashTable(5)

def solicitar_dato(campo):
    while True:
        valor = input(f"Ingresar {campo}: ").strip()
        if valor:
            return valor
        else:
            print(RED + f"\nERROR: Debe ingresar un valor para {campo}" + RESET)

def show_menu():
    while True:
        clear()
        Mensajes.titulo_principal()
        print("\n[1] Agregar IP")
        print("[2] Buscar IP")
        print("[3] Actualizar IP")
        print("[4] Eliminar IP")
        print("[5] Salir\n")

        option = input(YELLOW + "Ingrese una opción (1-5): " + RESET)

        match option:
            case "1":
                clear()
                Mensajes.agregar_ip()
                route = solicitar_dato("IP")
                interface = solicitar_dato("interfaz")
                hash_table.add_route(route, interface)
                print(YELLOW + "\nTabla después de agregar IP: \n" + RESET)
                hash_table.show_table()
                input(CYAN + "\nPresione Enter para continuar" + RESET)

            case "2":
                clear()
                Mensajes.buscar_ip()
                route = solicitar_dato("IP")
                result = hash_table.search_route(route)
                if result:
                    print(GREEN + f"\n✔ La IP {route} está en la interfaz {result}" + RESET)
                else:
                    print(RED + f"\n✖ La IP {route} no se encontró en la tabla" + RESET)
                input(CYAN + "\nPresione Enter para continuar" + RESET)

            case "3":
                clear()
                Mensajes.actualizar_ip()
                route = solicitar_dato("IP")
                interface = solicitar_dato("interfaz")
                hash_table.add_route(route, interface)
                print(YELLOW + "\nTabla después de actualizar IP: \n" + RESET)
                hash_table.show_table()
                input(CYAN + "\nPresione Enter para continuar" + RESET)

            case "4":
                clear()
                Mensajes.eliminar_ip()
                route = solicitar_dato("IP")
                hash_table.delete_route(route)
                print(YELLOW + "\nTabla después de eliminar IP: \n" + RESET)
                hash_table.show_table()
                input(CYAN + "\nPresione Enter para continuar" + RESET)

            case "5":
                print(RED + "\nSaliendo del programa..." + RESET)
                break

            case _:
                Mensajes.error_opcion()
                input(CYAN + "\nPresione Enter para continuar" + RESET)

def clear():
    os.system("cls")

if __name__ == "__main__":
    show_menu()
