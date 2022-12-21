# self.driver.execute_script("window.history.go(-1)")
from selenium import webdriver
from time import sleep
driver_path = '/Users/basavaprasadgola/Codes/Python/unfollowed/chromedriver'

class InstaBot:
	def __init__(self,username, password):
		self.username = username
		self.driver = webdriver.Chrome(driver_path)
		self.driver.get("https://instagram.com")
		sleep(1)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
		self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
		sleep(2)
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		sleep(2)

	def get_followers(self):
		self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
		sleep(2)
		self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
		sleep(1)
		following = self. _get_names()
		self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
		sleep(2)
		followers = self._get_followers()
		not_following_back = [user for user in following if user not in followers]
		print(not_following_back)



	def _get_names(self):
		sleep(1)
		scroll_box = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]")

		last_ht, ht = 0, 1
		while last_ht != ht:
			last_ht = ht 
			sleep(1)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""",scroll_box)
		sleep(1)
		links = scroll_box.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']
		
		self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/button").click()
		return names

	def _get_followers(self):
		sleep(1)
		scroll_box = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]")

		last_ht, ht = 0, 1
		while last_ht != ht:
			last_ht = ht 
			sleep(1)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""",scroll_box)
		sleep(1)
		links = scroll_box.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']
		self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/button").click()
		return names



My_bot = InstaBot('prasad_gola', 'Fibonacci1491625')
My_bot.get_followers()

