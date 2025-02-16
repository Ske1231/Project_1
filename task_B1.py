import os

# Correct path to access /data/logs/log1.txt
file_to_access = "C:/data/logs/log1.txt"

if os.path.exists(file_to_access):
    with open(file_to_access, "r") as f:
        content = f.read()
        print(content)
else:
    print("🚨 File not found:", file_to_access)

