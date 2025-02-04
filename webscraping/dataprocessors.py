from selenium.webdriver.remote.webelement import WebElement

class DataProcessor:
    def __init__(self):
        pass

    def extract_row_data(self, row_element: WebElement):
        # Create a dictionary to store the data
        data = {}

        # Find all div elements within td cells that have field-* classes
        cells = row_element.find_elements("css selector", "td[class*='field-'] div")

        # Extract field name and value from each cell
        for cell in cells:
            # Get the parent td element
            parent_td = cell.find_element("xpath", "..")
            # Extract the field name from the class (after 'field-')
            field_class = parent_td.get_attribute("class")
            field_name = field_class.split("field-")[1].split()[0]
            # Get the text value
            value = cell.text.strip()
            data[field_name] = value

        return data