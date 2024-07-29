from str_utils import *

def parse_authority(auth: str):
    if auth.count("@") == 0:
        return (auth, None, None, None)
    
    userinfo, host = auth.split("@", 1)
    
    if auth.count(":") == 0:
        return (auth, userinfo, host, None)
    
    host, port = host.split(":", 1)
    
    return (auth, userinfo, host, port)

def decode_str_hex_symbols(s: str):
    new_str = ""
    while len(s) != 0:
        if s[0] == "%":
            new_str += decode_hex_symbole(s[1:3])
            s = s[3:]
            continue

        next_index = s.find("%")
        if next_index == -1:
            next_index = len(s)
        
        new_str += take(s, next_index)
        s = skip(s, next_index)
    return new_str