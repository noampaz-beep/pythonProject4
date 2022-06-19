# enter name hello name
from datetime import datetime
import requests


def getName():
    current_name = input("enter your name: ")
    my_file = open("names.txt", "a")
    my_file.write(f"{current_name}\n")


def helloName():
    # my_file = open("names.txt", "r")
    # for line in my_file.readlines():
    #      print(f" hello {line.strip()}")
    # my_file.close()
    with open("names.txt") as my_file:
        for line in my_file.readlines():
            print(f"hello {line}", end='')


def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is ok")
    print(datetime.now())


def call_urls():
    with open("urlsnoam.txt") as urls:
        for line in urls.readlines():
            url_caller(line.strip())
    urls.close()



call_urls()
