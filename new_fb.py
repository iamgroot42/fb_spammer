import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


driver = None


def load_driver():
	global driver
	chromedriver = os.path.abspath("./chromedriver")
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)


def log_in(username, password):
	global driver
	driver.get("https://m.facebook.com")
	username_elem = driver.find_element_by_name("email")
	username_elem.clear()
	username_elem.send_keys(username)
	password_elem = driver.find_element_by_name("pass")
	password_elem.clear()
	password_elem.send_keys(password)
	password_elem.send_keys(Keys.RETURN)
	time.sleep(3) # Adjust according to your Internet speed


def post_to_this_page(target_id):
	global driver
	driver.get("https://m.facebook.com/" + target_id)
	for elem in soup(text="Write Post"):
	    	print elem.parent
	    	break
	like_stuff = driver.find_elements_by_xpath("//*[contains(text(), 'Like')]")
	comment_stuff = driver.find_elements_by_xpath("//*[contains(text(), 'Comment')]")
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	comment_stuff[i] = comment_stuff[i].get_attribute('href')


def comment_on_posts(posts, message = 'ohho'):
	for post in posts:
		comment(post, message)


if __name__ == "__main__":
	username = raw_input("Enter your Facebook username: ")
	password = getpass.getpass("Enter your Facebook password: ")
	load_driver()
	log_in(username, password)
	post_to_this_page("91springboard")

