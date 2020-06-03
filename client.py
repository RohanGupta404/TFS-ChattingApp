#!/usr/bin/env python3
import socket
import sys
import time
import concurrent.futures
from threading import Thread




def connect_socket():
   host = socket.gethostname()
   port = 12346

   s.connect((host, port))
   print("connected to chat server")


def send_message():
   global s
   sending_message = ""
   sending_message = input(str(">> "))
   sending_message = sending_message.encode("utf-8")
   s.send(sending_message)


def recive_message():
   global s
   recived_message = ""
   try:
      recived_message = s.recv(1024)
      if recive_message != "":
         recived_message = recived_message.decode("utf-8")
         print("\n ", recived_message, "\n")

   except:
      pass

def main():
   global s
   s = socket.socket()
   connect_socket()
   while True:
      send_message()
      receive_thread = Thread(target =recive_message())
      receive_thread.start()
main()
