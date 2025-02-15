import os
from PIL import Image

# Use a raw string (r"") to avoid path issues
image_path = r"C:\data\credit_card.png"

# Debugging: Check if Python can see the file
if os.path.exists(image_path):
    print(f"✅ File exists: {image_path}")
else:
    print(f"❌ Python still can't find the file: {image_path}")
    exit()  # Stop execution if the file is missing

# Open the image
image = Image.open(image_path)
print("✅ Image opened successfully!")

