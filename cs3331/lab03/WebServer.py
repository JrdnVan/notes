"""
(i) create a connection socket when contacted by a client (browser). x

(ii) receive HTTP request from this connection. Your server should only process GET request. You may assume that only GET requests will be received. x

(iii) parse the request to determine the specific file being requested. x

(iv) get the requested file from the server's file system. x

(v) create an HTTP response message consisting of the requested file preceded by header lines. x

(vi) send the response over the TCP connection to the requesting browser. x

(vii) If the requested file is not present on the server, the server should send an HTTP ?404 Not Found? message back to the client. x

(viii) the server should listen in a loop, waiting for next request from the browser. x
"""

import sys
from socket import *

# create a connection socket when contacted by a client (browser).
s = socket()
s.bind(('127.0.0.1', int(sys.argv[1])))
s.listen(1)

# the server should listen in a loop, waiting for next request from the browser.
while 1:

    # receive HTTP request from this connection. Your server should only process GET request. You may assume that only GET requests will be received.
    c = s.accept()[0]
    
    # parse the request to determine the specific file being requested.
    fn = c.recv(1024).split()[1][1:]
    
    try:
        #get the requested file from the server's file system.
        f = open(fn, "rb")
        response = f.read()
        f.close
        c.send("HTTP/1.1 200 OK\r\n".encode())
        
        # create an HTTP response message consisting of the requested file preceded by header lines.
        if "html".encode() in fn:
            c.send("Content-Type: text/html\r\n\r\n".encode())
        elif "png".encode() in fn:
            c.send("Content-Type: image/png\r\n\r\n".encode())  
    
        # send the response over the TCP connection to the requesting browser.
        c.send(response)
        
    except FileNotFoundError:
        # If the requested file is not present on the server, the server should send an HTTP ?404 Not Found? message back to the client.
        c.send("HTTP/1.1 404 File Not Found\r\n".encode())
        
    c.close()