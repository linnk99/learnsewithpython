from selenium import webdriver

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get('http://demo-store.seleniumacademy.com/')

# get the search textbox
search_field = driver.find_element_by_name('q')
search_field.clear()

# enter search keyword and submit
search_field.send_keys('tee')
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//*[@id='top']/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/p/strong")
products_amount = products.text

# get the number of items found matching the search term
print 'Found ' + products_amount

# close the browser window
driver.quit()
