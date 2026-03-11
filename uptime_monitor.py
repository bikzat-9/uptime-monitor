import requests
import datetime
import os
from dotenv import load_dotenv

# This tells Python: "Find the hidden .env file and load the secrets right now"
load_dotenv()

# This grabs the specific URL you pasted and saves it as a variable
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# --- NEW: THE DISCORD ALERT FUNCTION ---
def send_discord_alert(message):
    if WEBHOOK_URL:
        # Package the message exactly how Discord likes it
        payload = {"content": message}
        requests.post(WEBHOOK_URL, json=payload)
    else:
        print("No Discord Webhook URL found. Skipping alert.")
# ---------------------------------------

# The URL we want to monitor
url = "https://www.google.com/this-page-does-not-exist"

# 1. Grab the exact time the script runs and format it nicely
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    # response variable uses the requests library to get the url
    # establishes a timeout rule of 3 secs to connect to the server, 10 secs to read the response
    response = requests.get(url, timeout=(3, 10))
    response.raise_for_status()

    # We capture our final message in a variable so we can print AND log it
    if "Google" in response.text:
        log_message = f"{timestamp} - SUCCESS - Status Code: {response.status_code}"
    else:
        log_message = f"{timestamp} - ERROR - Site loaded, but expected content missing"
        # NEW: Trigger the alert because the site is missing content!
        send_discord_alert(f"🚨 {log_message}")

except requests.exceptions.RequestException as e:
    log_message = f" {timestamp} - ALERT - Unreachable: {e}"
    # NEW: Trigger the alert because the site is completely down!
    send_discord_alert(f"🚨 {log_message}")

# Print the log message to the console so we can see it running
print(log_message)
# 2. Create a textfile and write the result to said textfile
with open("uptime_log.txt", "a") as file:
    file.write(log_message + "\n")
