from selenium import webdriver
import time
from warnings import filterwarnings

filterwarnings("ignore")

browser = webdriver.Chrome()

urls = ["https://google.com/", "https://facebook.com/", "https://x.com/", "https://wikipedia.com"]

browser.get(urls[0])
time.sleep(2)

for url in urls[1:]:
    browser.execute_script(f"window.open('{url}', '_blank');")
    time.sleep(2)

try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()
