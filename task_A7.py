import re

# Read email file
with open("C:/data/email.txt", "r", encoding="utf-8") as file:
    email_content = file.read()

# Extract sender email using regex
match = re.search(r"From:\s*(\S+@\S+)", email_content)

# If found, save it
if match:
    sender_email = match.group(1)
    with open("C:/data/email-sender.txt", "w", encoding="utf-8") as file:
        file.write(sender_email)
    print(f"✅ Extracted sender email: {sender_email}")
else:
    print("❌ No email found in the file.")
