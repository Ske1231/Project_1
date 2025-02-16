from PIL import Image

input_image = r"C:\data\image.png"
output_image = r"C:\data\image_resized.png"

img = Image.open(input_image)
img = img.resize((200, 200))  # Resize to 200x200
img.save(output_image)

print(f"✅ Image resized and saved: {output_image}")
