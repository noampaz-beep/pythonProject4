from selenium import webdriver


my_driver = webdriver.Chrome ()
my_driver.get("C:/Users/npaz163749/Downloads/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[3]").click()
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_id("musicamt").send_keys("2")
my_driver.find_element_by_id("calculate").click()
expected = "6.00"
actual = my_driver.find_element_by_xpath("//*[@id=\"tip\"]").text

assert  expected == actual

if expected == actual:
    print("all good")
else:
    print("you broke the test")