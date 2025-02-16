import os

file_to_delete = r"C:\data\logs\log1.txt"  # File path

if os.path.exists(file_to_delete):
    print("🚨 File deletion is not allowed!")
else:
    print("✅ File does not exist, nothing to delete.")
