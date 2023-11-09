class HttpRequest:
    
    def __init__(self, req_msg):
        self.__method = None
        self.__params = None
        self.__url = None
        self.__header = None
        self.__parse_req_msg(req_msg)
    
    def get_method(self):
        return self.__method
    
    def get_param(self, name):
        return self.__params[name][0]
    
    def get_param_values(self, name):
        return self.__params[name]
    
    def get_url(self):
        return self.__url
     
    def __str__(self):
        return f'{self.__method},  {self.__url}, {self.__params}'
    
    def __parse_req_msg(self, req_msg):
        
        req_msg_lines = self.__generate_req_msg(req_msg)
        req_start_line = req_msg_lines[0].split(' ')
        
        self.__method = req_start_line[0]
        url_tmp = req_start_line[1]
        
        if '?' in url_tmp:
            self.__parse_parms(url_tmp)
            self.__url = url_tmp[0:url_tmp.index('?')]
        else:
            self.__url = url_tmp
        
        self.__generate_header(req_msg_lines)

    def __generate_header(self, req_msg_lines):
        req_header = req_msg_lines[1:req_msg_lines.index('')]
        self.__header = {}
        for e in req_header:
            tmp = e.split(':')
            self.__header[tmp[0]] = tmp[1]

    def __generate_req_msg(self, req_msg):
        req_msg = str(req_msg, encoding='utf-8')
        req_msg_lines = req_msg.splitlines()
        return req_msg_lines

    def __parse_parms(self, url_tmp):
        parm_str = url_tmp[url_tmp.index('?')+1:]
        parms_pairs = parm_str.split('&')
            
        params = {}
        for pair in parms_pairs:
            param_name = pair.split('=')[0]
            param_value = pair.split('=')[1]
                
            if param_name in params:
                params[param_name] = params[param_name].append(param_value)
            else:
                params[param_name] = [param_value]

        self.__params = params