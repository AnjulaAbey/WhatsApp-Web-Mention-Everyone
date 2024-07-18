from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


# Inputs
n= 10 # Number of times to press the down arrow key to load more contacts
group = "cse track xi" # Group name
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
time.sleep(10)
# Find the search input and interact with it
try:
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    
    group_name = group 
    for char in group_name:
        search_box.send_keys(char)

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
    time.sleep(60)
    members = []
    # Check if the specific element is visible
    try:
        special_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@role="button"][@tabindex="0"][@data-ignore-capture="any"]'))
        )
        if n<15:
            print("group members are less than 15")
            member_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@role="gridcell"]//span[@dir="auto"]'))
            )
                # Retrieve all group members
            for element in member_elements:
                members.append(element.text)
            members.pop(0)
            members.remove('You')
            # Go back to the group chat
            driver.find_element(By.XPATH, '//div[@aria-label="Close"]').click()
            print("Back to group chat")
        elif special_element:
            print("Special element is visible.")
            special_element.click()
            time.sleep(10)
            # Simulate pressing the down arrow key to load more contacts
            body = driver.find_element(By.TAG_NAME, 'body')
            for i in range(n):  
                body.send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2) 
                if(i%10 == 0):
                    member_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@role="gridcell"]//span[@dir="auto"]'))
            )
                # Retrieve all group members
                    for element in member_elements:
                        members.append(element.text)
                # Go back to the group chat
            driver.find_element(By.XPATH, '//div[@aria-label="Close"]').click()
            time.sleep(5)
            driver.find_element(By.XPATH, '//div[@aria-label="Close"]').click()
            print("Back to group chat")

        else:
            print("Special element is not visible.")
            member_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@role="gridcell"]//span[@dir="auto"]'))
            )
                # Retrieve all group members
            for element in member_elements:
                members.append(element.text)
    except Exception as e:
        print("Special element is not present.")
        member_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@role="gridcell"]//span[@dir="auto"]'))
        )
    

    members = list(set(members))
    print(len(members))
    # Filter out members with \u202f and modify phone numbers
    filtered_members = []
    for member in members:
        if '\u202f' not in member:
            if member.startswith('+'):
                filtered_members.append(member[:-1])
            else:
                filtered_members.append(member[:-1])
    
    # Print filtered members list
    print("Filtered Members List:", end=' ')
    print(filtered_members)
    time.sleep(5)
    

    
    # Wait for the chat to load
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-lexical-editor="true"]'))
    )

    # Mentioning everyone in the group
    chat_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    chat_box.click()

    # Typing the mentions
    for member in filtered_members:
        chat_box.send_keys('@')
        for char in member:
            chat_box.send_keys(char)
        time.sleep(1)
        chat_box.send_keys(Keys.TAB)
        chat_box.send_keys(Keys.SPACE)

    # Sending the message
    # chat_box.send_keys(Keys.ENTER)

    print("Message sent!")

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    # Quit the driver
    print("Quitting the driver...")
    driver.quit()
