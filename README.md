🧰 Project Structure
bash
Copy
Edit
selenium_automation/
├── main.py                # Entry point – runs all steps in sequence
├── login.py               # Handles browser setup and login to the system
├── form_fill.py           # Handles form filling and intermediate steps
├── file_upload.py         # Handles file upload and final confirmation
├── utils/
│   └── config.py          # Paths, constants, and settings
├── assets/
│   └── sample_file.png    # File used for upload (example)
├── README.md              # Project documentation
🚀 How to Run
Make sure you have Python 3 installed.

Install the required dependencies:

bash
Copy
Edit
pip install selenium webdriver-manager
Place the file to upload in the assets/ folder and update the path in config.py.

Run the main script:
python main.py

🔄 Description of Steps
login.py: Launches the browser with anti-bot detection options and logs into the platform using provided credentials.

form_fill.py: Navigates through the platform menus and fills in a form with sample data.

file_upload.py: Uploads a predefined file and optionally saves the form.

main.py: Orchestrates the execution of all scripts in order.

🧠 Technologies Used
Python 3

Selenium WebDriver

WebDriver Manager (for automatic ChromeDriver setup)

⚠️ Notes
This automation works with static XPATHs and might break if the webpage layout changes.

Always test and update the XPATHs if the application is updated.