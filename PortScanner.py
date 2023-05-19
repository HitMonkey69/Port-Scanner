# #Port Scanner by HitMonkey69


import socket
import pyfiglet

banner = pyfiglet.figlet_format('Port Scanner')
print(banner)
print('Enter 1 to use Port Scanner')
print('Enter 0 to Quit')

while(True):
    usr = int(input('Enter your Choice:'))

    if usr == 0:
        break

    else:
    

        host = input('Enter Host to Scan:')
        hostIP = socket.gethostbyname(host)

        print(hostIP)

