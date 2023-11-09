from enum import Enum

class HttpStatus(Enum):
    OK = (200,"ok", "HTTP/1.1 200 ok")
    NOT_FOUND = (404,"Not Found", "HTTP/1.1 404 Not Found")
    INTERNAL_SERVER_ERROR = (500, 'Internal Server Error', "HTTP/1.1 500 Internal Server Error")
    
    def __init__(self, code, msg, startline):
        self.code = code
        self.msg = msg
        self.startline = startline