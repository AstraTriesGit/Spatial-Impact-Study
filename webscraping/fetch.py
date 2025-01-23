import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataFetcher:
    def __init__(self):
        """
        Sets all the options for the driver in this method itself. No need to duplicate things, right?
        Sets a driver field ready for work!
        """
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-dev-shm-usage')

        prefs = {"download.default_directory": "~/Downloads"}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://indiawris.gov.in/wris/#/groundWater")

    def download_one(self, states:list[str]):
        # wait for the entire ArcGIS application to load
        WebDriverWait(self.driver, 25).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='Groundwaterlevelnew']"))
        )

        time.sleep(25)
        # the simulated user usage
        data_download_button = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.ID, "myBtn"))
        )
        data_download_button.click()
        report_type = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.ID, "select_reportType"))
        )
        select_report_type = Select(report_type)
        select_report_type.select_by_value("Statewise")
        time.sleep(10)

        # a much more involved state selection process
        state_dropdown = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-btn"))
        )
        state_dropdown.click()
        dropdown_list = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dropdown-list"))
        )
        dropdown_list.click()
        time.sleep(10)
        for state in states:
            checkbox = WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable((By.XPATH, f"//div[text()='{state}']/preceding-sibling::input[@type='checkbox']"))
            )
            checkbox.click()
        label = self.driver.find_element(By.CLASS_NAME, "col-form-label")
        label.click()

        start_date = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.ID, "startDateDiv"))
        )
        start_date.send_keys("2024-04-01")
        end_date = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.ID, "endDateDiv"))
        )
        end_date.send_keys("2024-04-30")
        final_download_button = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.ID, "dataDownloadforReport"))
        )
        final_download_button.click()
        student_checkbox = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.ID, "Student"))
        )
        student_checkbox.click()
        name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "nameID"))
        )
        name_input.send_keys("Tony Redgrave")
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "emailID"))
        )
        email_input.send_keys("tonyredgrave.hunter@gmail.com")
        submit_button = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success"))
        )
        submit_button.click()
