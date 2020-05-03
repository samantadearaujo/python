#coding: utf-8
import socket, threading, select

def conecta(cliente, endereco):
    print('Cliente {} Recebido!' .format(endereco))
    servidor = socket.socket()
    servidor.connect(('n1.serverip.co',8080))

cliente.recv(8192)
servidor.send('CONNECT n1.serverip.co:443 HTTP/1.0\r\n\r\n')
servidor.recv(8192)
cliente.send('HTTP/1.1 200 Connection established\r\n\r\n')

try:
    while True:
        leitura, escrita, erro = select.select([servidor,cliente],[],[servidor,cliente],3)
        if erro: break
        for i in leitura:
            dados = i.recv(8192)
            if not dados: raise
            print(dados)
            if i is servidor:
                cliente.send(dados)#Donwload
            else:
                servidor.send(dados)#Upload
   
except:
    print('Cliente Desconectado')


#Listen.
listen = socket.socket()
listen.bind( ('127.0.0.1', 8088) )
listen.listen(0)
print('Esperando o cliente no IP e porta: 127.0.0.1:8088')
while True:
    cliente, endereco = listen.accept()
    threading.Thread(target = conecta, args=(cliente,endereco)).start() 

   






