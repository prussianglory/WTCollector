import pyshark
import socket

class Collector:
    """
    Сборщик пакетов 
    """

    def __init__(self) -> None:
        self.iface = self.define_iface() # Определить интерфейс
        
    def get_cur_iface(self):
        print(f"Ваш текущий интерфейс: {self.iface[1]}")
        return self.iface

    def define_iface(self):
        ifaces_list = socket.if_nameindex()
        print('Выберите интерфейс:')
        print(ifaces_list)
        iface_id = int(input())
        return ifaces_list[iface_id]
    

