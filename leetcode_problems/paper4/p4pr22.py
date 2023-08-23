import re

# Read URLs from the input file
with open("input.txt", "r") as input_file:
    urls = input_file.read().splitlines()

# Initialize output file
with open("output.txt", "w") as output_file:
    # Loop through each URL
    for url in urls:
        # Check if URL is valid using regex
        if re.match(r"^(https:\/\/)([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}$", url):
            status = "valid"
        else:
            status = "invalid"
        
        # Write URL and status to output file
        output_file.write(url + ", " + status + "\n")

#....................Without regex......................

# Define a function to check if a given string contains only valid characters
def is_valid_string(s):
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-")
    return all(c in valid_chars for c in s)

# Read URLs from the input file
with open("input.txt", "r") as input_file:
    urls = input_file.read().splitlines()

# Initialize output file
with open("output.txt", "w") as output_file:
    # Loop through each URL
    for url in urls:
        # Check if URL starts with "https://"
        if not url.startswith("https://"):
            status = "invalid"
        else:
            # Remove "https://" prefix
            url = url[8:]
            # Check if remaining characters are valid
            if is_valid_string(url):
                status = "valid"
            else:
                status = "invalid"
        
        # Write URL and status to output file
        output_file.write("https://" + url + ", " + status + "\n")
