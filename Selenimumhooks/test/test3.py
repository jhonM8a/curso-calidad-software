from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from warnings import filterwarnings
filterwarnings("ignore")
import unittest

class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_unillanos(self):
		urlGeneral = 'https://www.unillanos.edu.co/'
		
		self.browser.get(urlGeneral)
		numberWhatsapp = self.browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div/footer/div/div/div[2]/div/p[10]')
		print(numberWhatsapp.text)
		self.assertEqual("Whatsapp +57 322 292 31 94",numberWhatsapp.text)


	def test_unillano_contactos_tres(self):
		urlGeneral = 'https://admisiones.unillanos.edu.co/'
		self.browser.get(urlGeneral)
		contactos = self.browser.find_elements(By.XPATH, '//*[@id="custom-7363-particle"]/div/ul/li/strong')
		
		res = []
		for contacto in contactos:
			res.append(contacto.text)
		self.assertTrue(3, len(res))
		

	def test_verify_campus(self):
		urlGeneral = 'https://admisiones.unillanos.edu.co/'

		self.browser.get(urlGeneral)
		campusBarcelona = self.browser.find_element(By.XPATH, '/html/body/div[2]/footer/div/div[1]/div[1]/div/div/ul/li[1]/strong')

		print(campusBarcelona.text.replace("\n", ""))
		campusClean = campusBarcelona.text.replace("\n", "")
		self.assertEqual(campusClean, "Campus Barcelona:")
				
	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()