from io_utils import *
from str_utils import *
from url_utils import *

# --Checking arguments--
if is_help():
    print_help()
    exit()

if arg_count() != 2:
    fail("Need one argument for the url")

# --Parsing the url--
url = get_url()

domain = url.split("?")[0]
domain = url.split("#")[0]

schema, domain_leftover = domain.split(":", 1)

if schema != "http" and schema != "https":
    fail("Unsupported schema")

authority = None

if domain_leftover.find("//") == 0:
    domain_leftover = skip(domain_leftover, 2)

    if domain_leftover[0] == "/":
        fail()
    
    if domain_leftover.count("/") == 0:
        domain_leftover += "/"
    
    authority, domain_leftover = domain_leftover.split("/", 1)

path = domain_leftover

authority, userinfo, host, port = parse_authority(authority)

# --Printing the url info--
print(f"Schema: {schema}")

if userinfo is not None:
    print(f"Authority: {authority}")
    print(f"Userinfo: {userinfo}")
    print(f"Host: {host}")
    if port is not None:
        print(f"Port: {port}")
else:
    hostname, top_domain = authority.rsplit(".", 1)
    sub_domain = None
    if hostname.count(".") != 0:
        hostname, sub_domain = hostname.split(".", 1)

    print(f"Top level domain (TLD): {top_domain}")
    if sub_domain is not None:
        print(f"Sub domain(s): {sub_domain}")
    print(f"Hostname: {hostname}")

print(f"Path: /{path}")

# Todo- implement the parameters and anchor info
# Fix the parse_authority, we can have a port without a username 