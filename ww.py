import requests

try:
    with open("Scorhes.txt") as myfile:
        for line in myfile.readlines():
            score = line
    myfile.close()
except FileNotFoundError:
    print(err)
response = requests.post("http://10.201.191.30:5001/whatismyscore")
print(response)