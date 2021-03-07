from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

PATH = "/home/chaitanya/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(7)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

for num_times in range(10):
    actions.perform()

#search = driver.find_element_by_name("s")
#print(search)
#search.send_keys('test')
#search.send_keys(Keys.RETURN)

#print(driver.page_source) 
#link = driver.find_element_by_link_text('Python Programming')
#link.click()