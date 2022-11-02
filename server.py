import socket
from time import sleep as wait
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def server():
    s.listen()
    while True:
        client, address = s.accept()
        print(address)
        while True:
            msg = input('Enter message to send: ')
            client.send(msg.encode('ascii'))
            print(client.recv(1024).decode('ascii'))
    client.close()
start = input('Start server? ')
if start == 'yes':
    s.bind(('127.0.0.1', int(input('Enter port number: '))))
    server()