from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your geckodriver
driver_path = '/snap/bin/geckodriver'
service = Service(executable_path=driver_path)

# Open WhatsApp Web
driver = webdriver.Firefox(service=service)
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code
print("Please scan the QR code to log in to WhatsApp Web.")
WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
)

print("QR code scanned. Logging in...")

# Wait for WhatsApp Web to load completely
WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
)

print("WhatsApp Web loaded.")

# Find the search input and interact with it
try:
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    
    group_name= "CsE tRaCk Xi" #Group name
    for i in range(0,len(group_name)):
        search_box.send_keys(group_name[i])

    
    # Wait for the search box to update with the full query
    time.sleep(5)  # Adjust as needed
    
    # Press Enter to perform the search
    search_box.send_keys(Keys.ENTER)
    
    # Wait for search results or group to load
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//header//div[@title="Profile details"]'))
    )

    # Open group info
    group_info_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//header//div[@title="Profile details"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", group_info_button)
    group_info_button.click()
    time.sleep(1)
    
    # Wait for group info to load
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@title="Group info"]'))
    )
    print("Group Info Loaded")
    time.sleep(10)

    # Find and click the target element directly
    try:
        target_element_xpath = '//span[@data-icon="exit"]'
        target_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, target_element_xpath))
        )
        target_element.click()
        print("Clicked on the target element.")
        time.sleep(10)
    except Exception as e:
        print(f"Error occurred while clicking the target element: {str(e)}")

    # Example: Retrieve all group members (you can modify as per your actual use case)
    members = driver.find_elements(By.XPATH, '//div[@role="button"]//span[@dir="auto"]')
    group_members = [member.text for member in members]

    # Go back to the group chat
    driver.find_element(By.XPATH, '//span[@data-icon="x"]').click()

    # Wait for the chat to load
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]'))
    )

    # Mentioning everyone in the group
    chat_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
    chat_box.click()

    # Typing the mentions
    for member in group_members:
        chat_box.send_keys('@' + member)
        time.sleep(1)
        chat_box.send_keys(Keys.TAB)

    # Sending the message
    chat_box.send_keys(Keys.ENTER)

    print("Message sent!")

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    # Quit the driver
    driver.quit()

