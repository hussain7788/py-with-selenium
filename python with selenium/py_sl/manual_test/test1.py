from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="E:\chrome driver\chromedriver.exe")
driver.get("https://www.cpasage.com/signin/")
print(driver.title)
driver.find_element_by_id("user").send_keys("sarah.walker@cpa.com")
driver.find_element_by_id("password").send_keys("Cpasage@123")
driver.find_element_by_id("submit").click()
sleep(1)
driver.maximize_window()
driver.find_element_by_id("clientActions").click()
links = driver.find_elements_by_tag_name("a")
count = 0
for link in links:
    count += 1
    print(link.text)
print(count)
    # if link == '<selenium.webdriver.remote.webelement.WebElement (session="aed82f4d192036b7042fe7fc6e1b23dc", element="b88cde69-b59a-44d1-9a2c-6179e2b450bc")>':
    #     print("ok")
    # else:
    #     print("not")
    # if link.text == "Frank":
    #     driver.find_elements_by_link_text("Frank").click()
    # else:
    #     print("not")

# driver.find_elements(By.TAG_NAME, "a")
# driver.find_element_by_id("frank.zhang@client.com-dashboard").click()
# driver.find_element_by_id("viewClientMessages").click()
# l_msgs = ['this is test1', 'this is test 2']
# for msg in l_msgs:
#     sleep(1)
#     driver.find_element_by_id("clientMessageText").send_keys(msg)
#     sleep(1)
#     driver.find_element_by_id("sendClientMessage").click()
# driver.find_element_by_id("hideClientMessages").click()

sleep(3)
driver.close()