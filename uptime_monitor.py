import requests
import datetime #This lets us work with dates and times :P. For now, use steps (ex. 1, 2, 3) to mark the steps for writing to a textfile

# The URL we want to monitor
url = "https://www.google.com"

# 1. Grab the exact time the script runs and format it nicely
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    # response variable uses the requests library to get the url
    # establishes a timeout rule of 3 secs to connect to the server, 10 secs to read the response
    response = requests.get(url, timeout=(3, 10))
    response.raise_for_status()

    # We capture our final message in a variable so we can print AND log it
    if "Google" in response.text:
        log_message = f"{timestamp} - SUCCSESS - Status Code: {response.status_code}"
    else:
        log_message = f"{timestamp} - ERROR - Site loaded, but expected content missing"

except requests.exceptions.RequestException as e:
    log_message = f" {timestamp} - ALERT - Unreachable: {e}"

# Print the log message to the console so we can see it running
print(log_message)
# 2. Create a textfile and write the result to said textfile
with open("uptime_log.txt", "a") as file:
    file.write(log_message + "\n")
