🧰 Project Structure

selenium_automation/
├── main.py                # Entry point – runs all steps in sequence
├── config/
│   └── settings.py          # Paths, constants, and settings
├── scripts/
│   └── connexion_hazmat.py          # Paths, constants, and settings
├── README.md              # Project documentation
├── requirements

🚀 How to Run
Make sure you have Python 3 installed.

Install the required dependencies:

pip install selenium webdriver-manager
Place the image to uplodoad and update the path in settings.py.

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