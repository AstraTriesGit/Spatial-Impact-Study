from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#defining driver options
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
prefs = {"download.default_directory": "."}
options.add_experimental_option("prefs", prefs)
# initializing chrome instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# sent GET request to the site using the driver
driver.get("https://indiawris.gov.in/wris/#/groundWater")
print("\nPage's title is: \n", driver.title)
time.sleep(25)

# Switch to the ArcGIS iframe if present
iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src*='Groundwaterlevelnew']")
driver.switch_to.frame(iframe)

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "myBtn"))
)
button.click()

# driver.close()