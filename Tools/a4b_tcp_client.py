import socket

s = socket.socket()
s.connect(('localhost', 12345))
s.sendall(b'hello server\n')
s.close()
