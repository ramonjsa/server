#@SERVER
#@AUTHOR RAMON JOSE DE SOUSA ARAUJO
#@SERVIDOR MULTTHREAD 

import socket

from _thread import *
import threading

trabalhador_lock = threading.Lock()


def trabalho (c):
	while True:
		data =  c.recv(1024)
		if not data:
			trabalhador_lock.release()
			break
		#realiza o trabalho com os dados recebidos 
		resposta = "resposta"
		#
		c.send(resposta.encode())
	c.close()
	
	
	
def Main():
	thred_list = []
	
	host = ""
	port = 20000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	print ("socket binded to port ",port)
	
	s.listen(5)
	while True:
		c , addr  = s.accept()
		
		trabalhador_lock.acquire()
		print("Conectado a :",addr[0],':', addr[1])
		thred_id = start_new_thread(trabalho,(c,))
	s.close()
		
if __name__ == '__main__': 
    Main()
	
	