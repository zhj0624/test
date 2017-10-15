#coding:utf-8
__author__ = 'ferraborghini'

from socket import *
import struct

#将16进制数据当做字节流传递

def dataSwitch(data):
    str1 = ''
    str2 = ''
    while data:
        str1 = data[0:2]
        s = int(str1,16)
        str2 += struct.pack('B',s)
        data = data[2:]
    return str2

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 502
    BUFSIZE = 1024
    ADDR = (HOST,PORT)
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    while True:
        data = raw_input('>')
        if not data:
            break
        tcpCliSock.send(dataSwitch(data))
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print data
    tcpCliSock.close()







#----------------------
#s = socket.socket()
#s.connect(('127.0.0.1',502))

#data = s.recv(1024)
#print data

#while True:  
    #data = s.recv(1024)  
    #if  data.strip():  
        #print 'Replay is ',data  
        #flag = True  
        #while flag:  
            #kel = raw_input('Question :>>')  
            #print 'raw_input values : %r' % kel  
            #if kel.strip():  
                #flag=False  
        #s.sendall(kel)  
        #if kel == 'exit':  
            #break  
#s.close()

