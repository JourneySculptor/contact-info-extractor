import tkinter as tk  # GUI library
import re  # For regex pattern matching
import pyperclip  # Clipboard operations
import requests  # For API requests
import time  # Time management for scheduling
from tkinter import filedialog  # Save file dialog

# Function to extract patterns (e.g., phone numbers, emails) from text
def extract_pattern(regex, text):
    matches = []
    invalid_entries = []
    for groups in regex.findall(text):
        if isinstance(groups, tuple):
            if groups[0]:  # If there's a match in the tuple, add it
                matches.append(groups[0])
            else:
                invalid_entries.append('Invalid entry')
        else:
            matches.append(groups)  # Directly add non-tuple matches
    # Debug print to see extracted matches and invalid entries
    print("Matches:", matches)
    print("Invalid Entries:", invalid_entries)
    return matches, invalid_entries

# Remove duplicates from extracted results
def format_results(matches):
    return list(set(matches))

# Save extracted data to a specified file
def save_to_file(data):
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'a') as file:
            file.write(data + '\n')
        result_label.config(text=f'Results saved to {file_path}')

# Send extracted data to an API endpoint
def send_to_api(data):
    api_url = "https://example.com/api"  # Replace with actual API endpoint
    headers = {'Content-Type': 'application/json'}
    payload = {'extracted_data': data}
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            result_label.config(text='Data sent to API successfully.')
        else:
            result_label.config(text='Failed to send data to API.')
    except requests.exceptions.RequestException as e:
        result_label.config(text=f'Error: {e}')

# Function to periodically extract data from clipboard
def schedule_extraction(interval=60):
    while True:
        text = pyperclip.paste()
        phone_matches, _ = extract_pattern(phone_regex, text)
        email_matches, _ = extract_pattern(email_regex, text)
        if phone_matches or email_matches:
            result = '\n'.join(format_results(phone_matches + email_matches))
            pyperclip.copy(result)
            result_label.config(text=f'Scheduled extraction:\n{result}')
            save_to_file(result)
            send_to_api(result)
        time.sleep(interval)

# Extract phone numbers and emails from input text
def extract_info():
    text = text_box.get('1.0', tk.END)
    phone_matches, invalid_phone_matches = extract_pattern(phone_regex, text)
    email_matches, invalid_email_matches = extract_pattern(email_regex, text)
    matches = phone_matches + email_matches

    if matches:
        result = '\n'.join(format_results(matches))
        pyperclip.copy(result)
        result_label.config(text=f'Results copied to clipboard:\n{result}')
        save_to_file(result)
        send_to_api(result)
    else:
        result_label.config(text='No valid phone numbers or email addresses.')

    invalid_matches = invalid_phone_matches + invalid_email_matches
    if invalid_matches:
        invalid_label.config(text='Invalid entries:\n' + '\n'.join(invalid_matches[:5]))  # Show only first 5 invalid entries
    else:
        invalid_label.config(text='No invalid entries found.')

# GUI setup
root = tk.Tk()
root.title('Contact Info Extractor')

instruction_label = tk.Label(root, text='Enter text containing phone numbers or email addresses:')
instruction_label.pack()

text_box = tk.Text(root, height=10, width=50)
text_box.pack()

extract_button = tk.Button(root, text='Extract Info', command=extract_info)
extract_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

invalid_label = tk.Label(root, text='')
invalid_label.pack()

# Updated regex patterns for phone numbers and emails
phone_regex = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')  # Improved phone number pattern
email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')  # Improved email pattern

root.mainloop()
