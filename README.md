# WhatsApp-Web-Mention-Everyone

This project automates the process of mentioning all members in a WhatsApp Web group chat using Selenium WebDriver.

## Prerequisites

- Python
- Selenium
- Firefox browser
- GeckoDriver

## Setup

1. **Install Selenium:**

   ```bash
   pip install selenium
   ```
2. **Download and Install GeckoDriver:**

    ```bash
    sudo snap install geckodriver
    ```

## Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AnjulaAbey/WhatsApp-Web-Mention-Everyone.git
    cd whatsapp-web-mention-everyone
    ```
2. **Run the Script:**

    ```bash
    python mention.py
    ```
3. **Follow the prompts:**

    - Enter the name of the WhatsApp group.
    - Enter the number of members in the group.

4. **Scan the QR code:**

Scan the QR code using your phone in the opened firefox window. 

## Description

The script performs the following steps:

1. Opens WhatsApp Web and waits for the user to scan the QR code.
2. Searches for the specified group name.
3. Opens the group info.
4. Loads the group members by pressing the down arrow key.
5. Retrieves and filters the group members.
6. Mentions each member in the group chat.

## Configuration

- Path to GeckoDriver:

     Ensure the driver_path variable in the script points to the correct location of your GeckoDriver executable.

## Notes

- The script currently only supports Firefox as the browser.
- Ensure your WhatsApp Web is logged in and the QR code is scanned within the specified timeout period.
- Adjust the sleep times in the script as needed based on your network speed and system performance.

## Troubleshooting

- If the script fails to find elements, ensure the XPaths used in the script are correct and haven't changed due to WhatsApp Web updates.
- Increase the wait times if elements are not loading within the specified time.

## Contributors

<a href="https://github.com/AnjulaAbey/WhatsApp-Web-Mention-Everyone/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AnjulaAbey/WhatsApp-Web-Mention-Everyone" />
</a>
