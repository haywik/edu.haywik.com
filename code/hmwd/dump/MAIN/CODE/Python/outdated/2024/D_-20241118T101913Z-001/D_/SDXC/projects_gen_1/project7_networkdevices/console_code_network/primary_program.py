import subprocess, os, time, platform,threading,socket



RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def host_device(arg):
    hostname=socket.gethostname()

    return hostname


global hostname
hostname = host_device(1)
def hub_wifi(arg):

    hub_wifi_ip = "192.168.0.1"

    hub_wifi_name = "Sky Hub"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((hub_wifi_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()


    return system_status

def booster_hub(arg):

    booster_hub_ip = "192.168.0.26"

    booster_hub_name = "Hub Booster"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((booster_hub_ip,80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()



    return system_status

def blink_mod(arg):

    blink_mod_ip = "192.168.0.6"

    blink_mod_name = "Blink sync Module"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((blink_mod_ip, 443))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()


    return system_status


def silver_laptop(arg):
    silver_laptop_ip ="192.168.0.7"

    silver_laptop_name="Silver laptop"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((silver_laptop_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status

def blue_laptop(arg):
    blue_laptop_ip ="192.168.0.70"

    blue_laptop_name="Blue laptop"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((blue_laptop_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status

def haydens_iphone(arg):
    haydens_iphone_ip = "192.168.0.53"

    hayden_iphone_name="Haydens Iphone"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((haydens_iphone_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status

def megans_iphone(arg):
    megans_iphone_ip="192.168.0.50"
    means_iphone_name="Meagns Iphone"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((megans_iphone_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status


def ps5(arg):
    ps5_ip="192.168.0.43"
    ps5_name="Playsation 5"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ps5_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status

def ps4(arg):
    ps4_ip="192.168.0.51"
    ps4_name="Playsation 4"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ps4_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status


def printer(arg):
    printer_ip="192.168.0.16"
    printer_name="Printer"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((printer_ip, 8080))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status


def haydens_tv(arg):
    haydens_tv_ip="192.168.0.24"
    haydens_tv_name="Haydens TV"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((haydens_tv_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status

def tinas_iphone(arg):
    tinas_iphone_ip="192.168.0.52"
    tinas_iphone_name="Tinas Iphone"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((tinas_iphone_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status

def rosss_iphone(arg):
    rosss_iphone_name="Ross's Iphone"
    rosss_ip="192.168.0.55"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((rosss_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status

def front_room_tv(arg):
    front_room_tv_ip = "192.168.0.3"
    front_room_tv_name = "Front Room TV"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((front_room_tv_ip, 80))
    if result == 0:
        system_status = "Good"
    else:
        system_status = "Bad"
    sock.close()

    return system_status