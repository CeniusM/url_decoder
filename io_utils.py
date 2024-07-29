import sys

_HELP_ARGS = ["/?", "/h", "help"]

def fail(msg="invalid url"):
    print(msg)
    exit()

def arg_count():
    return len(sys.argv)

def get_url():
    return sys.argv[1]

def is_help():
    return arg_count() == 0 or sys.argv[1] in _HELP_ARGS

def print_help():
    print("url_decoder is a small script for decoding a url and see what it consists of")