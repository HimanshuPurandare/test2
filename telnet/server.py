import socket,sys,os
from platform import system

host = "localhost"
port = 1155

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#ch = 'a'
try:
    s.bind((host,port))
except:
    print "Bind failed!"
    sys.exit()
    
print "Socket bind complete."
s.listen(5)
while 1:
    conn,addr = s.accept()
    print "Connected to "+addr[0]+":"+str(addr[1])
    
    #time.sleep(25)
    
    user = conn.recv(9)
    pswd = conn.recv(5)
    
    if user!='127.0.0.1' or pswd!='paddy':
        conn.send("Login failed")
        
    conn.send("Login successful")
    
    while True:
    
		stn = conn.recv(20)
		
		cmd = stn + " >> a.txt"
		
		os.system(cmd)
		
	   # file = str(ch)+".txt"
		
		f = open("a.txt","r")
		
		data = f.read(1024)
		
	   # while (data):    	
		conn.send(data)
		
		os.system('rm -r a.txt')
    
conn.close()
