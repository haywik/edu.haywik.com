import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
result = sock.connect_ex((host, port))
if result == 0:
    system_satus = "Good"
else:
    sustem_satus="Bad"
sock.close()