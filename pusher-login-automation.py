from selenium import webdriver

username = '<Your username>'
password = '<Your password>'

url = 'https://dashboard.pusher.com/accounts/sign_in'

driver = webdriver.Chrome("/Users/apple/Downloads/chromedriver")  #path to chrome driver

driver.get(url)

driver.find_element_by_id('signup-email').send_keys(username)
driver.find_element_by_id('signup-password').send_keys(password)
driver.find_element_by_class_name('active-b--dragonfruit-dark').click()
