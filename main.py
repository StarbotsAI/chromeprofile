import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
PROFILE_PATH = os.path.join(SCRIPT_DIR, "chrome_profile_jusbrasil")

def jusbrasil_login_and_wait():
    # Chrome options configuration
    options = uc.ChromeOptions()
    options.add_argument(f"--user-data-dir={PROFILE_PATH}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=pt-BR")
    
    # Initialize driver
    driver = uc.Chrome(options=options)
    
    # Anti-detection script
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        """
    })
    
    # Open login page
    print("Abrindo página de login do JusBrasil...")
    driver.get("https://www.jusbrasil.com.br/login")
    
    # Wait for user to manually login and reach the search page
    print("Por favor, faça o login manualmente.")
    print("O script será finalizado quando você acessar a página de busca.")
    
    while True:
        current_url = driver.current_url
        if "https://www.jusbrasil.com.br/iniciar-pesquisas" in current_url:
            print("Página de busca detectada!")
            print(f"Perfil do Chrome salvo em: {PROFILE_PATH}")
            break
        time.sleep(1)
    
    # Take screenshot before finishing
    driver.save_screenshot("screenshot.png")
    print("Screenshot salvo como 'screenshot.png'")
    
    # Close the browser
    driver.quit()
    print("Script finalizado com sucesso!")

if __name__ == "__main__":
    jusbrasil_login_and_wait()
