#!/usr/bin/env python3
import requests
import time

url = "http://web:8080/user-api/"

def registration(s, username, password):
    headers = {"Content-Type" : "application/json"}
    data = {"username": username, "password": password}
    r = s.post(url + "register", json=data, headers=headers)
    return r

if __name__ == "__main__":
    s = requests.Session()
    while 1:
        try:
            r = registration(s, "administrator", "sup3rs3cr3tp4ssw0rd")
            if "true" in r.text:
                break
        except:
            pass
        time.sleep(2)
