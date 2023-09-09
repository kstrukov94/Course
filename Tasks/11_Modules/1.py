"""IPADDRESS"""
# Инструкция import помимо работы с собственными модулями,
# также открывает доступ ко встроенной библиотеке Python — набору модулей и пакетов для решения разнообразных прикладных задач.
#
# Один из таких встроенных пакетов — это ipaddress — он позволяет работать с IP-адресами (как конечных компьютеров, так и сетей).
# Официальная документация по этому пакету доступна на этой странице.
#
# Попробуйте, используя официальную документацию, написать функцию has_access для контроля доступа компьютера в сети.
# Функция должна принимать два аргумента: IP-адрес компьютера и IP-адрес сети, а затем возвращать True,
# если IP-адрес компьютера входит в число допустимых хостов для переданной сети и False в противном случае.
#
# Подсказка: используйте метод hosts, чтобы исключить сам сетевой адрес, а также широковещательный адрес.
#
# Пример использования функции:
# access = has_access("91.142.84.30", "91.142.84.0/27")
# print(access)
# True

import sys, ipaddress as ipa


def has_access(ip1, ip2):
    ip_comp = ipa.ip_address(ip1)
    ip_netw = ipa.ip_network(ip2)
    return True if ip_comp in list(ipa.ip_network(ip_netw).hosts()) else False



print(has_access("91.142.84.30", "91.142.84.0/27"))

# import ipaddress
# def has_access(ip1, ip2):
#     ip_computer = ipaddress.ip_address(ip1)
#     ip_network = ipaddress.ip_network(ip2)
#     return True if ip_computer in list(ip_network.hosts()) else False
# print(has_access("91.142.84.30", "91.142.84.0/27"))

# import ipaddress
# def has_access(ipa, network):
#     # Преобразовываем адреса.
#     ipa = ipaddress.ip_address(ipa)
#     network = ipaddress.ip_network(network)
#
#     # Выводим данные.
#     return True if ipa in network.hosts() else False
