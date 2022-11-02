import socket
from time import sleep as wait
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def clientcode(ip, port):
    s.connect((ip, port))
    while True:
        print(s.recv(1024).decode('ascii'))
        wait(0.5)
        s.send(input('Enter reply: ').encode('ascii'))        
start = input('Start client? ')
if start == 'yes':
    clientcode(input('Enter ip address: '), int(input('Enter port number: ')))