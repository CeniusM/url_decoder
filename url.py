#!/usr/bin/env python3

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
    
    authority, domain_leftover = domain_leftover.split("/", 1)

path = domain_leftover

authority, userinfo, host, port = parse_authority(authority)

# --Printing the url info
print(f"Schema: {schema}")

if userinfo is not None:
    print(f"Authority: {authority}")
    print(f"Userinfo: {userinfo}")
    print(f"Host: {host}")
    if port is not None:
        print(f"Port: {port}")
else:
    sub_domain, top_domain = authority.rsplit(".", 1)
    hostname, sub_domain = sub_domain.split(".", 1)
    print(f"Top level domain (TLD): {top_domain}")
    print(f"Sub domain(s): {sub_domain}")
    print(f"Hostname: {hostname}")

print(f"Path: /{path}")

# Todo- implement the queries and fragments info