from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar el navegador
browser = webdriver.Chrome()

try:
    # Abrir la página
    browser.get("https://campusvirtualunillanos.co/")

    # Buscar un elemento utilizando el XPath específico
    element = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/section[2]/div/div/div[2]/div/div[1]/div/h3')
    element2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/section[2]/div/div/div[2]/div/div[2]/div/h3')

    

    # Obtener y mostrar el texto del elemento
    print(f"Texto del elemento encontrado: {element.text}")
    print(f"Texto del elemento encontrado: {element2.text}")

finally:
    # Cerrar el navegador
    browser.quit()
