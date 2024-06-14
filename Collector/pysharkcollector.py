import pyshark
import socket
from typing import List

class Collector:
    """
    Сборщик пакетов 
    """

    def __init__(self) -> None:
        self.iface = self.__define_iface() # Определить интерфейс
        
    def get_cur_iface(self) -> str:
        print(f"Ваш текущий интерфейс: {self.iface}")
        return self.iface

    # Выбор интерфейса
    def __define_iface(self) -> List[str]:
        valid_flag = False
        ifaces_list = [iface[1] for iface in socket.if_nameindex()]
        print('Выберите интерфейс (введите номер интерфейса):')
        ifaces_list_size = len(ifaces_list)        
        for i in range(ifaces_list_size):
            print(f"{i}:{ifaces_list[i]}")
        while valid_flag == False:                   
            iface_id = input()
            valid_flag, iface_id = self.__validate_id(iface_id, ifaces_list_size, valid_flag)
        return ifaces_list[iface_id]
    
    # Валидация введённого идентификатора интерфейса
    def __validate_id(self, id:str, size:int, valid_flag:bool):
        is_adv_digit = lambda x: x.isdigit() if x[:1]!='-' else x[1:].isdigit()
        if is_adv_digit(id):
            id = int(id)
            if id < 0:
                print("Введённое число должно быть неотрицательным! Пожалуйста, повторите попытку.")
                return False, id
            elif id >= size:
                print("Введенное число не должно превышать максимальный номер интерфейса. Пожалуйста, повторите попытку.")
                return False, id
            else:
                return True, id
        else:
            print("Введённое значение не является числом! Пожалуйста, повторите попытку.")
            return False, id

