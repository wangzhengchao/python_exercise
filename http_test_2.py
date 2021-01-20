from socket import *

sock = socket()
sock.bind(("0.0.0.0", 8004))

sock.listen(5)
connfd, addr = sock.accept()
print("connect from ", connfd)

request = connfd.recv(1024)

print(request.decode())
response = """HTTP/1.1 200 OK
Content-Type:text/html

"""
file = open("my.html", "rb")
data = file.read()

connfd.send(response.encode() + data)

connfd.close()
sock.close()
