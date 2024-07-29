def take_until(s: str, end: str):
    return s.split(end, 1)[0]

def skip(s: str, dist: int):
    return s[dist:]

def take(s: str, dist: int):
    return s[:dist]

def decode_hex_symbole(s: str):
    return chr(int(s, 16))