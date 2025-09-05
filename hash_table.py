class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__table = [None] * size

    def ip_to_int(self, ip):
        octets = list(map(int, ip.split(".")))
        return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]

    def hash(self, ip):
        key = self.ip_to_int(ip)
        return key % self.__size

    def add_route(self, ip, interface):
        index = self.hash(ip)
        start_index = index
        while self.__table[index] is not None:
            if self.__table[index][0] == ip:
                self.__table[index] = (ip, interface)
                return
            index = (index + 1) % self.__size
            if index == start_index:
                raise ValueError("Tabla Llena")
        self.__table[index] = (ip, interface)

    def search_route(self, ip):
        index = self.hash(ip)
        start_index = index
        while self.__table[index] is not None:
            if self.__table[index][0] == ip:
                return self.__table[index][1]
            index = (index + 1) % self.__size
            if index == start_index:
                break
        return None

    def delete_route(self, ip):
        index = self.hash(ip)
        start_index = index
        while self.__table[index] is not None:
            if self.__table[index][0] == ip:
                self.__table[index] = None
                return True
            index = (index + 1) % self.__size
            if index == start_index:
                break
        return False

    def show_table(self):
        for i, entry in enumerate(self.__table):
            print(f("Índice {i}: {entry}"))