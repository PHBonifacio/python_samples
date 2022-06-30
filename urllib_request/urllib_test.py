from asyncore import read

from urllib import request, parse

header = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Cookie" : "cf_clearance=JyuWYu9gy6wQfRQwbGWIeIyYWwXy46y58_IcMQ13EPQ-1656627036-0-150; PHPSESSID=tfu8sirn6l1d27u8csneref9m4"
    }

login = {"user" : "admin", "password": "senhafoda"}
login = parse.urlencode(login).encode()

req = request.Request("http://www.bancocn.com/admin/index.php", headers=header, data=login)  

resp = request.urlopen(req)

resp_html = resp.read()

print(resp_html) 