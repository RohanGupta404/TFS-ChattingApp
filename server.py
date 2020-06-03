#!/usr/bin/env python3
import socket
import sys
from threading import Thread

s = socket.socket()

def defining_socket():
   global conn_list
   global addr_list

   host = socket.gethostname()
   port = 12346
   s.bind((host, port))

   s.listen(5)

   conn_list = []
   addr_list = []

def list_for_connection(number_client):
   for i in range(number_client):
       conn, address = s.accept()
       conn_list.append(conn)
       addr_list.append(address)
       print("connection established with: " + address[0])

def recieve_and_send_message(client_no):
    sending_message = ""
    recived_message = ""
    recived_message = conn_list[client_no].recv(1024)
    recived_message = recived_message.decode("utf-8")
    print(recived_message)

    sending_message = recived_message.encode("utf-8")
    for k in range(0,number_clients):
        conn_list[k].send(sending_message)

number_clients = int(input("Enter number of clients: "))
defining_socket()
list_for_connection(number_clients)

allclient = {}
for k in range(number_clients):
    allclient[k] = k
for i in range(len(allclient)):
    allclient[i] = recieve_and_send_message

def thread_for_conections():
    for i in range(number_clients):
        Thread(target=allclient[i], args=(i,)).start()


while True:
    try:
        thread_for_conections()
    except:
        pass
