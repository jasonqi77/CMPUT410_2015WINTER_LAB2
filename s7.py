import socket
import sys
try:
    import thread
except ImportError:
    import _thread as thread

def clientthread(conn):
    #code here ...
    #while
    while 1:
        data = conn.recv(1024)
        data2 = str(data)
        data2 = data2[0:len(data2)-2]
        reply = '<Hello ' + data2 + '>\n'
        conn.sendall(reply.encode("UTF-8"))
    
    conn.close()    
    
    

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket')
    print('Error code: ' + str(msg[0]) + ', Error message: ' + msg[1] )
    sys.exit()
print('Socket created')
host = ''
port = 8888
try:
    s.bind((host, port))
except socket.error as msg:
    print('Bind failed. Error code: ' + str(msg[0] + ', message: ' + msg[1]))
    sys.exit()
print('Socket bind is complete')
s.listen(2)
print('Socket now listening')

while 1:
    conn, addr = s.accept()
    thread.start_new_thread(clientthread, (conn,))
    
s.close()
