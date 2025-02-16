import markdown
import os

# File paths
input_file = "C:/data/document.md"
output_file = "C:/data/document.html"

# Check if the markdown file exists
if not os.path.exists(input_file):
    print(f"🚨 File not found: {input_file}")
    exit(1)

# Read the Markdown file
with open(input_file, "r", encoding="utf-8") as md_file:
    md_content = md_file.read()

# Convert to HTML
html_content = markdown.markdown(md_content)

# Write to the output HTML file
with open(output_file, "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print(f"✅ Markdown converted to HTML: {output_file}")
