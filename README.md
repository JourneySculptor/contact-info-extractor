# Contact Info Extractor

## Overview
This Python script extracts contact information such as **phone numbers** and **email addresses** from input text. It provides a user-friendly GUI built with Tkinter, allowing users to paste or type text and automatically extracts any phone numbers or email addresses found.

## Features
- **Extract Phone Numbers and Emails**: Scans input text for phone numbers and email addresses using regular expressions.
- **Save Results**: Allows users to save the extracted contact information to a `.txt` file.
- **API Integration**: Sends extracted information to an external API endpoint for further processing (if configured).
- **Clipboard Copying**: Copies extracted data to the clipboard for easy access.
- **Automated Extraction (Optional)**: Monitors the clipboard for new contact information and processes it automatically.

## Requirements
- **Python 3.6+**
- **Required Libraries**:
  - `tkinter`: GUI creation (pre-installed with Python on most platforms).
  - `re`: Regular expressions (standard library).
  - `pyperclip`: Clipboard interactions. Install with `pip install pyperclip`.
  - `requests`: Sending data to an API endpoint. Install with `pip install requests`.

## Installation
1. Clone the Repository and Navigate to the Project Directory:
   git clone https://github.com/JourneySculptor/contact-info-extractor.git && cd contact-info-extractor

2. Install Required Libraries:
   pip install pyperclip requests

## Usage
1. Run the script:
   python contact_info_extractor.py

2. Extract Contact Information:
   Enter or paste text containing phone numbers or email addresses into the input box.
   Click the "Extract Info" button to display the extracted contact information.

3. Save Results:
   Select the "Save" option to store the extracted information in a `.txt file`, using the file dialog that appears.

4. Send Data to API (Optional):
   To enable API data submission, replace the placeholder `api_url` in the script with your actual endpoint.

   Example:
   api_url = "https://your-api-endpoint.com/api"


## Configuration
**API Endpoint**: To use the API feature, update the `api_url` variable in `contact_info_extractor.py` with your endpoint URL.

## Example

**Input:**
  Contact: johndoe@example.com, Phone: 123-456-7890
  
**Output:**
  Email: johndoe@example.com
  Phone: 123-456-7890

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
JourneySculptor 
