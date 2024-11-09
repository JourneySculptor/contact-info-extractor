# Contact Info Extractor

## Overview
This Python script extracts contact information such as **phone numbers** and **email addresses** from input text. It provides a user-friendly GUI built with Tkinter, allowing users to paste or type text and automatically extracts any phone numbers or email addresses found.

## Features
- **Extract Phone Numbers and Emails**: Scans input text for phone numbers and email addresses using regular expressions.
- **Save Results**: Allows users to save the extracted contact information to a `.txt` file.
- **API Integration**: Sends the extracted information to an external API endpoint for further processing (if configured).
- **Clipboard Copying**: Copies the extracted data to the clipboard for easy access.
- **Automated Extraction (Optional)**: Checks the clipboard periodically for new contact information and processes it automatically.

## Requirements
- **Python 3.6+**
- **Required Libraries**:
  - `tkinter`: For creating the GUI (pre-installed with Python on most platforms).
  - `re`: For regular expressions (standard library).
  - `pyperclip`: To interact with the clipboard. Install with `pip install pyperclip`.
  - `requests`: For sending data to an API endpoint. Install with `pip install requests`.

## Installation
1. Clone the repository:
   git clone https://github.com/JourneySculptor/contact-info-extractor.git

2. Navigate to the project directory:
   cd contact-info-extractor
   
3. Install the required packages:
   pip install -r requirements.txt

## Usage
1. Run the script:
   python contact_info_extractor.py

2. Enter or paste text containing phone numbers or email addresses in the input box.

3. Click Extract Info to see the extracted contact information.

4. Save Results: Choose a file to save the extracted information by following the file dialog that appears.

5. Send to API: The script sends the results to an external API if configured. You may need to replace https://example.com/api in the code with your actual endpoint.

## Configuration
**API Endpoint**: To use the API feature, update the api_url variable in contact_info_extractor.py with your endpoint URL.
api_url = "https://your-api-endpoint.com/api"

## Example
Example of the input and output:

**Input:**
  Contact: johndoe@example.com, Phone: 123-456-7890
  
**Output:**
  Email: johndoe@example.com
  Phone: 123-456-7890

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
JourneySculptor 
