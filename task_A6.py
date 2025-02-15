import json
import os

docs_path = "C:/data/docs/"
index = {}

# Check if the folder exists
if not os.path.exists(docs_path):
    print(f"❌ Error: Folder {docs_path} does not exist!")
else:
    md_files = [f for f in os.listdir(docs_path) if f.endswith(".md")]

    # Print found Markdown files
    if not md_files:
        print("❌ No Markdown (.md) files found in /data/docs/")
    else:
        print(f"📄 Found {len(md_files)} Markdown files: {md_files}")

    # Extract first H1 title from each file
    for file in md_files:
        with open(os.path.join(docs_path, file), 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith("# "):  # Detect H1 title
                    index[file] = line.strip()[2:]  # Remove "# " and store title
                    print(f"✅ Extracted title from {file}: {index[file]}")
                    break  # Stop after first H1

# Save the index
with open("C:/data/docs/index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2)

print(f"🎯 Markdown index saved to C:/data/docs/index.json")

