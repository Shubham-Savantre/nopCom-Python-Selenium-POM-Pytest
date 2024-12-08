from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


def create_driver():
    # Install the Edge driver using the manager
    service = Service(EdgeChromiumDriverManager().install())

    # Configure Edge browser options
    options = webdriver.EdgeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
    options.add_argument("start-maximized")  # Start the browser maximized
    options.add_argument("--disable-infobars")  # Disable info bars
    options.add_argument("--disable-extensions")  # Disable extensions
    options.add_argument("--disable-notifications")  # Disable notifications
    options.add_argument("--incognito")  # Use incognito mode
    options.add_argument("--lang=en-US")  # Set browser language to English (optional)

    # Set a realistic User-Agent to mimic a real browser
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    )

    # Instantiate the Edge WebDriver
    driver = webdriver.Edge(service=service, options=options)
    return driver
