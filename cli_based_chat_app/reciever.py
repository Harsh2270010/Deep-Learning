import socket 


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address="192.168.70.148"    # Bind to all available network interfaces
port_number=1355
complete_add = (ip_address , port_number)
s.bind(complete_add)
while True:
    message = s.recv(1024)
    print(message)
    data = message[0]
    data ="\n"
    print(data.encode("ascii"))







