from sentence_transformers import SentenceTransformer, util

# Load the model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read comments file
with open("C:/data/comments.txt", "r", encoding="utf-8") as file:
    comments = file.readlines()

# Convert comments to embeddings
embeddings = model.encode(comments)

# Find most similar pair
max_similarity = 0
best_pair = ("", "")

for i in range(len(comments)):
    for j in range(i + 1, len(comments)):
        similarity = util.cos_sim(embeddings[i], embeddings[j]).item()
        if similarity > max_similarity:
            max_similarity = similarity
            best_pair = (comments[i].strip(), comments[j].strip())

# Save the most similar comments
with open("C:/data/comments-similar.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(best_pair))

print(f"✅ Most similar comments saved.")
