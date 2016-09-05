import socket

s = socket.socket()
s.connect(("127.0.0.1",2015))


while True:

	mensaje = raw_input("> ")
	s.send(mensaje)
	if mensaje == "quit":
		break

print "adios"

s.close()
