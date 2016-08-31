#!/usr/bin/env python
import socket

s = socket.socket()
s.bind(("127.0.0.1",2015))
s.listen(5)
sc, addr = s.accept()

while True:
	recibido = sc.recv(1024)
	print recibido.find("quit")
	recibido = recibido [:-2]
	if (recibido == "quit"):
		print "salir por favor"
		break
	print "llego:[",recibido,"]"
	sc.send(recibido)

print "adios"
sc.close()
s.close()



