import pandas as pd
import re

# Update the file path to the location of your exported WhatsApp chat file
file_path = 'scrap.txt'

# Initialize lists to store chat data
dates = []
times = []
contacts = []
messages = []
emails = []

# Regular expression pattern to detect email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.split(' - ')
        if len(parts) == 2:
            date_time, message_part = parts
            date, time = date_time.split(', ')
            contact_message = message_part.split(': ', 1)
            if len(contact_message) == 2:
                contact, message = contact_message
                dates.append(date)
                times.append(time)
                contacts.append(contact)
                messages.append(message)

                # Find email addresses in the message
                email_matches = re.findall(email_pattern, message)
                if email_matches:
                    emails.append(", ".join(email_matches))
                else:
                    emails.append(None)

# Create a DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Time': times,
    'Full Name': contacts,
    'Message': messages,
    'Email': emails
})

# Export to CSV
df.to_csv('whatsapp_chat_data_with_fullnames_and_emails.csv', index=False)

print("Chat data saved to whatsapp_chat_data_with_fullnames_and_emails.csv")
