import requests
# Import the requests module

url = "http://www.example.com"
# Define the URL to request
response = requests.get(url)
# Make a GET request to the URL

if response.status_code == 200:
    # If the response status code is 200 (success)
    print("Request successful")
    # Print a success message
    print("Response body:", response.text)
    # Print the response body

    # Write the response text to a file
    with open('output.html', 'w', encoding='utf-8') as f:
        # Open a file named 'output.html' in write mode
        f.write(response.text)
        # Write the response text to the file
else:
    # If the response status code is not 200
    print("Request failed with status code:", response.status_code)
    # Print an error message with the status code