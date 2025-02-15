import json

# Read file
with open('/data/contacts.json', 'r') as file:
    contacts = json.load(file)

# Sort by last_name, then first_name
contacts_sorted = sorted(contacts, key=lambda x: (x['last_name'], x['first_name']))

# Write sorted output
with open('/data/contacts-sorted.json', 'w') as file:
    json.dump(contacts_sorted, file, indent=2)

print("Contacts sorted and saved to /data/contacts-sorted.json")
