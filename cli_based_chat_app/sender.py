import socket 

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # for connection between two systems , dgram is to convert the data into packets
    ip_address="192.168.70.126"
    ## sender ke andar humesha reciever ka ip adress ayega 
    port_number=1946
    target_add=(ip_address,port_number)
    message=input("Enter message here --->")
    encripted_message =message.encode("ascii")
    s.sendto(encripted_message,target_add)

except Exception as e:
    print("message not sent")
    