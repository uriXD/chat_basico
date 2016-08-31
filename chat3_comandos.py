#!/usr/bin/env python
import socket

s = socket.socket()
s.bind(("127.0.0.1",2016))
s.listen(5)
sc, addr = s.accept()

while True:
	recibido = sc.recv(1024)
	print recibido.find("quit")
	recibido = recibido [:-2]
	if (recibido == "quit"):
		print "salir por favor"
		break

	elif (recibido == "ayuda"):
		sc.send("comando ayuda, \n 1) quit: ayuda a salir del chat \n 2) uri: especial \n 3) ayuda: te da ayuda de los comandos \n ")

	elif (recibido == "uri"):
		sc.send("\n Bienvenido al chat de prueba :3 disfruta tu visita \(n,n)/ \n")

	elif (recibido == "tipo"):
		sc.send("\n chat version3 \n")

	elif (recibido == "konami"):
		sc.send("\n arriba arriba abajo abajo < > < > B A start \n")

	elif (recibido == "comoEstas"):
		sc.send("muy bien y tu? \n")

	elif (recibido == "lenguaje"):
		sc.send("python2.7\n")

   

	elif (recibido == "youtube"):
		sc.send("\n https://www.youtube.com/watch?v=YUjM2V6x7aM \n")

	elif (recibido == "info_chat"):
		sc.send("\n ip 127.0.0.1 2015\n")	

	elif (recibido == "sonic1"):
		sc.send("\n Level Select At the title screen, \n press Up, Down, Left, Right. You should hear a noise like a ring being collected. \n Then, hold A and press Start for a level select!\n")

	print "llego:[",recibido,"]"
	sc.send(recibido)

print "adios"
sc.close()
s.close()

#try redis
#redis