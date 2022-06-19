# API Testing
# 1. Testing Github API - Create a program in python that goes to the following API and
# checks that at least 5 git repositories exists - https://api.github.com/users/avielb/repos

# 3. Testing universities API - Go to http://universities.hipolabs.com/search?country=Israel
# and make sure that israel has at least 5 universities


import random
from selenium import webdriver
import string
import requests

response = requests.get("https://api.github.com/users/avielb/repos")

repos_list = response.json()

counter_git_repo = 0

for repo in repos_list:
    if repo["git_url"]:
        counter_git_repo = counter_git_repo + 1
        if counter_git_repo >= 5:
            print("more that 5 git repositories exists")
            break
    else:
        print("not git ")


# 2. Testing agify API - Create a program in python that generates 3 random names and
# checks that the age from the reply in this link: https://api.agify.io/?name=<name> is
# between 0 - 120

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random name is: ", result_str)
    return result_str


def check_age(age):
    if age is None:
        print("age is not int")
    elif age < 0 | age > 120:
        print(f"age is not between 0 -120: age= {age}")
    else:
        print(f"age between 0 -120: age= {age}")


for i in range(1, 4):
    name = get_random_string(8)
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url).json()["age"]
    check_age(response)

# 3. Testing universities API - Go to http://universities.hipolabs.com/search?country=Israel
# and make sure that israel has at least 5 universities

response = requests.get("http://universities.hipolabs.com/search?country=Israel").json()
university_list = []
for university in response:
    university_list.append(university["domains"])
    if len(university):
        print("Israel has at more than 5 universities")
        break

# UI Testing
# 4. Using Selenium go to https://www.ycombinator.com/ and test that the title is “Y Combinator”

my_driver = webdriver.Chrome()
my_driver.get("https://www.ycombinator.com/")
title = my_driver.title
assert title == "Y Combinator"

# 5. Using selenium go to https://hub.docker.com and test the the title is “Docker Hub
# Container Image Library | App Containerization”

my_driver = webdriver.Chrome()
my_driver.get("https://hub.docker.com")
title = my_driver.title
assert title == "Docker Hub Container Image Library | App Containerization"
