from logging import exception
import requests 
import sys

def bruteforce(domain, lines):
    for line in lines:
        try:
            url = "{}/{}".format(domain, line.replace("\n", ""))
            response = requests.get(url, timeout=1)
            code = response.status_code
            if 404 != code:
                print(">> {} - {}".format(code, url))
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as error:
            print(error)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        domain = sys.argv[1]
        file = open(sys.argv[2], 'r')
        print("Starting brute force on " + domain)
        bruteforce(domain, file.readlines())

    else:
        print("missing parameter.")
        print("usage: pybruteforce.py <host> <wordlist>")