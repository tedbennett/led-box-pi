import time
import requests

while True:
    response = requests.get("https://led-box.herokuapp.com")
    print(response.text != None)
    time.sleep(50)
