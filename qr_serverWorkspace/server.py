from io import BytesIO
import socket
from _http.HttpRequest import HttpRequest
from _http.HttpResponse import HttpResponse
from urls import url_mapping

class Server:
    
    def __init__(self, host, port, req_size):
        self.__host = host
        self.__port = port
        self.__req_size = req_size
    
    def start_server(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((socket.gethostname(), self.__port))
        serversocket.listen(5)
        
        while True:
            (clientsocket, address) = serversocket.accept()
            req_msg = clientsocket.recv(self.__req_size)
           
            request = HttpRequest(req_msg) 
            response = HttpResponse(clientsocket)
            target = url_mapping(request, response)
            
            body = target()
            
            response.add_body(body).send()
            
            
    def index(self):
        return 'Hi! Index Page!'
                    
    
