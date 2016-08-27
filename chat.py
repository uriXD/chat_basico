#!/usr/bin/env python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost",9994))
s.listen(1)
sc, addr = s.accept()

while True:
	recibido = sc.reciv(1024)
	if recibido == "quit":
		break

	print "recibido:", recibido
	sc.send(recibido)
print "adios"
sc.close()
s.close()


#aun se realizan pruebas debido aun error presentado
#1) error a resolver 
#Traceback (most recent call last):
#  File "chat.py", line 6, in <module>
#    s.listen(1)
#  File "/home/xxxx/Escritorio/python/socket.py", line 228, in meth
#    return getattr(self._sock,name)(*args)
#socket.error: [Errno 95] Operation not supported
