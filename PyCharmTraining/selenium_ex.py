from selenium import webdriver
from selenium.webdriver.common.keys import Keys

wd = webdriver.Chrome()
wd.get('http://www.python.org')
assert 'Python' in wd.title
print(wd.title)

e=wd.find_element_by_name('q') #_id('id-search-field')
e.send_keys("shdjhsjdhj")
e.send_keys(Keys.RETURN)

    #.send_keys("pycharm")
#*[@id="id-search-field"]