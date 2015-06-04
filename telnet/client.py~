import socket,sys

host = "localhost"
port = 1155

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

usname = raw_input("IPaddress: ")
passwd = raw_input("Password : ")

s.send(usname)
s.send(passwd)

msg = s.recv(20)

if msg=='Login failed':
	s.close()

print msg
	
while True:

	cmd = raw_input("CMD : ")

	s.send(cmd)

	data = s.recv(1024)

	print data

s.close()
