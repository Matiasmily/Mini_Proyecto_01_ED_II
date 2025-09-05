from hash_table import HashTable
import os

hash_table = HashTable(5) 

def show_menu():
    while True:
        clear()
        print("SIMULACIÓN DE ROUTER\n")
        print("[1] Agregar IP")
        print("[2] Buscar IP")
        print("[3] Actualizar IP")
        print("[4] Eliminar IP")
        print("[5] Salir\n")

        option = input("Ingrese una opción (1-5): ")
        
        if option == "1":
            clear()
            print("Agregar IP\n")
            route = input("Ingresar IP: ")
            interface = input("Ingresar interfaz: ")
            hash_table.add_route(route,interface)
            print("\nTabla después de agregar IP: \n")
            hash_table.show_table()
            input("\nPresione Enter para continuar")

        elif option == "2":
             clear()
             print("Buscar IP\n")
             route = input("Ingresar IP: ")
             result = hash_table.search_route(route)
             if result:
                    print(f"\nLa IP {route} está en la interfaz {result}")
             else:
                    print(f"\nLa IP {route} no se encontró en la tabla")
             input("\nPresione Enter para continuar")

        elif option == "3":
             clear()
             print("Actualizar IP\n")
             route = input("Ingresar IP: ")
             interface = input("Ingresar interfaz: ")
             hash_table.add_route(route,interface)
             print("\nTabla después de actualizar IP: \n")
             hash_table.show_table()
             input("\nPresione Enter para continuar")

        elif option == "4": 
             clear()
             print("Eliminar IP\n")
             route = input("Ingresar IP: ")
             hash_table.delete_route(route)
             print("\nTabla después de eliminar IP: \n")
             hash_table.show_table()
             input("\nPresione Enter para continuar")
        
        elif option == "5":
             break
        
        else:
             print("\nIngrese una opción válida (1-5)")
             input("\nPresione Enter para continuar")

def clear():
        os.system("cls")

if __name__ == "__main__":
    show_menu()
    