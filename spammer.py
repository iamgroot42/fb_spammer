import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


driver = None


def get_specific_element(xpath, button_text):
	global driver
	submit_buttons = driver.find_elements(By.XPATH, xpath)
	for button in submit_buttons:
		if button.is_displayed():
			if button.text == button_text:
				return button
	return None


def read_post_text(file_path = './post_text'):
	f = open(file_path,'r')
	post_message = []
	for line in f:
		post_message.append(line.rstrip())
	return post_message


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


def post_to_this_page(target_id, link, text):
	global driver
	try:
		driver.get("https://m.facebook.com/" + target_id)
		actions = webdriver.ActionChains(driver)
		post_button = get_specific_element("//*[@class='_56bz _54k8 _5c9u _5caa']", "Write Post")
		post_button.click()
		driver.find_element_by_id("uniqid_1").clear()
		driver.find_element_by_id('uniqid_1').send_keys(link)
		time.sleep(1)
		driver.find_element_by_id("uniqid_1").clear()
		for sentence in text:
			driver.find_element_by_id('uniqid_1').send_keys(sentence)
			driver.find_element_by_id('uniqid_1').send_keys(Keys.RETURN)
		submit_button = get_specific_element('//button', 'Post')
		submit_button.click()
		return buttons
	except Exception, e:
		time.sleep(10)
		return None
	

def post_on_these_pages(link, text, filename='target_list'):
	f = open(filename, 'r')
	target_ids = []
	for target in f:
		target_ids.append(target.rstrip())
	print target_ids
	for target in target_ids:
		if post_to_this_page(target, link, text) is not None:
			print "Spammed", target
		time.sleep(5)


if __name__ == "__main__":
	username = raw_input("Enter your Facebook username: ")
	password = getpass.getpass("Enter your Facebook password: ")
	link = raw_input("Enter event URL: ")
	load_driver()
	message_text = read_post_text()
	log_in(username, password)
	post_on_these_pages(link, message_text)
