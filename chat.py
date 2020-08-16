import sys
import socket
import getopt
import threading



def send(socket_obj,msg):
    socket_obj.send(msg.encode('utf-8'))

   
def receive(socket_obj):
    data = socket_obj.recv(1024).decode("utf-8")
    print(data)
    
    

def client_loop(target,port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(port)
    client.connect((target,port))
    while True:
        msg = input("send=> ")
        
        send(client, msg)
        receive(client)
            
def server_loop(target,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int((port))
    server.bind((target, port))
  
    server.listen(5)
    while True:
        c, addr = server.accept()
        print(f"{addr[0]} connected to the chat")
        thre = threading.Thread(target=server_handler, args=(c,addr))
        thre.start()

def server_handler(c,addr):
    while True:
        data = c.recv(1024)
        data = data.decode("utf-8")
        print(f"{addr[0]} : {data}")
      
        msg = input("send=> ")
        c.send(msg.encode("utf-8"))

global listen
global target
global port


listen      = False
target      = ""
port        = 4500 



opts,arg = getopt.getopt(sys.argv[1:],"lc:t:p:")
for o,a in opts:
    if o in ['-l']:
        listen = True
    elif o in ['-t']:
        target = a
    elif o in ['-p']:
        port = a    
print(target)    
print(port)

if not listen :
    
    client_loop(target,port)
    
if listen:
    server_loop(target, port)