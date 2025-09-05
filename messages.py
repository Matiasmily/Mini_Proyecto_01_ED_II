RESET   = "\033[0m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

class Mensajes:
    @staticmethod
    def titulo_principal():
        print("\n ")
        print(GREEN + "╔════════════════════════════════════════╗" + RESET)
        print(GREEN + "║ " + WHITE + "         SIMULACIÓN DE ROUTER          " + GREEN + " ║" + RESET)
        print(GREEN + "╚════════════════════════════════════════╝" + RESET)

    @staticmethod
    def agregar_ip():
        print("\n ")
        print(YELLOW + "╔════════════════════════════════════════╗" + RESET)
        print(YELLOW + "║ " + WHITE + "             AGREGAR IP               " + YELLOW + " ║" + RESET)
        print(YELLOW + "╚════════════════════════════════════════╝" + RESET)

    @staticmethod
    def buscar_ip():
        print("\n ")
        print(BLUE + "╔════════════════════════════════════════╗" + RESET)
        print(BLUE + "║ " + WHITE + "             BUSCAR IP                " + BLUE + " ║" + RESET)
        print(BLUE + "╚════════════════════════════════════════╝" + RESET)

    @staticmethod
    def actualizar_ip():
        print("\n ")
        print(MAGENTA + "╔════════════════════════════════════════╗" + RESET)
        print(MAGENTA + "║ " + WHITE + "           ACTUALIZAR IP              " + MAGENTA + " ║" + RESET)
        print(MAGENTA + "╚════════════════════════════════════════╝" + RESET)

    @staticmethod
    def eliminar_ip():
        print("\n ")
        print(CYAN + "╔════════════════════════════════════════╗" + RESET)
        print(CYAN + "║ " + WHITE + "             ELIMINAR IP              " + CYAN + " ║" + RESET)
        print(CYAN + "╚════════════════════════════════════════╝" + RESET)

    @staticmethod
    def error_opcion():
        print(RED + "\nERROR!, Ingrese una opción válida (1 - 5)" + RESET)
