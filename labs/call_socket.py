import socket

def resolve(host):
    return socket.gethostbyname(host)


print(resolve('sixty-north.com'))