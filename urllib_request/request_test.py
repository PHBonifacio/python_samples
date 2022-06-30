import requests 

header = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Cookie" : "cf_clearance=JyuWYu9gy6wQfRQwbGWIeIyYWwXy46y58_IcMQ13EPQ-1656627036-0-150; PHPSESSID=tfu8sirn6l1d27u8csneref9m4"
    }

login = {"user" : "admin", "password": "senhafoda"}

#answer = requests.get("http://www.bancocn.com" , headers=header)

answer = requests.post("http://www.bancocn.com/admin/index.php" , headers=header, data = login)
print(answer.text)
