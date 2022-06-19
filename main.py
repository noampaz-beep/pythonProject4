# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import chromedriver_binary
from selenium import webdriver

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

def score_server():
    with open("Scores.txt") as myfile:
        for line in myfile.readlines():
            score = line
    myfile.close()


my_driver = webdriver.Chrome ()
my_driver.get("C:/Users/npaz163749/Downloads/tip_calc/index.html")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
