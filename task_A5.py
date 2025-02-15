import os

# List log files sorted by modification time (most recent first)
log_files = sorted(
    [f for f in os.listdir('/data/logs/') if f.endswith('.log')],
    key=lambda f: os.path.getmtime(os.path.join('/data/logs/', f)),
    reverse=True
)[:10]

# Extract first lines
first_lines = []
for log in log_files:
    with open(f'/data/logs/{log}', 'r') as file:
        first_lines.append(file.readline().strip())

# Write to output file
with open('/data/logs-recent.txt', 'w') as file:
    file.write("\n".join(first_lines))

print("Extracted first lines saved to /data/logs-recent.txt")
