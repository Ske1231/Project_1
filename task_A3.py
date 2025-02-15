from datetime import datetime

# List of possible date formats in the file
date_formats = [
    "%b %d, %Y",         # Example: Mar 07, 2016
    "%Y-%m-%d",          # Example: 2016-03-07
    "%Y/%m/%d %H:%M:%S", # Example: 2014/02/22 18:50:22
    "%d-%m-%Y",          # Example: 07-03-2016
    "%m/%d/%Y",          # Example: 03/07/2016
]

# Function to parse date with multiple formats
def parse_date(date_str):
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    return None  # If no format matches, return None

# Read file
with open('C:/data/dates.txt', 'r') as file:
    dates = file.readlines()

# Count Wednesdays
wednesday_count = sum(1 for date in dates if (parsed_date := parse_date(date)) and parsed_date.weekday() == 2)

# Write output
with open('C:/data/dates-wednesdays.txt', 'w') as file:
    file.write(str(wednesday_count))

print(f"Number of Wednesdays: {wednesday_count}")


