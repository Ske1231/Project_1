import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Example API
output_file = r"C:\data\api_data.json"

try:
    response = requests.get(url)
    response.raise_for_status()

    with open(output_file, "w") as f:
        f.write(response.text)

    print(f"✅ Data saved to {output_file}")

except requests.exceptions.RequestException as e:
    print(f"🚨 API request failed: {e}")
