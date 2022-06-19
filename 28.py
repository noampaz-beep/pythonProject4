import requests

response = requests.post("http://127.0.0.1:5001/whatismyname")
expected = "saved new car"
assert expected == response.text
