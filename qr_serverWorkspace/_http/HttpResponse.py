from _http.HttpStatus import HttpStatus

class HttpResponse:
    def __init__(self, clientsocket):
         self.__status = HttpStatus.OK
         self.__header = {}
         self.__body = None
         self.__clientsocket = clientsocket
         
    def __str__(self):
        return f'{self.__header} {self.__body} {self.__status}'
    
    def set_status(self, httpStatus):
        self.__status = httpStatus
        return self
    
    def get_status(self):
        return self.__status
    
    def add_header(self, name, val):
        self.__header[name] = val
        return self
    
    def add_body(self, data):
        self.__body = data
        return self
        
    def send(self):
        if isinstance(self.__body, str) or self.__body is None:
            self.__send_text_data()
        else:
            self.__send_bytes()
        
        return self

    def __send_bytes(self):
        response_msg = self.__prepare_response()
        self.__clientsocket.send(response_msg.encode('utf-8'))
        self.__clientsocket.send(self.__body)
        self.__clientsocket.close()
    
    def __send_text_data(self):
        response_msg = self.__prepare_response()
        response_msg += self.__body
        self.__clientsocket.send(response_msg.encode('utf-8'))
        self.__clientsocket.close()

    def __prepare_response(self):
        response_msg = self.__status.startline + '\n'
        
        for name, val in self.__header:
            response_msg += name + ':' + val + '\n'
        
        response_msg += '\n'
        return response_msg
        

